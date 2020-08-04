import requests
import json
import spotipy
from django.shortcuts import redirect
from spotipy import oauth2
import urllib
import os
from dotenv import load_dotenv
from django.templatetags.static import static

load_dotenv()

USERNAME = "jordantwells"
SP_CLIENT_ID = os.environ.get('LC_CLIENT_ID')
SP_CLIENT_SECRET = os.environ.get('LC_CLIENT_SECRET')
SP_REDIRECT_URI = "http://127.0.0.1:8000/webapps/lyric-cloud/"
SP_SCOPE = "user-read-recently-played user-read-playback-state user-read-private user-library-modify"

def user_login():
	user_response = requests.get("https://accounts.spotify.com/authorize", params = {
    "client_id" : SP_CLIENT_ID,
    "response_type" : "code",
    "redirect_uri" : SP_REDIRECT_URI,
    "state" : "dog",
    "scope": SP_SCOPE  
		})
	return redirect(user_response.url)

def	get_access_token(code):
	access_token = requests.post("https://accounts.spotify.com/api/token", 
		data = {
			'Content-Type': 'application/x-www-form-urlencoded',
			"grant_type" : "authorization_code",
			"code" : code,
			"redirect_uri": SP_REDIRECT_URI,
			"client_id": SP_CLIENT_ID,
			"client_secret" : SP_CLIENT_SECRET
			})
	return access_token.json()["access_token"]

from bs4 import BeautifulSoup


def lyric_scraper(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html('script')]
    lyrics = html.find("div",  class_= "lyrics").get_text()
    return lyrics

import re
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt,mpld3




def generate_lyric_cloud(access_token):
	header = {"Authorization" :f"Bearer {access_token}"}
	recently_played_data = requests.get("https://api.spotify.com/v1/me/player/recently-played",
		headers = header,
		params = {"limit": 15}).json()
	print(recently_played_data)

	song_titles = []
	song_artists = []

	for item in recently_played_data['items']:
	    song_titles.append(item["track"]['name'])
	    song_artists_per_song = [artist["name"] for artist in item["track"]["artists"]]
	    song_artists.append(song_artists_per_song)

	GE_API_URL = "https://api.genius.com/"
	GE_SCOPE = "me"
	GE_ACCESS_TOKEN = os.environ.get("GE_ACCESS_TOKEN")

	headers = {"Authorization" : "Bearer "+ GE_ACCESS_TOKEN}
	


	all_lyrics = ""
	for i, song_title in enumerate(song_titles):
	    search = requests.get(GE_API_URL + "search", headers = headers, params = {"q" : song_title}).json()
	    hits = search["response"]["hits"]
	    
	    if len(hits) != 0:
	        result = hits[0]["result"]
	        artists = result["primary_artist"]["name"].split(",")
	        
	        #Splitting on & here fixes some problems with musicals
	        if (artists[0].split(" &")[0] in song_artists[i]) or (artists[0] in song_artists[i]):
	            result_url = result["url"]
	            print(result_url)
	            lyric = lyric_scraper(result_url)
	            all_lyrics += lyric
	        
	
	regex = re.compile(".*?\[(.*?)\]")
	all_lyrics = re.sub(regex, "", all_lyrics)



	#mask = np.array(Image.open(static("spotify_logo.png")))

	wc = WordCloud(background_color="white", max_words=2000, contour_width=0, contour_color='steelblue')
	wc.generate(all_lyrics)
	plt.axis("off")
	plt.figure(figsize=(9, 5), dpi = 600)
	plt.imshow(wc, interpolation='bilinear')
	plt.axis("off")


	plt.savefig("CLOUDYCLOUD", format = "png")
	return Image.open("CLOUDYCLOUD.png")
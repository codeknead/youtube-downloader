from __future__ import unicode_literals
import youtube_dl
import urllib
import urllib.parse
from bs4 import BeautifulSoup


class Manager:
	YOUTUBE_URL = "https://www.youtube.com/results?search_query="
	youtube_url = []
	isPlayList = False
	ydl_opts = {
		'format': 'bestaudio/best',  # choice of quality
		'extractaudio': True,  # only keep the audio
		'audioformat': "mp3",  # convert to mp3
		'outtmpl': '%(id)s',
	}

	def search_youtube_urls(self, text_to_search, isPlayList):
		self.isPlayList = isPlayList
		query = urllib.parse.quote(text_to_search)
		url = self.YOUTUBE_URL + query
		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html)
		if self.isPlayList is True:
			for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
				self.youtube_url.append('https://www.youtube.com' + vid['href'])
		else:
			vid = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
			self.youtube_url.append('https://www.youtube.com' + vid[0]['href'])

	def download(self):
		with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
			if len(self.youtube_url) > 0 and self.isPlayList is True:
				for i in range(len(self.youtube_url)):
					ydl.download([self.youtube_url[i]])
			else:
				if len(self.youtube_url) > 0:
					ydl.download([self.youtube_url[0]])



from manager import Manager

if __name__ == "__main__":
	search_text = input()
	isPlaylist = input()
	yp = Manager()
	yp.search_youtube_urls(search_text, isPlaylist)
	yp.download()

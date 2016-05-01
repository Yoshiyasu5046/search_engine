
def get_source(url):
	if url == "view-source:http://example.webscraping.com/":
		return open_file(source)
	else:
		return None
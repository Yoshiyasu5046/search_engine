def open_file(source):
    with open(source, "r") as f :
        output = f.read(30)
        return output
    open_source.close()

#print open_file("sample_source.html")


def get_next_target(source):
    source = open_file(source)
    start_link = source.find("<a href=")
    if start_link == -1:
        return None, 0
    start_quote = source.find('"', start_link)
    end_quote = source.find('"', start_quote + 1)
    url = source[start_quote + 1 : end_quote]
    return url, end_quote

# print get_next_target("sample_source.html")


def get_all_links(source):
	links = []
	f = open_file(source)
	while True:
		url, endpos = get_next_target(f)
		if url:
			links.append(url)
			f = source[endpos:]
		else:
			break
	return links


print get_all_links("sample_source.html")
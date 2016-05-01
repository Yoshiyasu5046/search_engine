# This search engine takes the source source url as input and return the urls in the source source as an array.
from os import getcwd 

#print getcwd()

def open_file(source):
	source = "Users/Yoshiyasu/Documents/coding/Udacity/Search_engine/sample_source.html"
	file = open(source, "r") 
	output = file.read()
	output.close()
	return

def get_next_target(source):
    source = open_file(source)
    start_link = source.find('href=')
    if start_link == -1:
        return None, 0
    start_quote = source.find('"', start_link)
    end_quote = source.find('"', start_quote + 1)
    url = source[start_quote + 1 : end_quote]
    return url, end_quote
    
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(source):
    links = []
    while True:
        url, endpos = get_next_target(source)
        if url:
            links.append(url)
            source = source[endpos:]
        else:
            break
    return links
    
def crawl_web(source):
    tocrawl = [source]
    crawled = []
    url = ""
    while tocrawl:
        source = tocrawl.pop()
        if url not in crawled:
            union(tocrawl, get_all_links(source))
            crawled.append(url)
    return crawled

print crawl_web("sample_source.html")

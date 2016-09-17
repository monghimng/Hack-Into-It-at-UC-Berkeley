import urllib.request as web
link = "http://api.census.gov/data/2010/sf1?key=4dbe021cda8a6bb5a803fe065758760671f13e3f&get=P0010001,NAME&for=state:41"
f = web.urlopen(link)
print(f.read())

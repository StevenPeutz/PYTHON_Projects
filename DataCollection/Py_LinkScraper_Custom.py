import urllib.request, urllib.parse, urllib.error
source_url = input('Type the URL you want to scrape (including http or https) and hit enter : ')
page_in_bytes = urllib.request.urlopen(source_url).read()
page = page_in_bytes.decode('utf8')



#i = 0
def getNextUrl(page):
    startLink = page.find('<a href=')
    if startLink == -1:
        #print('no href found..', 0)
        return None, 0
    startQuote = page.find('"', startLink)
    endQuote = page.find('"', startQuote + 1)
    url = page[startQuote + 1 : endQuote]
    return url, endQuote
#print(getNextUrl(page))

def print_all_links(page):
    while True:
        url, endpos = getNextUrl(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

print(print_all_links(page))
#print(print_all_links(urllib.request.urlopen('http://stevenpeutz.info').read()))

import requests
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urljoin

# I had to <pip3 install lxml> to get this to work
def getLinks(url, pattern):
    """From the page of <genre> movies, make a list of URLS for each movie page
    credit: https://pythonspot.com/extract-links-from-webpage-beautifulsoup/"""
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, features="lxml")
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile(pattern)}):
        links.append(link.get('href'))

    return links

def getMoviePages():
    """Edit the getMovies list of URLS to be in a form we can "click" on"""
    genreURL = "https://imsdb.com/genre/Sci-Fi"   # <===== change this to scrape different genres
    pattern = "^/Movie Scripts/"
    moviepages = []
    for i, url in enumerate(getLinks(genreURL, pattern)):
        url = re.sub(" ", "%20", url)
        moviepages.append(urljoin(genreURL, url))

    return moviepages


def getScriptLinks():
    """Gets the link to all existing movie scripts passed in by getMoviePages()
    Takes hella long to run"""
    pattern = "/scripts/"
    script_links = []
    moviepages = getMoviePages()
    for i in range(len(moviepages)):
        script_links.append(getLinks(moviepages[i], pattern))

    script_links = [x for x in script_links if x != [] and x != ['/scripts/.', '/scripts/.']]

    rootURL = 'https://imsdb.com'
    for i in range(len(script_links)):
        script_links[i] = urljoin(rootURL, script_links[i][0])

    return script_links


def getScripts(scripts):
    """Put all the scripts into a list
    Getting this error: RecursionError: maximum recursion depth exceeded
    help??"""
    all_scripts = []
    for i in range(len(scripts)):
        URL = scripts[i]
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        script = soup.find('pre')

        all_scripts.append(script)

    for i, play in enumerate(all_scripts):
        if play is None:
            all_scripts.pop(i)
        else:
            all_scripts[i] = (play.text.strip())

    return all_scripts

print(getScripts(getScriptLinks()))

# installed beautifulsoup4 & requests
import grequests  # use grequests instead of request for multiple pages
from bs4 import BeautifulSoup
import pprint  # pretty print

"""Scrape 2 pages of hacker news"""

urls = ['https://news.ycombinator.com/news?p=1', 'https://news.ycombinator.com/news?p=2']
unsent_request = (grequests.get(url) for url in urls)
response = grequests.map(unsent_request)

# iterate over the pages in response
links, subtext = [], []
for res in response:
    soup = BeautifulSoup(res.text, 'html.parser')
    links += soup.select('.storylink')
    subtext += soup.select('.subtext')


def sort_by_votes(hn):
    return sorted(hn, key=lambda k: k['points'], reverse=1)


def sort_by_age(hn):
    return sorted(hn, key=lambda k: k['hours'])


def create_custom_hackernews(links, subtext):
    hn = []
    for idx, item in enumerate(links):

        title = links[idx].getText()  # could replace links[idx] with item
        href = links[idx].get('href', None)  # None is default in case no link
        vote = subtext[idx].select('.score')
        hours = subtext[idx].select('.age')[0].getText().replace(' hours ago', '')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))  # remember vote is a [] with 1 element
            if points > 100:
                hn.append({'idx': idx, 'title': title, 'link': href, 'points': points, 'hours': hours})  # use dict
            # print({'idx': idx, 'title': title, 'link': href, 'points': points})
    return hn


hnlist = (create_custom_hackernews(links, subtext))
print(f'{len(hnlist)} stories found with votes >100. Printing in order of upvotes first:')
pprint.pprint(sort_by_votes(hnlist))


# installed beautifulsoup4 & requests
import requests
from bs4 import BeautifulSoup
import pprint  #pretty print

res = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all('div'))  # div, a are elements
links = soup.select('.storylink')
subtext = (soup.select('.subtext'))  # select the class subtext (dot is a class)
# print(votes[0].get('id')) #can use get to get the next level down eg id


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


hn = create_custom_hackernews(links, subtext)
print(f'{len(hn)} stories found with votes >100. Printing in order of upvotes first:')
pprint.pprint(sort_by_votes(hn))


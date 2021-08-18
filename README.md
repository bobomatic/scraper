# scraper
Python code that scrapes a news website and puts the stories into a dictionary for display

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Examples of Use](#examples-of-use)
* [Status](#status)
* [Sources](#sources)

## General Info
This project is a demonstration of web scraping using beautiful soup. The module could be adapted to provide a newsfeed on a website.

## Technologies
This project is created with

Python 3.8

Beautifulsoup4

grequests - asynchronous http requests

## Setup
To run this project install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

## Features
* scrape pages of hackernews website https://news.ycombinator.com/news
* add to dictionary (title, links, votes, hours old)
* sort by votes and display (pprint) stories with votes>100 in terminal

### To do:
* Use this module for a website newsfeed or weekly email update

## Examples of Use

Usage: 

scrape.py

Stories from page 1 with >100 votes are displayed in the terminal

scrape2.py

Stories from page 1&2 with >100 votes are displayed in the terminal

If the functions are imported (import scrape_2) then scrape(urls) will provide a list of link and subtext tags 
(where urls is a list of urls). A custom function such as create_custom_hackernews can then be used to extract the news stories, links etc into a dictionary for display.

Code example:

Command line
`$ python3 scrape2.py`

Import module
`import scrape2
links, subtext = scrape(urls)`

## Status
Basic scraping functionality is complete.
Further development will be required to integrate with a website

## Sources
This project is inspired by Andrei Neagoie Python Zero to Mastery course:

https://www.udemy.com/course/complete-python-developer-zero-to-mastery

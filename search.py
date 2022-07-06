import urllib.request
import urllib.parse
import argparse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = 'http://export.arxiv.org/api/query?search_query='
PREFIX = {'Title': 'ti',
          'Author': 'au',
          'Abstract': 'abs',
          'Comment': 'co',
          'Journal Reference': 'jr',
          'Subject Category': 'cat',
          'Report Number': 'rn',
          'ID': 'id',
          'All': 'all'}

# input_keywords = input('Please enter the keywords or search phrases separated by commas: ')
input_keywords = 'reinforcement learning'


def make_query(url=BASE_URL, prefix=PREFIX['All'], keywords=input_keywords):
    keywords = urllib.parse.quote(keywords)
    print(keywords)
    url = f'{url}{prefix}:"{keywords}"'
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            soup = BeautifulSoup(response, 'xml')
        else:
            print('Please, check the correctness of the request')
    cols = ['id', 'updated', 'title', 'summary', 'author', 'link']
    articles = pd.DataFrame(columns=cols)
    # articles = articles.set_index('id')

    for tag in soup.find_all('entry'):
        # row_to_concat = pd.DataFrame({'id': [0],
        #                               'updated': tag.updated,
        #                               'title': tag.title,
        #                               'summary': tag.summary,
        #                               'author': [n.string for n in tag.find_all('name')],
        #                               'link': tag.find(title='pdf').get('href')})
        # articles = pd.concat([articles, row_to_concat])
        print([n.string for n in tag.find_all('name')])


    # print(articles.head())
    # print(articles.describe())


def main():
    make_query()


if __name__ == '__main__':
    main()

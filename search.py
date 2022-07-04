import urllib.request
import urllib.parse
import argparse
import xml.etree.ElementTree as ET


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

input_keywords = input('Please enter the keywords or search phrases separated by commas: ')


def make_query(url=BASE_URL, prefix=PREFIX['All'], keywords=input_keywords):
    keywords = urllib.parse.quote(keywords)
    print(keywords)
    url = f'{url}{prefix}:"{keywords}"'
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            tree = ET.parse(response)
            root = tree.getroot()
        else:
            print('Please, check the correctness of the request')

    articles = []
    for entry in root.findall('entry'):
        title = entry.find('title').text
        articles.append(title)
    print(articles)


def main():
    make_query()


if __name__ == '__main__':
    main()

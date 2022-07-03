import urllib.request
import urllib.parse
import argparse


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
    url = f'{BASE_URL}{prefix}:"{keywords}"'
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            r = response.read()
            print(r)
        else:
            print('Please, check the correctness of the request')


def main():
    make_query()


if __name__ == '__main__':
    main()

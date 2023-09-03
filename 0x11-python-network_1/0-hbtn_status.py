#!usr/bin/python3
''' fetches https://intranet.hbtn.io/status. '''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        site = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(site)))
        print('\t- content: {}'.format(site))
        print('\t- utf8 content: {}'.format(site.decode('utf-8')))

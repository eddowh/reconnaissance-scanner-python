#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from io import TextIOWrapper


def get_robots_txt(url):
    """
    TODO
    """

    # if no backslash, append to URL
    path = url + (
        "" if url.endswith('/')
        else "/"
    )
    path += "robots.txt"

    try:
        req = urlopen(path)
    except Exception, err:
        print err
        return
    else:
        data = TextIOWrapper(req, encoding='utf-8')
        return data.read()

def main():
    print get_robots_txt('https://www.reddit.com')


if __name__ == '__main__':
    main()

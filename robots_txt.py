#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import io


def get_robots_txt(url):
    """
    Accepts URL as an argument,
    and outputs the robots.txt file.
    """

    # if no backslash, append to URL
    path = url + (
        "" if url.endswith('/')
        else "/"
    )

    # request the robots.txt file from internet
    req = urllib.request.urlopen(
        path + 'robots.txt',
        data=None
    )

    data = io.TextIOWrapper(req, encoding='utf-8')

    return data.read()


def main():
    print get_robots_txt('https://www.reddit.com')


if __name__ == '__main__':
    main()

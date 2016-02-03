#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2


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
        req = urllib2.urlopen(path, data=None)
    except Exception, err:
        print "ERROR: %s" % err
        return
    else:
        data = req.read()
        return data


def main():
    print get_robots_txt('https://www.google.com/')


if __name__ == '__main__':
    main()

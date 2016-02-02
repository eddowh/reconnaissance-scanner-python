#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def get_whois(url_tld):
    """TODO"""

    command = "whois %s" % url_tld
    process = os.popen(command)

    results = str(process.read())

    return results


def main():
    print get_whois('facebook.com')


if __name__ == '__main__':
    main()
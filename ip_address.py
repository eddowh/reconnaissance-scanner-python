#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def get_ip_address(url):
    """
    TODO
    """
    command = "host %s" % url
    process = os.popen(command)
    results = str(process.read())

    # move 12 characters ahead of phrase 'has address'
    # to get to the beginning of the ip address
    marker = results.find('has address') + 12

    return results[marker:].splitlines()[0]


def main():
    print get_ip_address('google.com')


if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def get_nmap(options, ip):
    """
    TODO
    """
    command = "nmap %s %s" % (options, ip)
    process = os.popen(command)

    results = str(process.read())

    return results


def main():
    print get_nmap('-F', '54.186.250.79')

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2


def get_robots_txt(url):
    """
    TODO
    """

    # if no backslash, append to URL
    url = url + (
        "" if url.endswith('/')
        else "/"
    )
    robots_txt_path = url + "robots.txt"

    try:
        req = urllib2.urlopen(robots_txt_path, data=None)
    except Exception, err:
        print "ERROR: %s" % err
        return
    else:
        data = req.read()
        return data


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
    
    
def get_nmap(options, ip):
    """
    TODO
    """
    command = "nmap %s %s" % (options, ip)
    process = os.popen(command)

    results = str(process.read())

    return results
    
   
def get_whois(url_tld):
    """TODO"""

    command = "whois %s" % url_tld
    process = os.popen(command)

    results = str(process.read())

    return results

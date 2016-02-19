#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tld import get_tld

from filesystem import *
from helpers import *


ROOT_DIR = 'companies'


def main():
    create_dir(ROOT_DIR)
    gather_info('baidu', 'http://www.baidu.com/')
    gather_info('hacker-news', 'https://news.ycombinator.com/')


def gather_info(name, url):
    robots_txt = get_robots_txt(url)

    # if robots_txt returns None, it can mean quite a few things
    # i.e. requesting the robots.txt file from reddit in Indonesia
    # is not possible because of CertificateError - simply put,
    # Reddit is blocked in Indonesia
    if not robots_txt:
        return

    domain_name = get_tld(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    whois = get_whois(domain_name)

    create_report(
        name,
        url,
        domain_name,
        nmap,
        robots_txt,
        whois
    )


def create_report(name, url, domain_name, nmap, robots_txt, whois):

    project_dir = "%s/%s" % (ROOT_DIR, name)
    create_dir(project_dir)

    write_file(project_dir + "/" + "nmap.txt", nmap)
    write_file(project_dir + "/" + "robots.txt", robots_txt)
    write_file(project_dir + "/" + "whois.txt", whois)


if __name__ == '__main__':
    main()

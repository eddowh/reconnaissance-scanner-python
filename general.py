#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def create_dir(directory):
    """
    Create a folder if not created yet.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    """
    Write content into file.
    """
    f = open(path, 'w')
    f.write(data)
    f.close()

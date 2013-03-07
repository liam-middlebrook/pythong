#!/bin/env python
# -*- coding: utf8 -*-
"""
Contains utility functions used by pythong, including
command parsing.
"""

from pythong.project import Project

import argparse


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("name")
    args = p.parse_args()
    new_project = Project(args.name)


def ask_yes_no(message, default=None):
    """ Prompt the user for a boolean response.
        Thanks to this useful recipe for help:
            http://code.activestate.com/recipes/577058/
    """
    valid = {"yes": True,
             "y": True,
             "ye": True,
             "no": False,
             "n": False}
    if default:
        prompt = " [Y/n] "
        valid[''] = True
    else:
        prompt = " [y/N] "
        valid[''] = False

    while True:
        print message + prompt,
        choice = raw_input().lower()
        if choice in valid:
            return valid[choice]
        print "Please respond with 'yes', 'no', 'y', or 'n'."

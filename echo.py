#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "https://kenzie.zoom.us/rec/play/6MAud7qgrm83HYLHsASDU6MvW43pfKys1nce-_Bbzx6zViMENVWlYrITYWSpqDbUA7gs9q-oF-SYuEc?startTime=1592939798000&_x_zm_rtaid=hh-8qZ6URJ6kZxHdEHgOmw.1594945598504.822f51a13bf0678dbe045089783611ce&_x_zm_rhtaid=865"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', help="text to be manipulated")
    parser.add_argument('-u', '--upper', action="store_true", help="convert text to uppercase")
    parser.add_argument('-l', '--lower', action="store_true", help="convert text to lowercase")
    parser.add_argument('-t', '--title', action="store_true", help="convert text to titlecase")

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)
    
    msg = args.text
    if args.upper:
        msg = msg.upper()
    if args.lower:
        msg = msg.lower()
    if args.title:
        msg = msg.title()    
        
    print(msg)
    return


if __name__ == '__main__':
    main(sys.argv[1:])

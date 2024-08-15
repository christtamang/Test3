#!/usr/bin/env python3

def test_test3():

    import os, sys

    if not os.path.exists("users.csv"):

        sys.exit("users.csv does not exist. Either test3.py hasn't been run OR it does not create the file users.csv.")

test_test3()
#!/usr/bin/env python3
# Author: Christ Tamang, st9849601@gmailcom
# Date: 2024/08/15
# Purpose: Import the write_csv and read_csv functions from lib. Call each function.
# Usage: ./test3.py
# 

from lib import write_csv, read_csv

# Call the write_csv function, passing it the arguments "names.dat", "emails.dat", and "users.csv"
write_csv("names.dat", "emails.dat", "users.csv")

# Call the read_csv function, passing it the argument "users.csv"
read_csv("users.csv")

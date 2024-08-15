#!/usr/bin/env python3
# Author: Christ Tamang, st9849601@gmailcom
# Date: 2024/08/15
# Purpose: Function library for Test 3.

import os
import sys

def write_csv(namesFile, emailsFile, usersFile):
    # Check if the namesFile doesn't exist
    if not os.path.exists(namesFile):
        # Exit the program with an error message
        sys.exit(f"Error: {namesFile} does not exist.")
    
    # Check if the emailsFile doesn't exist
    if not os.path.exists(emailsFile):
        # Exit the program with an error message
        sys.exit(f"Error: {emailsFile} does not exist.")
    
    # Check if the usersFile doesn't exist
    if not os.path.exists(usersFile):
        # Create the usersFile
        with open(usersFile, 'w') as _:
            pass

    # Open the namesFile with read permission as namesData
    with open(namesFile, 'r') as namesData:
        # Read the lines of the namesData file and store them in the list names
        names = namesData.readlines()

    # Open the emailsFile with read permission as emailsData
    with open(emailsFile, 'r') as emailsData:
        # Read the lines of the emailsData file and store them in the list emails
        emails = emailsData.readlines()

    # Open the usersFile with append permission as file
    with open(usersFile, "a") as file:
        # Loop through the range of the length of the names list
        for each in range(len(names)):
            # Write the names and emails to the file
            file.write(names[each].strip() + "," + emails[each].strip() + "\n")

    # Close the namesData file
    namesData.close()

    # Close the emailsData file
    emailsData.close()

    # Close the file
    file.close()

def read_csv(usersFile):
    # Open the file with read permission. Store it in the variable users.
    with open(usersFile, 'r') as users:
        # Print the header
        print(f"{'Name':10}\t{'Email'}")

        # Use a for loop to loop through the lines in the users file
        for data in users:
            # Split the data by comma
            data = data.strip().split(',')

            # Print the data with a fixed field width of 10 for the name (data 0) and no fixed field width for the email (data 1). Separate the name and email with a tab.
            print(f"{data[0]:10}\t{data[1]}")

    # Close the file
    users.close()
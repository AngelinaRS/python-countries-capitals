"""Countries-Capitals"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def reset():
    """This cleans the screen"""
    if os.name == ("posix"): #In Linux
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"): #In windows
        os.system("cls")
reset()

def is_alpha(country_or_capital):
    """This verifies if has letters"""
    if country_or_capital.isalpha() == True:
        return True
    else:
        return False

def is_title(country_or_capital):
    """This converts in format title"""
    country_or_capital = country_or_capital.title()
    return country_or_capital

def minuscule(choose_user):
    """This converts the choose user in minuscule"""
    choose_user = choose_user.lower()
    return choose_user

def message():
    """This shows a message"""
    print "**Insert a valid name**"

def insert_country():
    """This saves the country"""
    reset()
    enter_country = False
    while enter_country == False:
        country = raw_input("Insert the country: ")
        country_title = is_title(country)
        enter_country = is_alpha(country)
        if enter_country == False: #If the country is not an alphabetical value
            message()
    return country_title


def menu_print():
    """This shows the options that has the menu"""

    print "----------------------------------------------------------------------"
    print "|                          Choose an option                          |"
    print "|1. Country      *To insert a country and capipal                    |"
    print "|2. Countries    *To see the countries                               |"
    print "|3. Capitals     *To see the capitals                                |"
    print "|4. All          *To see countries with their capitals               |"
    print "|5. AllOrdered   *To see the countries and capitals                  |"
    print "|                 ordered by capital                                 |"
    print "|6. AllMail      *To send by Email                                   |"
    print "|7. Exit                                                             |"
    print "----------------------------------------------------------------------"

def menu_option():
    """This saves the election of the user"""
    while True:

        choose_user = raw_input(" - ")
        choose_user = minuscule(choose_user)

        if choose_user == "7":
            reset()
            sys.exit()
        else:
            reset()
            print "**Choose a valid option**"
            menu()

def menu():
    """This saves the menu"""
    menu_print()
    menu_option()

if __name__ == '__main__':
    menu()

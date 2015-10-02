"""Countries-Capitals"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

COUNTRIES_CAPITALS = {}

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

def press_enter():
    """This asks to the user that press enter"""
    raw_input("Press -Enter-")

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

def insert_capital():
    """This saves the capital"""
    enter_capital = False
    while enter_capital == False:
        capital = raw_input("Insert the capital: ")
        capital_title = is_title(capital)
        enter_capital = is_alpha(capital)
        if enter_capital == False: #If the capital is not an alphabetical value
            message()
    return capital_title

def add_cc(country, capital):
    """This saves the country and capital in a dictionary"""
    COUNTRIES_CAPITALS[country] = capital

def insert_country_and_capital():
    """This adds the countries and capitals in a dictionary"""

    country = insert_country()
    capital = insert_capital()
    add_cc(country, capital)

    #If the user wants to insert another article
    while True:
        choose_user = raw_input("Do you want to insert another country and capital? y/n  ")
        another = minuscule(choose_user)
        if another == "y":
            country = insert_country()
            capital = insert_capital()
            add_cc(country, capital)
        elif another == "n":
            reset()
            menu()
        else:
            print "Only can write -y- or -n-  "
    return another

def show_countries():
    """This shows the list of the countries"""
    reset()
    print "-" * 70
    print "*These are the countries*\n".center(70, " ")

    #This iterarates in the keys of the dictionary
    for key in COUNTRIES_CAPITALS.keys():
        print key.center(70, " ") #This centers the list of the countries
    print "\n" + "-" * 70

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

        if choose_user == "1" or choose_user == "country":
            reset()
            insert_country_and_capital()

        elif choose_user == "2" or choose_user == "countries":
            reset()
            show_countries()
            press_enter()
            reset()
            menu()

        elif choose_user == "7":
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

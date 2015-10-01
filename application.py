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



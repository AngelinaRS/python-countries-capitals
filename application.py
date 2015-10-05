"""Countries-Capitals"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import smtplib
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


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
    raw_input("\n\nPress -Enter-  ")
    reset()
    menu()

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
        choose_user = raw_input("\nDo you want to insert another country and capital? y/n  ")
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

def show_capitals():
    """This shows the list of the capitals"""
    reset()
    print "-" * 70
    print "*These are the capitals*\n".center(70, " ")

    #This iterarates in the values of the dictionary
    for value in COUNTRIES_CAPITALS.values():
        print value.center(70, " ") #This centers the list of the capitals
    print "\n" + "-" * 70

def show_all():
    """This shows the countries with their capitals"""
    reset()
    print "-" * 50
    print "*These are the countries and capitals*\n".center(50, " ")

    for key in COUNTRIES_CAPITALS:
        print "{k:^25s}{v}".format(k=key, v=COUNTRIES_CAPITALS[key])
    print "\n" + "-" * 50

def show_all_ordered():
    """This shows the countries and capitals ordered"""
    reset()
    print "-"*50
    print "These are the countries and capitals".center(50, " ")
    print "Ordered\n".center(50, " ")

                    #This sorts the Contries                 This sorts the capitals
    for key, value in sorted(COUNTRIES_CAPITALS.iteritems(), key=lambda (k, v): (v, k)):
        print "{country:^25s}{capital}".format(country=key, capital=value)
    print "\n" + "-" * 50

def send_mail():
    """This sends the list of countries and capital to lgarcia@cognits.co"""

    print "Remember, the list of countries and capitals"
    print "will be sent to the same email that You insert\n"

    fromaddr = raw_input("Insert your email:  ")  #The username
    password = getpass.getpass("Password: ")  #Not showing the password
    toaddrs =  fromaddr
    body = ""

    for country, capital in COUNTRIES_CAPITALS.iteritems():
        body = body + country + "-" + capital + "\n"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Subject'] = "Countres and Capitals"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "\n\nEmail Sent"
    except:
        reset()
        print "Error! Invalid username or password\n"
        send_mail()

def valid_menu(choose_user):
    """This verifies if the dictionary is empty"""
    reset()
    if COUNTRIES_CAPITALS == {} and (choose_user == "2" or choose_user == "countries" \
        or choose_user == "3" or choose_user == "capitals" \
        or choose_user == "4" or choose_user == "all" \
        or choose_user == "5" or choose_user == "allordered" \
        or choose_user == "6" or choose_user == "allmail"):
        return True

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

        if valid_menu(choose_user) == True:
            print "\n There are not lists to show\n"
            press_enter()
        else:
            if choose_user == "1" or choose_user == "country":
                reset()
                insert_country_and_capital()

            elif choose_user == "2" or choose_user == "countries":
                reset()
                show_countries()
                press_enter()

            elif choose_user == "3" or choose_user == "capitals":
                reset()
                show_capitals()
                press_enter()

            elif choose_user == "4" or choose_user == "all":
                reset()
                show_all()
                press_enter()

            elif choose_user == "5" or choose_user == "allordered":
                reset()
                show_all_ordered()
                press_enter()

            elif choose_user == "6" or choose_user == "allmail":
                reset()
                send_mail()
                press_enter()

            elif choose_user == "7" or choose_user == "exit":
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

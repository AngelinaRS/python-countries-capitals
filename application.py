"""Countries-Capitals"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import smtplib
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class CountriesAndCapitals(object):
    """Save countries and capitals"""

    def __init__(self):
        self.countries_capitals = {}

    def reset(self):
        """This cleans the screen"""
        if os.name == ("posix"): #In Linux
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"): #In windows
            os.system("cls")

    def is_alpha(self, country_or_capital):
        """This verifies if has letters"""
        try:
            country_or_capital = country_or_capital.decode("utf-8")
            #If in the word there is a space but is not empty
            if country_or_capital.isalpha() == True or " " in country_or_capital \
            and country_or_capital.isspace() == False:
                return True
            else:
                return False
        except:
            return False

    def is_title(self, country_or_capital):
        """This converts in format title"""
        decode = country_or_capital.decode("utf-8") #This allows special characters
        title = decode.title()
        text = title.encode("utf-8") #This converts in format title the special characters
        return text

    def minuscule(self, choose_user):
        """This converts the choose user in minuscule"""
        choose_user = choose_user.lower()
        return choose_user

    def message(self):
        """This shows a message"""
        print "**Insert a valid name**"

    def press_enter(self):
        """This asks to the user that press enter"""
        raw_input("\n\nPress -Enter-  ")
        self.reset()
        self.menu()

    def insert_country(self):
        """This saves the country"""
        self.reset()
        enter_country = False
        while enter_country == False:
            country = raw_input("Insert the country: ")
            country_title = self.is_title(country)
            enter_country = self.is_alpha(country)
            if enter_country == False: #If the country is not an alphabetical value
                self.message()
        return country_title

    def insert_capital(self):
        """This saves the capital"""
        enter_capital = False
        while enter_capital == False:
            capital = raw_input("Insert the capital: ")
            capital_title = self.is_title(capital)
            enter_capital = self.is_alpha(capital)
            if enter_capital == False: #If the capital is not an alphabetical value
                self.message()
        return capital_title

    def add_cc(self, country, capital):
        """This saves the country and capital in a dictionary"""
        self.countries_capitals[country] = capital

    def insert_country_and_capital(self):
        """This adds the countries and capitals in a dictionary"""

        country = self.insert_country()
        capital = self.insert_capital()
        self.add_cc(country, capital)

        #If the user wants to insert another article
        while True:
            choose_user = raw_input("\nDo you want to insert another country and capital? y/n  ")
            another = self.minuscule(choose_user)
            if another == "y":
                country = self.insert_country()
                capital = self.insert_capital()
                self.add_cc(country, capital)
            elif another == "n":
                self.reset()
                self.menu()
            else:
                print "Only can write -y- or -n-  "
        return another

    def show_countries(self):
        """This shows the list of the countries"""
        self.reset()
        print "-" * 70
        print "*These are the countries*\n".center(70, " ")

        #This iterarates in the keys of the dictionary
        for key in self.countries_capitals.keys():
            print key.center(70, " ") #This centers the list of the countries
        print "\n" + "-" * 70

    def show_capitals(self):
        """This shows the list of the capitals"""
        self.reset()
        print "-" * 70
        print "*These are the capitals*\n".center(70, " ")

        #This iterarates in the values of the dictionary
        for value in self.countries_capitals.values():
            print value.center(70, " ") #This centers the list of the capitals
        print "\n" + "-" * 70

    def show_all(self):
        """This shows the countries with their capitals"""
        self.reset()
        print "-" * 50
        print "*These are the countries and capitals*\n".center(50, " ")
        print "Country".center(24, "*"), "Capital".center(24, "*") + "\n"

        for key in self.countries_capitals:
            print key.center(24, " "), self.countries_capitals[key].center(24, " ")
        print "\n" + "-" * 50

    def show_all_ordered(self):
        """This shows the countries and capitals ordered"""
        self.reset()
        print "-"*50
        print "These are the countries and capitals".center(50, " ")
        print "Ordered\n".center(50, " ")
        print "Country".center(24, "*"), "Capital".center(24, "*") + "\n"

                        #This sorts the Contries                 This sorts the capitals
        for key, value in sorted(self.countries_capitals.iteritems(), key=lambda (k, v): (v, k)):
            print key.center(24, " "), value.center(24, " ")
        print "\n" + "-" * 50

    def send_mail(self):
        """This sends the list of countries and capital to lgarcia@cognits.co"""

        print "Remember, the list of countries and capitals"
        print "will be sent to the same email that You insert\n"

        fromaddr = raw_input("Insert your email:  ")  #The username
        password = getpass.getpass("Password: ")  #Not showing the password
        toaddrs = fromaddr
        body = ""
        #This adds to the message the countries and capitals
        for country, capital in self.countries_capitals.iteritems():
            body = body + country + "-" + capital + "\n"

        msg = MIMEMultipart()
        msg['From'] = fromaddr #This saves the mail of the sender
        msg['To'] = toaddrs  #This saves the mail of the receiver
        msg['Subject'] = "Countres and Capitals"  #This saves the subject
        msg.attach(MIMEText(body, 'plain')) #This saves the message

        try:
            #This verifies if the data are valid to send the mail
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(fromaddr, password)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print "\n\nEmail Sent"
        except:
            #This asks again the mail and password if the data are invalid
            self.reset()
            print "Error! Invalid username or password\n"
            self.send_mail()

    def valid_menu(self, choose_user):
        """This verifies if the dictionary is empty"""
        self.reset()
        if self.countries_capitals == {} and (choose_user == "2" or choose_user == "countries" \
            or choose_user == "3" or choose_user == "capitals" \
            or choose_user == "4" or choose_user == "all" \
            or choose_user == "5" or choose_user == "allordered" \
            or choose_user == "6" or choose_user == "allmail"):
            return True

    def menu_print(self):
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

    def menu_option(self):
        """This saves the election of the user"""
        while True:

            choose_user = raw_input(" - ")
            choose_user = self.minuscule(choose_user)

            if self.valid_menu(choose_user) == True:
                print "\n There are not lists to show\n"
                self.press_enter()
            else:
                if choose_user == "1" or choose_user == "country":
                    self.reset()
                    self.insert_country_and_capital()

                elif choose_user == "2" or choose_user == "countries":
                    self.reset()
                    self.show_countries()
                    self.press_enter()

                elif choose_user == "3" or choose_user == "capitals":
                    self.reset()
                    self.show_capitals()
                    self.press_enter()

                elif choose_user == "4" or choose_user == "all":
                    self.reset()
                    self.show_all()
                    self.press_enter()

                elif choose_user == "5" or choose_user == "allordered":
                    self.reset()
                    self.show_all_ordered()
                    self.press_enter()

                elif choose_user == "6" or choose_user == "allmail":
                    self.reset()
                    self.send_mail()
                    self.press_enter()

                elif choose_user == "7" or choose_user == "exit":
                    self.reset()
                    sys.exit()

                else:
                    self.reset()
                    print "**Choose a valid option**"
                    self.menu()

    def menu(self):
        """This saves the menu"""
        self.menu_print()
        self.menu_option()

MAIN = CountriesAndCapitals()

if __name__ == '__main__':
    MAIN.menu()

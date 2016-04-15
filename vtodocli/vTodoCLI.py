#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Tuesday, April 5th 2016, 5:47:03 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Friday, April 15th 2016, 3:36:45 am
import os
import sys
import curses
import bcrypt
import getpass
from curses import wrapper
from vtodocli import models
from colored import fg, bg, attr

class VtodoCLI:
    def __init__(self,argp):
        self.argparser = argp
        self.stdscr = None
        self.username = ""
        self.passwd = None
        self.vmodels = models.VTodoModel()

    """
    Prompts the user to login
    Will hash password as the web app does
    """
    def login(self):
        self.welcome_header()
        self.username = raw_input("Username >> ")
        dbdata = self.vmodels.get_user(self.username)
        passwdhash = dbdata[0][3]
        passwd = getpass.getpass("Password >> ")
        if (bcrypt.hashpw(passwd,passwdhash) == passwdhash):
            print "Successful Login!"
        else:
            sys.exit("Invalid credentials")


    """
    ASCII art for user
    Uses same color as navbar in web app(arch blue :D)
    """
    def welcome_header(self):
        color = fg(25)
        sfx = attr(1)
        res = attr(0)
        print """{} {}
               ______          __         ________    ____
         _   _/_  __/___  ____/ /___     / ____/ /   /  _/
        | | / // / / __ \/ __  / __ \   / /   / /    / /
        | |/ // / / /_/ / /_/ / /_/ /  / /___/ /____/ /
        |___//_/  \____/\__,_/\____/   \____/_____/___/
        {}""".format(color,sfx,res)
        sys.stdout.flush()


    ##############################################
    # Everything below this is related to curses #
    ##############################################
    """
    Initialize curses
    """
    def initCurses(self):
        # self.logger.logInfo("Initializing Curses")
        wrapper(self.handleCurses)

    """
    Handles curses after initializing
    """
    def handleCurses(self,stdscr):
        self.stdscr = stdscr
        sys.stdout.flush()

        curses.curs_set(0)
        curses.cbreak()
        curses.echo()
        curses.start_color()
        curses.use_default_colors()

        while True:
            self.cursesMenu()
            status = self.getKeystroke()
            if status == "submit":
                break
            if status == "end":
                sys.exit("User has exited ncurses")
                break
            else:
                continue
        curses.endwin()

    """
    Formats a menu onto the terminal screen
    """
    def cursesMenu(self):
        self.stdscr.clear()
        self.stdscr.border(0)
        self.stdscr.addstr(2, 2, "vTodo CLI")
        self.stdscr.addstr(4, 4, "1 - List Tasks")
        self.stdscr.addstr(5, 4, "2 - Add a Task")
        self.stdscr.addstr(6, 4, "3 - Delete a Task")
        self.stdscr.addstr(7, 4, "4 - Exit")
        self.stdscr.refresh()

    """
    Read a single keystroke from user untill it is a valid menu option
    """
    def getKeystroke(self):
        useropt = self.stdscr.getch()

        if useropt == ord('1'):
            results = self.vmodels.queryDB(1, self.username)
            self.listTasks(results)
        elif useropt == ord('2'):
            tasktitle = self.getConfig("Enter Task Title, press [Enter] for none")
            taskbody = self.getConfig("Enter Task Body, must be at least 3 characters")
            
            return "submit"

    """
    List all tasks
    A bit ugly, but formats using color nicely
    """
    def listTasks(self,results):
        self.stdscr.clear()
        self.stdscr.addstr(0,6,"All of {}\'s Tasks".format(self.username), curses.color_pair(1))
        curses.init_pair(1,25,curses.COLOR_BLACK-1)
        i = 1
        for elem in results:
            # Title
            self.stdscr.addstr(i,1,"Title: ",curses.color_pair(1))
            self.stdscr.refresh()
            y,x = curses.getsyx() # Colorize label only
            self.stdscr.addstr(i,x,"{}".format(elem[2]))

            # Date Due
            self.stdscr.addstr(i+1,1,"Date Due: ",curses.color_pair(1))
            self.stdscr.refresh()
            y,x = curses.getsyx() # Colorize label only
            self.stdscr.addstr(i+1,x,"{}".format(elem[3]))
            self.stdscr.refresh()
            y,x = curses.getsyx() # Colorize label only

            # Time Due
            self.stdscr.addstr(i+1,x," Time Due: ",curses.color_pair(1))
            self.stdscr.refresh()
            y,x = curses.getsyx() # Colorize label only
            self.stdscr.addstr(i+1,x,"{}".format(elem[4]))

            # Task Body
            body = elem[5].replace('\n', '').replace('\r', '')

            self.stdscr.addstr(i+2,1,"Task: ",curses.color_pair(1))
            self.stdscr.refresh()
            y,x = curses.getsyx()
            self.stdscr.addstr(i+2,x,"{}".format(body))

            self.stdscr.refresh()
            y,x = curses.getsyx()
            i = y + 2

        self.stdscr.getch()

    """
    Reads a config value & returns it
    """
    def getConfig(self,msg):
        self.stdscr.clear()
        self.stdscr.addstr(2,2,msg)
        self.stdscr.refresh()
        userval = self.stdscr.getstr(4,4,120)
        return userval

def main():
    run = VtodoCLI(1)
    run.login()
    run.initCurses()
if __name__ == "__main__":
    main()

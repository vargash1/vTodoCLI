#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Tuesday, April 5th 2016, 5:47:03 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 5th 2016, 11:28:48 am
import textwrap
import sys
class VtodoParse:

    def __init__(self):
        self.OPTIONS = {
            'ls'  : False,
            'add' : False,
            'rm'  : False
        }

    """
    Parses arguments read
    Then calls appropriate method
    """
    def parseArgs(self,tmpargs):
        if len(tmpargs) >= 2:
            args = tmpargs[1]
            if args in self.OPTIONS:
                self.OPTIONS[args] = True
                return self.OPTIONS
            else:
                self.usage("Invalid Arguments Passed")
        else:
            self.usage()

    """
    Prints usage and exits with code 1
    """
    def usage(self,msg=""):
        textwrap.dedent("""
        Description:
            This program is part of vTodo that will allow the user to interact with
            their tasks via CLI.
        Usage:
            Pass arguments to the program as shown below.

            arithcli [OPTION] [TASK]

        OPTION:
            add
                Adds a task and stores it in the database
            ls
                Lists tasks that belong to the user
            rm
                Removes a task that belongs to the user
        """)
        sys.exit(msg)

def main():
    test = vtodoParse()
    test.parseArgs()

if __name__ == "__main__":
    main()

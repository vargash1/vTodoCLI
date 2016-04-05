#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Tuesday, April 5th 2016, 5:47:03 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 5th 2016, 11:36:45 am
import sys

class VtodoView:
    def __init__(self,argp,mod):
        self.ncurses = False
        self.argp = argp
        self.model = mod
        self.useropt = None

    def getparsedArgs(self):
        self.useropt = self.argp.parseArgs(sys.argv)

    def handleOpt(self):
        if self.useropt['ls']:
            self.model.connectDB()
            self.model.queryDB(1)

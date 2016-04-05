#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Tuesday, April 5th 2016, 11:35:05 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 5th 2016, 11:38:12 am
from vtodocli import vtodoviews, vtodomodels, vtodoparser
import os
from os.path import join, dirname
from dotenv import load_dotenv

def main():
    ap = vtodoparser.VtodoParse()
    db = vtodomodels.VtodoModel()
    boss = vtodoviews.VtodoView(ap,db)
    boss.getparsedArgs()
    boss.handleOpt()

if __name__ == "__main__":
    main()

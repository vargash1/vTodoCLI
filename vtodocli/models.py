#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Tuesday, April 5th 2016, 5:47:03 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Friday, April 15th 2016, 5:29:49 am
import os
import sys
import psycopg2
import psycopg2.extras
from termcolor import colored
from dotenv import load_dotenv


class VTodoModel:
    def __init__(self):
        self.client = None
        self.dbcon = None
        self.connectDB()

    """
    Connects to DB using .env file
    """
    def connectDB(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        CONNSTRING = os.environ.get("CONNSTRING")
        self.dbcon = psycopg2.connect(CONNSTRING)
        self.client = self.dbcon.cursor()

    def get_user(self, username):
        query = "SELECT * FROM users WHERE USERNAME=\'{}\';".format(username)
        self.client.execute(query)
        results = self.client.fetchall()
        self.dbcon.commit()
        return results

    """
    Queries DB
    Type:(0 : insert, 1 : select, 2: delete)
    """
    def queryDB(self,type,username,body=None,title=None,newdate=None,newtime=None):
        if type == 1:
            print colored("Fetching tasks from DATABASE",'green')
            query = "SELECT * FROM notes WHERE username=\'{}\' ORDER BY noteid DESC;".format(username)
            self.client.execute(query)
            result = self.client.fetchall()
            self.dbcon.commit()
            return result

        elif type == 2:
            print colored("Inserting task into DATABASE",'green')
            query = "INSERT INTO notes (username, title, datedue, timedue, taskbody) VALUES (%s, %s, %s, %s, %s);"
            data = (username, title, newdate, newtime, body)
            self.client.execute(query,data)
            self.dbcon.commit()
        elif type == 3:
            query = "DELETE FROM notes WHERE noteid=\'{}\' AND username=\'{}\';".format(body,username)
            self.client.execute(query)
            self.dbcon.commit()
        else:
            print colored("Unkown type to query, unexpected error")
            sys.exit("Unexpected Error")

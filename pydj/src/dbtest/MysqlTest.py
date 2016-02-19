'''
Created on Feb 19, 2016

@author: mehrab
'''
import mysql.connector

from mysql.connector import Error
from django.db.models.sql.constants import CURSOR

config = {'password': 'password', 'host': 'localhost', 'user': 'mehrab', 'database': 'python-db'}

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(**config)
        
        if conn.is_connected():
            print('Connected to MySQL database')
            
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM auth_user")
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print e
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    print __name__
    connect()


#!/usr/bin/python3
'''
The script takes in an arg and displays all values in states
where 'name' matches the arg from db 'hbtn_0e_0_usa'
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    '''
    Áccess to the db and get the states.
    '''

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY %(name)s \
                ORDER BY states.id ASC", {'name': argv[4]})
    rows = cur.fetchall

    for row in rows:
        print(row)

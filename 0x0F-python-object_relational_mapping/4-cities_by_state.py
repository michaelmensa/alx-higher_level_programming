#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    ''' script that lists all cities from db htn_0e_4_usa
    '''

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = 'SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC'
    cur.execute(query)
    cities = cur.fetchall()

    for city in cities:
        print(city)

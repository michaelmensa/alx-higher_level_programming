#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    ''' script that lists all cities from db hbtn_0e_4_usa
    '''

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.name = states.id
            ORDER BY
                cities.id ASC
        """)
        cities = cur.fetchall()

    if cities is not None:
        for city in cities:
            print(city)

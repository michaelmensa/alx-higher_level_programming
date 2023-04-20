#!/usr/bin/python3
'''
this script takes the name of a state as an arg and lists
cities of that state, using the db 'hbtn_0e_0_usa'
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    '''
    Access the db and get the cities from it
    '''

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities,name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))

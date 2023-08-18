#!/usr/bin/python3

"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    query = 'SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %(name)s\
            ORDER BY cities.id ASC'
    cur.execute(query, {'name': sys.argv[4]})

    cities = cur.fetchall()

    if cities is not None:
        print(", ".join([city[0] for city in cities]))

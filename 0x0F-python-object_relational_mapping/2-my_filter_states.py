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
    query = 'SELECT * FROM states WHERE states.name LIKE "{}%" \
            ORDER BY states.id ASC'.format(sys.argv[4])
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()

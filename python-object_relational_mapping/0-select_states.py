#!/usr/bin/python3
''' Script to retrieve data from a database 
Created on Nov 17 09:33:11 2022
@author: Avelino Carvajal'''

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
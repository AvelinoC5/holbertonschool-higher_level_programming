#!/usr/bin/python3
"""This module takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
Created on Nov 17 09:33:11 2022
@author: Avelino Carvajal
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    cont = 0
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8mb4")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states "
                "ON cities.state_id = states.id WHERE BINARY states.name "
                "= BINARY %(states.name)s ORDER BY cities.id ASC",
                {'states.name': argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        if cont > 0:
            print(", ", end="")
        print(row[0], end="")
        cont = cont + 1
    print()
    cur.close()
    conn.close()

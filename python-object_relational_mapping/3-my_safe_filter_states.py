#!/usr/bin/python3
"""This module takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name, Code write one that is safe from MySQL injections.
Created on Nov 17 09:33:11 2022
@author: Avelino Carvajal
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8mb4")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY "
                "name = BINARY %(name)s ORDER BY id ASC", {'name': argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

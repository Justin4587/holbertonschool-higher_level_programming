#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1],
                         argv[2], argv[3], port=3306)
    curse = db.cursor()
    curse.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = curse.fetchall()
    for row in rows:
        print(row)

    curse.close()
    db.close()

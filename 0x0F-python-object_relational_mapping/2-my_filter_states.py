#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1],
                         argv[2], argv[3], port=3306)
    curse = db.cursor()
    curse.execute("SELECT * FROM states WHERE name='{}'\
                   ORDER BY states.id ASC".format(argv[4]))
    rows = curse.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    curse.close()
    db.close()

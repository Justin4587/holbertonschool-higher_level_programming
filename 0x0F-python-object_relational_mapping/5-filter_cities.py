#!/usr/bin/python3
""" I'm going to be mad """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1],
                         argv[2], argv[3], port=3306)
    curse = db.cursor()
    curse.execute("SELECT cities.name\
                   FROM cities JOIN states ON cities.state_id=states.id\
                   WHERE states.name=%s\
                   ORDER BY cities.id ASC", (argv[4], ))
    rows = curse.fetchall()

    string = ""
    for row in range(len(rows)):
        if row != len(rows) - 1:
            string += rows[row][0] + ", "
        else:
            string += rows[row][0]

    print(string)

    curse.close()
    db.close()

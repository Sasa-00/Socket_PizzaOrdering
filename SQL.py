import sqlite3


def creating_table():
    conn = sqlite3.connect('pizzeria.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE PIZZERIA
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    SIZE TEXT NOT NULL,
    QUANTITY INT,
    PRICE INT NOT NULL);''')
    print("Table created successfully")
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (1, 'Capricciosa', '32cm', 40, 550 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (2, 'Capricciosa', '46cm', 36, 650 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (3, 'Pepperoni', '32cm', 33, 580 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (4, 'Pepperoni', '46cm', 30, 680 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (5, 'BBQ Chicken', '32cm', 38, 600 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (6, 'BBQ Chicken', '46cm', 31, 700 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (7, 'Veggie', '32cm', 22, 560 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (8, 'Veggie', '46cm', 25, 660 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (9, 'Margherita', '32cm', 40, 510 )");
    conn.execute("INSERT INTO PIZZERIA (ID,NAME,SIZE,QUANTITY,PRICE) \
    VALUES (10, 'Margherita', '46cm', 44, 610 )");
    conn.commit()
    print("Records created successfully")
    conn.close()


def reading_table():
    conn = sqlite3.connect('pizzeria.db')
    print("Opened database successfully")
    cursor = conn.execute("SELECT id, name, size, quantity, price from PIZZERIA")
    str_tabela = ""
    for row in cursor:
        str_tabela += ("ID = " + str(row[0]))
        str_tabela += (", NAME = " + str(row[1]))
        str_tabela += (", SIZE = " + str(row[2]))
        str_tabela += (", QUANTITY = " + str(row[3]))
        str_tabela += (", PRICE = " + str(row[4]) + "\n")
    print("Operation done successfully")
    conn.close()
    return str_tabela


def deleting_from_table(name, size):

    conn = sqlite3.connect('pizzeria.db')
    conn.execute(f"UPDATE PIZZERIA set QUANTITY = QUANTITY - 1 where NAME = '{name}' and SIZE = '{size}';")
    conn.commit()
    print("Total number of changes :", conn.total_changes)
    cursor = conn.execute("SELECT id, name, size, quantity, price from PIZZERIA")
    str_deleted = ""
    for row in cursor:
        str_deleted += ("ID = " + str(row[0]))
        str_deleted += (", NAME = " + str(row[1]))
        str_deleted += (", SIZE = " + str(row[2]))
        str_deleted += (", QUANTITY = " + str(row[3]))
        str_deleted += (", PRICE = " + str(row[4]) + "\n")
    print("Operation UPDATE done successfully")
    conn.close()
    return str_deleted


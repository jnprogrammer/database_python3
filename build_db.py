import sqlite3, csv, datetime


# TODO: Build tables if there are none
db = sqlite3.connect("transactions.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS transactions "
           "(account_number TEXT, "
           "account_type TEXT, "
           "account_name TEXT, "
           "date DATE, "
           "transaction_info TEXT, "
           "transaction_type TEXT, "
           "amount REAL, "
           "balance REAL)")

cursor = db.cursor()
# TODO: import csv data into application
#  or maybe it can go from the csv to the DB ??
#  but then could that be a vulnerability,
#  better to import the data and verify its valid data. . .


fname = "bnk-prod.csv"

# TODO: export data to database
with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        account_number = row[0]
        account_type = row[1]
        account_name = row[2]
        date = row[3]
        transaction_info = row[4]
        transaction_type = 'unpack Tuple'  # TODO: need to unpack tuple inside this column because it messes up database when not extracted.
        amount = row[8]
        balance = row[9]
        print(row)
        cursor.execute('''INSERT INTO transactions(account_number, account_type, account_name, date, transaction_info, transaction_type, amount, balance)
        VALUES(?,?,?,?,?,?,?,?)''', (account_number, account_type, account_name, date, transaction_info, transaction_type, amount, balance))
        db.commit()



# TODO: create functions that run computations from data in database

# TODO: generate reports on data in graphs


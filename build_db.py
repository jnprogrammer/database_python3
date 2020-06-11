import sqlite3, csv


# TODO: Build tables if there are none
db = sqlite3.connect("transactions.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS transactions (account_number TEXT, account_type TEXT, account_name TEXT, date DATE, "
           "transaction_info TEXT, transaction_type TEXT, ammount REAL, balance REAL)")

cursor = db.cursor()
# TODO: import csv data into application
#  or maybe it can go from the csv to the DB ??
#  but then could that be a vulnerability,
#  better to import the data and verify its valid data. . .

fname =
# TODO: export data to database

# TODO: create functions that run computations from data in database

# TODO: generate reports on data


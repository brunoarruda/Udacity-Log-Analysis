#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)

c = db.cursor()
c.execute("SELECT * FROM INFORMATION_SCHEMA.tables WHERE table_schema='public';")
colnames = [desc[0] for desc in c.description]
results = c.fetchall()

print(colnames)
print(results)

db.close()
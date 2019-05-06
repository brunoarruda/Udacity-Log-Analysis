#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)

c = db.cursor()

# query 1: Quais são os três artigos mais populares de todos os tempos?

# query article titles and transform them in paths as used in log table
query_setup_paths = """
SELECT 
  REGEXP_REPLACE(SUBSTRING(LOWER(title), '[[:alpha:] ]+'), ' ', '-', 'g') as PATHS
FROM articles 
LIMIT 100;
"""
c.execute(query_setup_paths)
results = c.fetchall()

print(c.description)
print(results)

# query 2: Quem são os autores de artigos mais populares de todos os tempos?

# query 3: Em quais dias mais de 1% das requisições resultaram em erros?

db.close()
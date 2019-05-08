#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = 'news'

def print_query(title, description, results):
  results_str = '\n'.join([' - '.join(row) for row in results])
  print('\n{}\n\n{}'.format(title, results_str))

def main():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()

  # registering views in database  
  sql = open('views.sql').read()
  for query in sql.split(';'):
    if query.strip():
      c.execute(query)

  # query 1 
  query_title = 'Quais são os três artigos mais populares de todos os tempos?'
  
  query_most_popular_articles = """
  SELECT
    "article title",
    "access count"::text || 'views'
  FROM title_access_count_and_author
  LIMIT 3;"""
  c.execute(query_most_popular_articles)
  print_query(query_title, c.description, c.fetchall())
  
  # query 2
  query_title = 'Quem são os autores mais populares de todos os tempos?'
  
  query_authors_of_most_popular_articles = """
  SELECT author, views::text || 'views'
  FROM (
    SELECT author, SUM("access count") AS views
    FROM title_access_count_and_author
    GROUP BY author
    ORDER BY views
    LIMIT 3) AS subquery;"""

  c.execute(query_authors_of_most_popular_articles)
  print_query(query_title, c.description, c.fetchall())

  # query 3
  query_title = 'Em quais dias mais de 1% das requisições resultaram em erros?'
  
  query_days_with_server_problems = """
  WITH
    status_not_found AS (
      SELECT DATE(time) AS Data, COUNT(status) as count
      FROM log  
      GROUP BY DATE(time), status
      HAVING status = '404 NOT FOUND'
      ORDER BY Data DESC
    ),
    status_all AS (
      SELECT DATE(time) AS Data, COUNT(status) as count
      FROM log  
      GROUP BY DATE(time), status
      ORDER BY Data DESC
    )
    SELECT 
      subquery.data::TEXT,
      CAST(subquery.porcentagem AS VARCHAR(3)) || '% de erro' AS Porcentagem
    FROM (
      SELECT 
        status_all.data, 
        (status_not_found.count/status_all.count::DECIMAL)*100 AS Porcentagem
      FROM status_all
      INNER JOIN status_not_found
      ON status_all.data = status_not_found.data
      ORDER BY porcentagem DESC, data ASC
    ) as subquery
    WHERE subquery.porcentagem > 1;"""
  c.execute(query_days_with_server_problems)
  print_query(query_title, c.description, c.fetchall())

  db.close()

if __name__ == '__main__':
  main()
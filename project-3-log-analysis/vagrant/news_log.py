#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)

c = db.cursor()

# query 1: Quais são os três artigos mais populares de todos os tempos?

view_article_dashed_titles = """
CREATE VIEW article_dashed_titles AS
SELECT
  REGEXP_REPLACE(SUBSTRING(LOWER(title), '[[:alpha:] ]+'), ' ', '-', 'g')
  AS dashedTitles
FROM articles;
"""
c.execute(view_article_dashed_titles)

view_log_dashed_titles = """
CREATE VIEW log_dashed_titles AS
SELECT innerquery.dashedTitles
FROM (
  SELECT
    SUBSTRING(path, '^/article/(.*)') AS dashedTitles
  FROM log) as innerquery
WHERE innerquery.dashedTitles IS NOT NULL;
"""
c.execute(view_log_dashed_titles)

view_articles_title_and_access_count = """
CREATE VIEW article_title_and_access_count AS
SELECT articles.dashedTitles as "article title", COUNT(*) as "access count"
FROM article_dashed_titles as articles
INNER JOIN log_dashed_titles as log
ON articles.dashedTitles = log.dashedTitles
GROUP BY "article title"
ORDER BY "access count" DESC
LIMIT 3;
"""

c.execute(view_articles_title_and_access_count)
c.execute('SELECT * FROM article_title_and_access_count')
results = c.fetchall()

print(results)

# query 2: Quem são os autores de artigos mais populares de todos os tempos?


# query 3: Em quais dias mais de 1% das requisições resultaram em erros?

db.close()

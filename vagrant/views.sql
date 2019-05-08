-- views created to make the queries as requested on project

-- View to query title of articles, a transformation of title to correspond to paths on logs and their authors
CREATE VIEW dashed_titles_and_author
AS
SELECT
  articles.title,
  REGEXP_REPLACE(SUBSTRING(LOWER(articles.title), '[[:alpha:] ]+'), ' ', '-', 'g') AS dashedTitles,
  authors.name AS author
FROM articles
INNER JOIN authors
  ON articles.author = authors.id;

-- View to transform paths of log in a correspondence to titles of articles
CREATE VIEW paths_as_dashed_titles
AS
SELECT
  subquery.dashedTitles
FROM (SELECT
  SUBSTRING(path, '^/article/(.*)') AS dashedTitles
FROM log) AS subquery
WHERE subquery.dashedTitles IS NOT NULL;

-- View to count accesses of articles, along with title and author
CREATE VIEW title_access_count_and_author AS
SELECT 
  articles.title AS "article title", 
  COUNT(articles.title) AS "access count",
  articles.author
FROM 
  dashed_titles_and_author as articles
  INNER JOIN paths_as_dashed_titles as visits
  ON articles.dashedTitles = visits.dashedTitles
GROUP BY "article title", author
ORDER BY "access count" DESC;

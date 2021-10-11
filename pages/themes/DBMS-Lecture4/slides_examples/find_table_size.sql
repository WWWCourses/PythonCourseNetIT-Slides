SELECT
  TABLE_SCHEMA AS `Database`,
  TABLE_NAME AS `Table`,
  ROUND((DATA_LENGTH) ) AS `Size (B)`
FROM
  information_schema.TABLES
WHERE
    TABLE_SCHEMA = "test"
  AND
    TABLE_NAME = "dt"
ORDER BY
  (DATA_LENGTH)
DESC;

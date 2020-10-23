# PostgreSQL

## Database Fundamentals

### ORMS
- Programattic interfaces with your database that represent tables/records as classes/objects.

### ACID
- Atomicity:  guarantees that each transaction is treated as a single "unit", which either succeeds completely, or fails completely: if any of the statements constituting a transaction fails to complete, the entire transaction fails and the database is left unchanged. 
- Consistency: ensures that a transaction can only bring the database from one valid state to another, maintaining database invariants
- Isolation: ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially
- Durability:  guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure

### Transactions
- DB's don't write directly to the files. They typically write to log files that are periodally flushed and saved. So a commit isn't really a commit

### N+1 Problem
- Most ORMs have lazy-loading enabled by default, so queries are issued for the parent record, and then one query for EACH child record. As you can expect, doing N+1 queries instead of a single query will flood your database with queries, which is something we can and should avoid.

### Normalization
- Different leveling of normalizating data through relationships defined by foreign key to other tables to reduce duplication.

### Index
- Indexing is a way of sorting a number of records on multiple fields. Creating an index on a field in a table creates another data structure which holds the field value, and a pointer to the record it relates to. This index structure is then sorted, allowing Binary Searches to be performed on it.

## PSQL Commands
```
psql -d database -U  user -W
psql -d dvdrental -U postgres -W
\c dbname username -- switch database
\l -- list databases
\d table_name -- describe table
\dn - list schemas
\df - List functions
\dv - List Available views
\du - List users
\s - command history
\s filename - command history to a file
\timing command - turns on timing in queries


```

## ANSI SQL
- Not much to add here. ANSI SQL is pretty similar as you switch databases. 
```
    select column_a, 10 as ALIAS
    from TABLE_NAME one
    inner join table_two as two
    on one.id = two.id
    where column_b = 100
    AND colum_c in ('1','2')
    OR column_d like '%jan%'
    order by column_a
    limit 4 offset 3 || fetch first 5 row only;
UNION
    select column_a, sum(some_column) as ALIAS
    from TABLE_NAME one
    inner join table_two as two
    on one.id = two.id
    group by column_a
    having sum(some_column) > 10
    order by column_a
    limit 4 offset 3 || fetch first 5 row only;
UNION select column_a, 10 
    from table_name
    join (select * from some_table)
     on id = id
```
## CTE's Always
```
WITH cte_film AS (
    SELECT 
        film_id, 
        title,
        (CASE 
            WHEN length < 30 THEN 'Short'
            WHEN length < 90 THEN 'Medium'
            ELSE 'Long'
        END) length    
    FROM
        film
)
SELECT
    film_id,
    title,
    length
FROM 
    cte_film
WHERE
    length = 'Long'
ORDER BY 
    title; 
```

## Modifying Data
- Insert – guide you on how to insert single row into a table.
- Insert multiple rows – show you how to insert multiple rows into a table.
- Update – update existing data in a table.
- Update join – update values in a table based on values in another table.
- Delete – delete data in a table.
- Upsert – insert or update data if the new row already exists in the table.

## Postgre Transactions
- BEGIN, COMMIT, ROLLBACK

## Managing Tables
```
ALTER TABLE IF EXISTS table_name
RENAME TO new_table_name;

ALTER TABLE table_name 
ADD COLUMN column_name datatype column_constraint;

ALTER TABLE table_name 
DROP COLUMN column_name;

ALTER TABLE table_name
ALTER COLUMN column_name [SET DATA] TYPE new_data_type;

ALTER TABLE table_name 
RENAME COLUMN column_name TO new_column_name;

DROP TABLE [IF EXISTS] table_name 
[CASCADE | RESTRICT];

TRUNCATE TABLE table_name;

CREATE TEMPORARY TABLE temp_table_name(
   column_list
);

CREATE TABLE new_table AS 
TABLE existing_table;

```

### Data Types
- Boolean
- Character types such as char, varchar, and text.
- Numeric types such as integer and floating-point number.
- Temporal types such as date, time, timestamp, and interval
- UUID for storing Universally Unique Identifiers
- Array for storing array strings, numbers, etc.
- JSON stores JSON data
- hstore stores key-value pair
- Special types such as network address and geometric data.

## Creating Tables
```
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_contraint,
   column2 datatype(length) column_contraint,
   column3 datatype(length) column_contraint,
   table_constraints
);
```
### Constraints
- NOT NULL – ensures that values in a column cannot be NULL.
- UNIQUE – ensures the values in a column unique across the rows within the same table.
- PRIMARY KEY – a primary key column uniquely identify rows in a table. A table can have one and only one primary key. The primary key - constraint allows you to define the primary key of a table.
- CHECK – a CHECK constraint ensures the data must satisfy a boolean expression.
- FOREIGN KEY – ensures values in a column or a group of columns from a table exists in a column or group of columns in another table. - Unlike the primary key, a table can have many foreign keys.

### Auto Increment
```
CREATE SEQUENCE table_name_id_seq;

CREATE TABLE table_name (
    id integer NOT NULL DEFAULT nextval('table_name_id_seq')
);

ALTER SEQUENCE table_name_id_seq
OWNED BY table_name.id;
```
OR
```
CREATE TABLE table_name(
    id SERIAL
);
```
OR 
GENERATED AS IDENTITY

## Sequences
```
CREATE SEQUENCE [ IF NOT EXISTS ] sequence_name
    [ AS { SMALLINT | INT | BIGINT } ]
    [ INCREMENT [ BY ] increment ]
    [ MINVALUE minvalue | NO MINVALUE ] 
    [ MAXVALUE maxvalue | NO MAXVALUE ]
    [ START [ WITH ] start ] 
    [ CACHE cache ] 
    [ [ NO ] CYCLE ]
    [ OWNED BY { table_name.column_name | NONE } ]
```
```
CREATE SEQUENCE mysequence
INCREMENT 5
START 100;
```

## Triggers
```
CREATE OR REPLACE FUNCTION log_last_name_changes()
  RETURNS TRIGGER 
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	IF NEW.last_name <> OLD.last_name THEN
		 INSERT INTO employee_audits(employee_id,last_name,changed_on)
		 VALUES(OLD.id,OLD.last_name,now());
	END IF;

	RETURN NEW;
END;
$$

DROP TRIGGER [IF EXISTS] trigger_name 
ON table_name [ CASCADE | RESTRICT ];

ALTER TRIGGER trigger_name
ON table_name 
RENAME TO new_trigger_name;

ALTER TABLE table_name
DISABLE TRIGGER trigger_name | ALL

ALTER TABLE table_name
ENABLE TRIGGER trigger_name |  ALL;
```

## Views
```
CREATE VIEW view_name AS query;

CREATE OR REPLACE view_name 
AS 
query

DROP VIEW [ IF EXISTS ] view_name;

CREATE MATERIALIZED VIEW view_name
AS
query
WITH [NO] DATA;

```

# Indexes
```
REINDEX TABLE table_name;   
REINDEX INDEX index_name;

CREATE INDEX index_name ON table_name [USING method]
(
    column_name [ASC | DESC] [NULLS {FIRST | LAST }],
    ...
);

DROP INDEX  [ CONCURRENTLY]
[ IF EXISTS ]  index_name 
[ CASCADE | RESTRICT ];

SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    schemaname = 'public'
ORDER BY
    tablename,
    indexname;
```

### Index Types
- B-Tree: Maintains sorted data, allows searches, insertions, deletions, and sequential access in logarithmic time.
- Hash: Great for = Comparison
```
CREATE INDEX index_name 
ON table_name USING HASH (indexed_column);
```
- GIN :  generalized inverted indexes. useful when you have multiple values stored in a single column, for example, hstore, array, jsonb, and range types
- BRIN:  block range indexes. BRIN allows the use of an index on a very large table that would previously be impractical using B-tree without horizontal partitioning. for example, the created date column of the sales order table.
- GiST: useful in indexing geometric data types and full-text search.
- SP-GiST: supports partitioned search trees that facilitate the development of a wide range of different non-balanced data structures.

### MultiColumn Index
```
CREATE INDEX index_name
ON table_name(a,b,c,...);
```

## Administration
### Create Database
```
CREATE DATABASE database_name
WITH
   [OWNER =  role_name]
   [TEMPLATE = template]
   [ENCODING = encoding]
   [LC_COLLATE = collate]
   [LC_CTYPE = ctype]
   [TABLESPACE = tablespace_name]
   [ALLOW_CONNECTIONS = true | false]
   [CONNECTION LIMIT = max_concurrent_connection]
   [IS_TEMPLATE = true | false ]
```
### Check Sizes
```
SELECT
    relname AS "relation",
    pg_size_pretty (
        pg_total_relation_size (C .oid)
    ) AS "total_size"
FROM
    pg_class C
LEFT JOIN pg_namespace N ON (N.oid = C .relnamespace)
WHERE
    nspname NOT IN (
        'pg_catalog',
        'information_schema'
    )
AND C .relkind <> 'i'
AND nspname !~ '^pg_toast'
ORDER BY
    pg_total_relation_size (C .oid) DESC
LIMIT 5;

SELECT
    pg_size_pretty (
        pg_database_size ('dvdrental')
    );

SELECT
    pg_size_pretty (
        pg_tablespace_size ('pg_default')
    );

SELECT
    pg_size_pretty (pg_indexes_size('actor'));

```
### Schemas
```
CREATE SCHEMA [IF NOT EXISTS] schema_name;

CREATE ROLE john 
LOGIN
PASSWORD 'Postgr@s321!';

CREATE SCHEMA AUTHORIZATION john;
```

### Tablespaces
```
CREATE TABLESPACE tablespace_name
OWNER user_name
LOCATION directory_path;
```

### Roles
```
CREATE ROLE dev_api WITH
LOGIN
PASSWORD 'securePass1'
VALID UNTIL '2030-01-01';

GRANT privilege_list | ALL 
ON  table_name
TO  role_name;

REVOKE privilege | ALL
ON TABLE table_name |  ALL TABLES IN SCHEMA schema_name
FROM role_name;
```

### Backup/Restores
```
pg_dump -U postgres -W -F t dvdrental > c:\pgbackup\dvdrental.tar
```
```
psql -U username -f backupfile.sql
```
```
pg_restore --dbname=newdvdrental --verbose c:\pgbackup\dvdrental.tar
```
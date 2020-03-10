# multicorn\_urllib

This is a foreign data wrapper using multicorn and python's urllib module in order to download any data as a table within PostgreSQL.

## How to Use

1. Install multicorn
2. Create the server in PostgreSQL
3. Create the foreign table
4. Run simple SELECT queries filtering for a single URL.

```
$ sudo apt install postgresql-12-python3-multicorn
$ sudo -u postgres psql target_database
```

```SQL
CREATE SERVER multicorn_urllib FOREIGN DATA WRAPPER multicorn OPTIONS ( wrapper 'urllibfdw.UrllibForeignDataWrapper' );
CREATE FOREIGN TABLE some_schema.the_internet ( url CHARACTER VARYING, response CHARACTER VARYING ) SERVER multicorn_urllib;
SELECT * FROM some_schema.the_internet WHERE url='https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv';
```

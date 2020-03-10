# multicorn\_urllib

This is a foreign data wrapper using multicorn and python's urllib module in order to download any data as a table within PostgreSQL.

## How to Use

1. Make sure you have an SMTP server running on localhost.
2. Install multicorn
3. Create the server in PostgreSQL
4. Create the foreign table
5. INSERT into the table with `from`, `to`, `subject`, `body_html` and `body` columns.

```
$ sudo apt install postgresql-12-python3-multicorn
$ sudo -u postgres psql target_database
```

```SQL
CREATE SERVER multicorn_smtp FOREIGN DATA WRAPPER multicorn OPTIONS ( wrapper 'urllibfdw.MailerForeignDataWrapper' );
CREATE FOREIGN TABLE some_schema.mailing ( "from" text, "to" text, "subject" text, "body" text, "body_html" text) SERVER multicorn_smtp;
INSERT INTO some_schema.mailing ("from", "to", "subject", "body", "body_html") VALUES ('sender@example.com', 'recipient@example.com', 'hello world !', '<strong>hello</strong> world !')
```

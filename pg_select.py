# -*- coding: UTF8
#
#  pg_select.py: run SQL SELECT of Postgresql from python 
#  
#  Ver-0.01, 20180513: initial implementation.
#
#      using psycopg2 module to connect to PostgreSQL server.
#
import get_argv
import psycopg2
import psycopg2.extensions



DSN = "dbname='NxJapanSeSme' user='postgres' host='172.16.251.24' password='Pg2018tm'"
conn = psycopg2.connect(DSN)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
conn.set_client_encoding("UTF8")
cur = conn.cursor()

cur.execute("SELECT se_key, se_full_name_eng, se_full_name_jp from se_t")
rows = cur.fetchall()
for row in rows:
    print row[0], row[1], row[2]

conn.commit()

cur.execute("COMMIT")
cur.close
conn.commit


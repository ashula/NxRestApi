# -*- coding: UTF8
#
#  pg_sql.py: run SQL query of Postgresql from python
#  
#  Ver-0.01, 20180513: initial implementation from pg_select.py
#
#      using psycopg2 module to connect to PostgreSQL server.
#
#
#     argv[1]: IP address of PostGresql server.
#     argv[2]: DB Name to access.
#     argv[3]: user of DB.(default is 'postgres')
#     argv[4]: password of DB.
#     argv[5]: SQL statement
#
import get_argv
import psycopg2
import psycopg2.extensions

def pg_sql(IP, DBNAME, USER, PASSWORD, SQL):

    DSN = "dbname='"+DBNAME+"' user='"+USER+"' host='"+IP+"' password='"+PASSWORD+"'"
    conn = psycopg2.connect(DSN)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
    conn.set_client_encoding("UTF8")
    cur = conn.cursor()

    #cur.execute("SELECT se_key, se_full_name_eng, se_full_name_jp from se_t")

    try:
        cur.execute(SQL)
    except Exception, e:
        pass

    # psycopg2.errorcodes.lookup(e.pgcode[:2])
    # psycopg2.errorcodes.lookup(e.pgcode)

    r=[]

    rows = cur.fetchall()
    for row in rows:
        # print cols
        for col in row:
            print col,
            print ",",
            r.append(col)
    print

    conn.commit()

    cur.execute("COMMIT")
    cur.close
    conn.commit

    return r

if (__name__=='__main__'):
    argv = get_argv.get_argv(6)

    IP = argv[1]                    #  172.16.251.24
    DBNAME = argv[2]                #  'NxJapanSeSme'
    USER = argv[3]                  #  'postgres'
    PASSWORD = argv[4]              #  'password'
    # SQL = arvg[5]
    # SQL = "SELECT se_key, se_full_name_eng, se_full_name_jp from se_t"
    SQL = "SELECT * from se_t"

    r = pg_sql(IP, DBNAME, USER, PASSWORD, SQL)

    for element in r:
        print element,
        print ",",
    print

else:
    pass

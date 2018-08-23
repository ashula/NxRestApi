# config: UTF-8
#
#   make list html/php/pgsql script source from list of row names of table
#
#   #00: table name
#   #01: 1st column name
#   #02: 2nd column name
#      :
#      :
#   #(n-1): last column name
#
#   Ver-0.01: 28May2018, Initial implementation
#

import sys

def gen_list_pgsql(fn):

    # fn = './pg_row_list.txt'

    f = open(fn)
    line = f.readline()
    f.close()

    rows=[]

    with open(fn) as f:
        for line in f:
            line = line.rstrip('\r\n')
            rows.append(line)

    print rows
    print rows[1:]
    print rows[2:]

    # sql select query statement
    print
    sys.stdout.write('$sql = "SELECT ')
    sys.stdout.write(rows[1].rstrip())
    for row in rows[2:]:
    #    print (', %s') % row.stlip(),
        sys.stdout.write(', ')
        sys.stdout.write(row.rstrip())

    print (' FROM %s ";') % rows[0]

    # print row of titles of each colums
    num = 0
    print ('echo "<table border=\\"1\\">";')
    print ('echo "<tr>";')
    for row in rows[1:]:
        print 'echo "<td>%s</td>";' % row
    print ('echo "</tr>";')
    print
    # print row(s) of data of each colums
    print ('foreach ($dbh->query($sql) as $row){')
    print ('    echo "<tr>";')
    for row in rows[1:]:
        print('    echo "<td>".$row[\'%s\']."</td>";')  %  row
    print ('    echo "</tr>";')
    print ('}')

if (__name__== '__main__') :

    fn = sys.argv[1]
    print fn

    gen_list_pgsql(fn)

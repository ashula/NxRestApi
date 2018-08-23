# config: UTF-8
#
#   make insert SQL html/php/pgsql script source from list of row names of table
#
#   #00: table name
#   #01: 1st column name
#   #02: 2nd column name
#      :
#      :
#   #(n-1): last column name
#
#   input val1, val2,..., valN  from form or ULR parameters.
#
#   $sql =  "INSERT INTO <<table>> (col1, col2, col3,..., colN) VALUES (val1, val2, val3, .... valN);"
#
#   Ver-0.01: 18Jun2018, Initial implementation
#

import sys

def gen_ins_pgsql(fn):

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

    print "---insert SQL statement-----------------"

    # sql INSERT query statement
    ## make parameters blank for initialization.
    print "------make parameters blank for initialization---"

    print
    sys.stdout.write("$")
    sys.stdout.write(rows[1].rstrip())
    sys.stdout.write('="";')
    print

    for column in rows[2:]:
        sys.stdout.write("$")
        sys.stdout.write(column.rstrip())
        sys.stdout.write('="";')
        print
    print

    ## get parameters from POST-ed HTML page

    print
    print "------get parameters from POST-ed HTML page---"
    sys.stdout.write("$")
    sys.stdout.write(rows[1].rstrip())
    sys.stdout.write('=@$_POST["')
    sys.stdout.write(rows[1].rstrip())
    sys.stdout.write('"];')
    print

    for column in rows[2:]:
        sys.stdout.write("$")
        sys.stdout.write(column.rstrip())
        sys.stdout.write('=@$_POST["')
        sys.stdout.write(column.rstrip())
        sys.stdout.write('"];')
        print
    print

    ### generate SQL INS statement
    print
    print "------generate SQL INSERT statement---"

    sys.stdout.write('$sql_ins = "INSERT INTO ')
    sys.stdout.write(rows[0].rstrip())
    sys.stdout.write(' (')
    sys.stdout.write(rows[1].rstrip())
    for column in rows[2:]:
    ###    print (', %s') % row.stlip(),
        sys.stdout.write(', ')
        sys.stdout.write(column.rstrip())

    sys.stdout.write (') VALUES (')

    ###  print list of value of each colummn.
    sys.stdout.write(':')
    sys.stdout.write(rows[1].rstrip())
    for column in rows[2:]:
        sys.stdout.write(',:')
        sys.stdout.write(column.rstrip())
    print (');";')

    print ("---SQL parameter bind----")

    # $conn = new PDO($dsn, $user, $pass) ;

    print "$conn = new PDO($dsn, $user, $pass) ;"
    print 'print ("DB connect succeeded.<br>");'
    print "$stmt = $conn->prepare($sql_ins);"

    sys.stdout.write('$stmt->bindparam(":')
    sys.stdout.write(rows[1].rstrip())
    sys.stdout.write('",$')
    sys.stdout.write(rows[1].strip())
    sys.stdout.write(');')
    print
    for column in rows[2:]:
        sys.stdout.write( '$stmt->bindparam(":')
        sys.stdout.write(column.rstrip())
        sys.stdout.write('",$')
        sys.stdout.write(column.strip())
        sys.stdout.write(');')
        print

    sys.stdout.write('$stmt->execute();')
    print

    print "---HTML Input Form-------------"
    print "not completed yet."

    print '<form method="POST" action="<?php echo $_SERVER["PHP_SELF"]?>">'
    print "<table>"

    # 1st user column. Please remove if this column type is 'serial' of pgsql
    print "<tr>"
    sys.stdout.write('<td>')
    sys.stdout.write(rows[1].rstrip())
    sys.stdout.write(':')
    print('</td>')
    sys.stdout.write('<td><input type="text" name="')
    sys.stdout.write(rows[1].rstrip())
    sys.stdout.write('"')
    print('></td>')
    print "</tr>"
    print

    num=0

    # 2nd and following user columns.
    # Please be careful whether or not each column is NO NULL or not.
    for column in rows[2:]:
      print "<tr>"
      sys.stdout.write('<td>')
      sys.stdout.write(column.rstrip())
      sys.stdout.write(':')
      print('</td>')
      sys.stdout.write('<td><input type="text" name="')
      sys.stdout.write(column.rstrip())
      sys.stdout.write('"')
      print('></td>')
      print "</tr>"
      print

    # insert buttom
    print ('<tr>')
    sys.stdout.write('<td><input type="submit" value="insert" name="sub1"></td>')
    print ('</tr>')

    print "</table>"
    print "</form>"

    ## print row of titles of each colums
    #num = 0
    #print ('echo "<table border=\\"1\\">";')
    #print ('echo "<tr>";')
    #for row in rows[1:]:
    #    print 'echo "<td>%s</td>";' % row
    #print ('echo "</tr>";')
    #print
    ## print row(s) of data of each colums
    #print ('foreach ($dbh->query($sql) as $row){')
    #print ('    echo "<tr>";')
    #for row in rows[1:]:
    #    print('    echo "<td>".$row[\'%s\']."</td>";')  %  row
    #print ('    echo "</tr>";')
    #print ('}')

if (__name__== '__main__') :

    fn = sys.argv[1]
    print fn

    gen_ins_pgsql(fn)

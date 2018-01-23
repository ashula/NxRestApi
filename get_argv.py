#
#    get_argv.py
#
#    get argment strings into returning list
#
#    Ver-0.03: 23Jan2018, return argc, argv[]
#    Ver-0.02: 25Oct2017, Check actual argc and argv.
#    Ver-0.01: 23Oct2017, Initial implementation.
#
#    Simple check whether or not the number of given argments including prog-name is the same as specified number.
#
#    arg[0]: program name in execution command.
#    arg[1]: 1st argment.
#    arg[2]: 2nd argment.
#      :
#    arg[num_argc-1]: (num_argc -1)th argument.
#
#    return number of args and list of argvs.
#
import sys

def get_argv(num_argc):
    argv=sys.argv
    argc=len(sys.argv)

    if (argc!=num_argc):
        print >> sys.stderr, "Error: number(%d) of argments is wrong aganst specified(%d)" % (num_argc, argc)
        print >> sys.stderr, argv
        sys.exit()
    return argc, argv

if (__name__=="__main__"):
    argc, argv = get_argv(5)
#    print >> sys.stderr, argv
    print "argc=%s" % argc
    i=0
    for x in argv[0:]:
        print "argv[%s]=%s" % (i, x)
        i +=1



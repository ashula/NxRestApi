#
#    get_argv.py
#
#    get argment strings into returning list
#
#    Ver-0.01: 23Oct2017, Initial implementation.
#
#    Simple check whether or not the number of given argments including prog-name is the same as specified number.
#
#    arg[0]: program name in execution command.
#    arg[1]: 1st argment.
#    arg[2]: 2nd argment.
#      :
#    arg[num_argc-1]: (num_argc -1)th argment.
#
import sys

def get_argv(num_argc):
    argv=sys.argv
    argc=len(sys.argv)

    if (argc!=num_argc):
        print >> sys.stderr, "Error: number(%d) of argments is wrong aganst specified(%d)" % (num_argc, argc)
        sys.exit()
    return argv

if (__name__=="__main__"):
    argv = get_argv(4)
#    print >> sys.stderr, argv
    i=0
    for x in argv[0:]:
        print "argv[%s]=%s" % (i, x)
        i +=1
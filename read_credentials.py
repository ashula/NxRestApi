#
#    read_credentials.py
#    READ Nutanix credentials(combination of UID and PASSWORD) from specified file.
#        for test purpose 'CREDENTIALS_LIST.txt' is used
#
#    Ver-0.10:18Oct2017, Initial coding.
#
#    Note: credentials list file must has unix/linux line termination (0x0a), not like windows(0x0d,0x0a). 
#
import os
import sys

def read_credentials(fname):
    f = open(fname, 'r')

    uid = f.readline()[:-1]
    pwd = f.readline()[:-1]

    if pwd == '':
        print sys.stderr, "%s is bad format!!, exit program."  % fname
        close(f)
        exit()

    credentials_list = [uid, pwd]

    while (uid != '' and pwd !=''):
        uid = f.readline()[:-1]
        pwd = f.readline()[:-1]
        if pwd != '':
            credentials_list.append(uid)
            credentials_list.append(pwd)

    return credentials_list

if __name__ == '__main__':
    fname = 'CREDENTIALS_LIST.txt'
    credentials_list = read_credentials(fname)
    print  credentials_list


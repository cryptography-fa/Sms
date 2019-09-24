# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, sys
username = 'buat sendiri lah ajg'
password = 'aing ga di hargai juga bisa nghargai orang asu'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('username : ')
    if uname == username:
        pwd = raw_input('password : ')
        if pwd == password:
            print '\n\x1b[1;34mWOKE WELCOM TO MY TOOLS',
            sys.exit()
        else:
            print '\n\x1b[1;36mKALO GA TAU GA USAH MAKSA ASU!!!\x1b[00m'
            print 'LOGIN KEMBALI \n'
            restart()
    else:
        print '\n\x1b[1;36mUSERNAME BUKAN ITU ASW !!!\x1b[00m'
        print 'LOGIN BALIK AH\n'
        restart()


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
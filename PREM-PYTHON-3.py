#!/usr/bin/python3
#-*- coding: utf-8 -*-
#marshal py3

'''
PyMarshal - Compile Python Script
THIS PROJECT WAS CREATER BY MR PREM PROJECT
Copyright 12 - 07 - 2k19 @prem_babu_3608
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[ PREM-PROJECT ] USED PYTHON VERSION 3")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy3 = """
 (   (         *                              
 )\ ))\ )    (  `       (    (      (         
(()/(()/((   )\))(    ( )\   )\   ( )\    (   
 /(_))(_))\ ((_)()\   )((_|(((_)( )((_)   )\  
(_))(_))((_)(_()((_) ((_)_ )\ _ )((_)_ _ ((_) 
| _ \ _ \ __|  \/  |  | _ )(_)_\(_) _ ) | | | 
|  _/   / _|| |\/| |  | _ \ / _ \ | _ \ |_| | 
|_| |_|_\___|_|  |_|  |___//_/ \_\|___/\___/  
                                              
==============================================
            WELCOME TO PREM PROJECT
==============================================
[✓] OWNER NAME ==> MR PREM BABU JI
[✓] CODED NAME ==> @prem_babu_3608
[✓] VERSION    ==> PREM-PYTHON-3
[✓] WHATSAPP   ==> +91 7009799979
[✓] YOUTUBE    ==> PREM PROJECT
[✓] FACEBOOK   ==> facebook.com/prembabu001
==============================================
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

'''
CODED    ==> @prem_babu_3608
MY NAME  ==> PREM BABU
WHATSAPP ==> 7009799979
YOUTUBE  ==> PREM PROJECT
FACEBOOK ==> facebook.com/prembabu001
NOTICE   ==> THIS TOOL IS MADE BY MR PREM BABU
'''

os.system('clear')
try:
    print(bannerpy3)
    print (y+' ['+w+'+'+y+'] '+w+'EXAMPLE '+y+'   >>>'+w+' /sdcard/prem.py')
    file = input(y+' ['+w+'+'+y+'] '+w+'INPUT FILE'+y+'  >>>'+w+' ')
    o = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'×'+r+'] '+r+'[ '+w+'ERROR '+r+'] '+w+'THIS FILE IS WRONG '+r+'>>> '+w+'"'+dfv+'"\n')
        sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
        print (R + '   ['+W+'×'+R+'] '+R+'[ '+W+'FILE ALLREDY TO ENCRIPTION BY PREM PROJECT\n') 
        sys.exit()

fileout = open(o + 'enc.py', 'w')
fileout.write('#ENCRYPTION BY MR PREM PROJECT\n')
fileout.write('#FACEBOOK => facebook.com/prembabu001\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3) 
print (y+'\n ['+w+'✓'+y+'] '+w+'FILE SUCCESS TO ENCRIPTION BY MR PREM BABU   '+y+'>>> ' + w + o + 'enc.py\n')

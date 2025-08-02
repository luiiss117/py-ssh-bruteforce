## 🚀 Asynchronous SSH Brute Forcer

A high-performance, asynchronous SSH brute-forcing tool written in Python. Leveraging `asyncio` and `asyncssh`, this script attempts multiple username/password combinations concurrently.

---

## 📝 Features

- **Asynchronous Execution:** Built on `asyncio` and `asyncssh`.
- **Configurable Concurrency:** Limit the number of simultaneous SSH connections with Semaphore.
- **Wordlist Support:** Accepts separate user and password lists.
- **Result Summary:** Collects and displays all successful login combinations.
- **Stop On Success Option:** If set, the program will stop brute forcing when a valid credential combination is found.

---

## ⚙️ Requirements

- Python 3.11+
- `asyncssh` library

## 📥 Installation
```bash
git clone https://github.com/luiiss117/py-ssh-bruteforcer
pip install asyncssh
````

---

## 📚 Usage

```
usage: ssh_brute_forcer.py [-h] -i IP [-t TASKS] -u USER_LIST -p PASSWORD_LIST [-P PORT] [--stop-on-success]

options:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IPv4 address of the target host
  -t TASKS, --tasks TASKS
                        Maximum number of tasks at once.
  -u USER_LIST, --user-list USER_LIST
                        User list.
  -p PASSWORD_LIST, --password-list PASSWORD_LIST
                        Password list.
  -P PORT, --port PORT  Alternative SSH port.
  --stop-on-success     Stop if a valid credential combination is found.
```

## 🌟 Example

```bash
python3 ssh_brute_forcer.py -i 127.0.0.1 -u users.txt -p passwords.txt -t 4 --stop-on-success
[-] Incorrect login: hidalgo:Contraseña1234
[-] Incorrect login: hidalgo:hola123
[-] Incorrect login: hidalgo:adios9999
[-] Incorrect login: arthur:adios9999
[-] Incorrect login: arthur:hola123
[-] Incorrect login: arthur:Contraseña1234
[+] Succesful login: ernest:hola123
Exiting...
[+] Correct logins:
ernest:hola123
All done in 5.73 seconds!
Valid credentials found!
```


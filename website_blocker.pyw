import time
from datetime import datetime as dt

# for windows users with the "\n" in the file directory use "r" host_path =r"C:\Users\marcs\Desktop\Hosts"
hosts_temp=r"C:\Users\marcs\Desktop\jfiles\numpy\webblocker\hosts"
hosts_path=r"C:\Users\marcs\Desktop\Hosts\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

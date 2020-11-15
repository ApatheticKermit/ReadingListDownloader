
import requests
import urllib3
from bs4 import BeautifulSoup
import time
import pandas as pd
url = "https://durham.rl.talis.com/index.html?browse"
#url = "https://rl.talis.com/3/durham/lists/89530171-EFC1-6EB4-EA1C-5D5A91CC8860.html?lang=en"

def parser(url):
    done=0
    while done != 1:
        response = requests.get(url)
        soup =  BeautifulSoup(response.text,"html.parser")
        listoflinks=[]
        i=0
        if url == "https://durham.rl.talis.com/index.html?browse":
            for a in soup.findAll('a', href=True):
                if "https://durham.rl.talis.com/departments" in a["href"] or "https://durham.rl.talis.com/faculties" in a["href"] :
                    if a["href"] not in listoflinks:
                        i+=1
                        listoflinks.append(a["href"])
                        title = a.get('title')
                        print("["+str(i)+"]",title)
            where2go= int(input("Please enter the number you wish to go: "))
            url = listoflinks[where2go-1]
        else:
            for a in soup.findAll('a', href=True):
                if "https://durham.rl.talis.com/" in a["href"]:
                    if a["href"] not in listoflinks:
                        i+=1
                        listoflinks.append(a["href"])
                        title = a.get('title')
                        print("["+str(i)+"]",title)
            if listoflinks == []:
                done = 1
            else:
                where2go= int(input("Please enter the number you wish to go: "))
                url = listoflinks[where2go-1]
    
    btn_onlclick_list = [a.get('onclick') for a in soup.find_all('button')]
    
parser(url)

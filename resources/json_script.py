import requests
from bs4 import BeautifulSoup as BSHTML
import os
import json

'''
Note this is extremely bad
Also this specific script will download both images **and** answers so I should fix that later
'''

def get_images(url):

    rating = url.split("/")[-3].split("-")[0]

    for year in range(2004, 2019): #2004-2018 (this is max range as of 2020)

        question = True

        try:
            r = requests.get(f"{url}{str(year)}")
        except:
            pass

        soup = BSHTML(r.content, features="lxml")
        images = soup.findAll("img")

        for image in images:
            if "individual-problems" in image.decode():
                if question == True:
                    data[rating[0].upper() + "MC"][str(year)]["questions"].append(base_url + str(image['src']))
                    question = False
                else:
                    data[rating[0].upper() + "MC"][str(year)]["answers"].append(base_url + str(image['src']))
                    question = True
            else:
                pass

base_url = "https://www.ukmt.org.uk"

url_list = [
    'https://www.ukmt.org.uk/competitions/solo/intermediate-mathematical-challenge/archive/',
    'https://www.ukmt.org.uk/competitions/solo/junior-mathematical-challenge/archive/',
    'https://www.ukmt.org.uk/competitions/solo/senior-mathematical-challenge/archive/'
]

data = {}

for rating in ["JMC", "IMC", "SMC"]:
    data[rating] = {}
    for i in range(2004, 2019):
        data[rating][str(i)] = {"questions":[], "answers":[]}

print("Script will take a few seconds...")

for url in url_list:
    get_images(url)

with open("file.json", "w") as file:
    json.dump(data, file)

# print("uwu getting some data")
# with open("file.json") as file:
#     data = json.load(file)
#     for i in data["SMC"]["2010"]["questions"]:
#         print(i)
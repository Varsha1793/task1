import requests
from bs4 import BeautifulSoup
import pandas
url="https://www.careerindia.com/colleges/colleges-in-chennai/"

for page in range(1,4):
    request_ = requests.get(url)
    content=request_.content
    soup=BeautifulSoup(content,"html.parser")
    
    colleges=soup.find_all("div",{"class":"edu-detlist-container"})
    info=[]
    for college in colleges:
        college_dictionary={}
        college_dictionary["name"]=college.find("h2",{"class":"edu-det-heading"}).text
        college_dictionary["address"]=college.find("div",{"class":"edu-det-subhead"}).text
        try:
            college_dictionary["contact"]=college.find("div",{"class":"edu-det-lable"}).text
        except AttributeError:
                pass
        info.append(college_dictionary)
dataframe=pandas.DataFrame(info)
dataframe.to_csv("college.csv")

        

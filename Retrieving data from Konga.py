from bs4 import BeautifulSoup
import requests
import pandas as pd

url  = 'https://www.konga.com/product/kids-ride-on-bicycle-with-carrier-and-helmet-5-9-years-6162399'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
master_url='https://www.konga.com'
#item_url= f(master_url)+(item_name)+(item_)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

print('Welcome to the smart item review. This program allows you to retrieve the details of any item on Konga with just the link. Enjoy!!!')
item_link= input("Kindly enter the link to the item page and press enter....")
page = requests.get(item_link)
soup = BeautifulSoup(page.text,'html.parser')
master_list =[]
data_dict ={}
data_dict['item_name']         = soup.find("h4", attrs= {"_24849_2Ymhg"}).text.strip()
data_dict['item_price']        = soup.find("div", attrs= {"_678e4_e6nqh"}).text.strip()
data_dict['item_code']         = soup.find("div", attrs= {"_97fc0_3W515 b50e0_1HOLM"}).text.strip()
data_dict['item_brand']         = soup.find("div", attrs= {"_97fc0_3W515 b50e0_1HOLM"}).text.strip()
data_dict['item_colour']       = soup.find("div", attrs= {"_0e41d_2HzTx _03609_37JE6"})
data_dict['item_discount']     = soup.find("span", attrs= {"b3d46_3IwtW"}).text.strip()
data_dict['Phoneno']           = soup.find("a", id= {"phoneNumberDisplay"}).text.strip()
data_dict['item_seller']       = soup.find("a", attrs= {"_70f3d_3BLwX"}).text.strip()
data_dict['item_description']  = soup.find("div", attrs= {"_96f69_2zWIQ"}).text.strip()
item_detail= master_list.append(data_dict)
df = pd.DataFrame(master_list)
print(df)
df.to_csv(r'C:\Users\DELL\Desktop\web\Item detail with link on Konga.csv', index='False')

#print(item_name,item_price,item_code,item_colour,item_discount,item_Phoneno, item_seller,item_description) 


    

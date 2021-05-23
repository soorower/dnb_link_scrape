import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from discord_webhook import DiscordWebhook, DiscordEmbed
webhook = DiscordWebhook(
    url='https://discord.com/api/webhooks/840041328401842187/Hsw4Ih0CgCUtoIj4DHORY_-UZ_PLIwd9wyJxPntKPkgKkTIIdPWltYTHsgz35PlAiRJt', username="Yahoo Finance For Fiverr")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
url = 'https://www.dnb.com/business-directory.html'
r = requests.get(url, headers = headers)
soup = bs(r.content, 'html.parser')
print(1)
all_industries = [x.find('a')['href'] for x in soup.findAll('div',attrs = {'class':'col-md-6 col-xs-6 link'})]
links = []
for li in all_industries:
    lin = f'https://www.dnb.com/{li}'
    links.append(lin)

    
lists = []
data = {} 
#-------------------------------------Agriculture & forestry industry--------------------------------------------------
agriculture_foresty = links[:15] #15
for ag_for in agriculture_foresty:
    print(ag_for)
    print(2)
    r = requests.get(ag_for, headers = headers)
    soup = bs(r.content, 'html.parser')
    
    reg_links = []
    regions = [x.find('a')['href'] for x in soup.findAll('div',attrs = {'class':'col-md-6 col-xs-6 data'})]
    region_company_num = [int((int(x.text.strip().replace(',','').replace('(','').replace(')',''))/50)+2) for x in soup.findAll('span',attrs = {'class':'number-countries'})]
    for reg in regions:
        lin = f'https://www.dnb.com/{reg}'
        reg_links.append(lin)
    print(3)
    for region,k in zip(reg_links,region_company_num): 
        for i in range(1,k):
            new_link = region[:-1] + str(i)
            print(new_link)
            r = requests.get(new_link, headers = headers)
            soup = bs(r.content, 'html.parser')
            print(4)
            ultimate_comanies1 = [x.find('div').find('a')['href'] for x in soup.findAll('div',attrs = {'class':'col-md-12 data'})]
            ultimate_comanies = []
            for li in ultimate_comanies1:
                lin = f'https://www.dnb.com/{li}'                
                data = {
                    'company url': lin
                }
                lists.append(data)
        

df = pd.DataFrame(lists).drop_duplicates(subset=['company url'], keep='first').reset_index(drop=True)
df.to_csv('dnb_agriculture_and_forestry.csv',encoding = 'utf-8',index=False)


embed = DiscordEmbed(title='Dnb all links', description='agriculture and forestry' )
with open('dnb_agriculture_and_forestry.csv', "rb") as f:
    webhook.add_file(file=f.read(), filename='dnb_agriculture_and_forestry.csv')
webhook.add_embed(embed)
response = webhook.execute()
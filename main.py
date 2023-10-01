"""
Data scraping store.steampowered.com aplication
"""
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

#extraction data:
url = 'https://store.steampowered.com/search'
def get_data(url):
    r = requests.get(url)
    return r.text

#processing data
def parse(data):
    result=[]
    soup = BeautifulSoup(data,'html.parser')
    contents = soup.find('div',attrs={'id':'search_resultsRows'})
    games = contents.find_all('a')

    #print(result)

    for game in games:
        link = game['href'] #untuk redirect ke link tersebut

    #parsing data
        title = game.find('span',{'class':'title'}).text.strip().split('£')[0]
        price = game.find('div',{'class':'search_discount_and_price'}).text.strip().split('£')[0]
        released = game.find('div',{'class':'search_released'}).text.strip().split('£')[0]

        if released == '':
            released='none'

        #sorting data
        data_dict = {
        'title': title,
        'price': price,
        'link':link,
        'released':released,
        }

        #append
        result.append(data_dict)
    return result

#proscess cleaned data from parser
def output (diatas: list):
    for i in diatas:
        print(i)

if __name__ == '__main__':
    data = get_data(url)

    final_data = parse(data)

    output(final_data)








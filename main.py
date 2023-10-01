"""
Data scraping store.steampowered.com aplication
"""
import requests #ekstraksi data
from bs4 import BeautifulSoup #processing data
import json #file to excel
import pandas as pd #dataframe

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

    for list_games in games:
        link = list_games['href'] #untuk redirect ke link tersebut

    #parsing data
        title = list_games.find('span',{'class':'title'}).text.strip().split('£')[0]
        price = list_games.find('div',{'class':'search_discount_and_price'}).text.strip().split('£')[0]
        released = list_games.find('div',{'class':'search_released'}).text.strip().split('£')[0]

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
    #writing json
    with open ('json_result.json', 'w') as outfile:
        json.dump(result,outfile)
    return result

#read json
def load_data():
    with open('json_result.json') as json_file:
        data = json.load(json_file)


#proscess cleaned data from parser
def output (diatas: list):
    for i in diatas:
        print(i)

def generate_data(result, file_name):
    df=pd.DataFrame(result)
    df.to_excel(f'{file_name}.xlsx', index=False)

if __name__ == '__main__':
    data = get_data(url)

    final_data = parse(data)
    file_name= input('masukan nama file:')
    generate_data(final_data,file_name)
    output(final_data)








import requests
import datetime

url = ('https://www.cbr-xml-daily.ru/archive/2022/09/08/daily_json.js')
response = requests.get(url).json()
date = response['Date']
USD = response['Valute']['USD']['Value']
with open('dataset.csv', 'a') as f:
    f.write(date)
    f.write(", ")
    f.write(str(USD))
    f.write("\n")

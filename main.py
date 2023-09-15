import requests
import datetime

d = datetime.date(2021, 9, 1)
df = datetime.datetime.now() + datetime.timedelta(days=1)
while d.year != df.year or d.month != df.month or d.day != df.day:
    month = d.month
    day = d.day
    if month < 10:
        month = "0" + str(d.month)
    if day < 10:
        day = "0" + str(d.day)
    url = ('https://www.cbr-xml-daily.ru/archive/' + str(d.year) + '/' + str(month) + '/' + str(day) + '/daily_json.js')
    response = requests.get(url).json()
    if 'error' in response:
        d += datetime.timedelta(days=1)
    else:
        date = response['Date']
        USD = response['Valute']['USD']['Value']

        with open('dataset.csv', 'a') as f:
            f.write(date)
            f.write(", ")
            f.write(str(USD))
            f.write("\n")
        d += datetime.timedelta(days=1)

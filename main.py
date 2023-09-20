import requests
import datetime

#Дата с которой будем записать данные
d = datetime.date(2023, 9, 1)
df = datetime.datetime.now() + datetime.timedelta(days=1)
#цикл для изменения дат
while d.year != df.year or d.month != df.month or d.day != df.day:
    month = d.month
    day = d.day
    #Изменение строки для месяца
    if month < 10:
        month = "0" + str(d.month)
    # Изменение строки для дней
    if day < 10:
        day = "0" + str(d.day)
    #url сайта с которого загружаем данные
    url = ('https://www.cbr-xml-daily.ru/archive/' + str(d.year) + '/' + str(month) + '/' + str(day) + '/daily_json.js')
    response = requests.get(url).json()
    #Проверка на ошибку, если по определённой дате нет данных
    if 'error' in response:
        d += datetime.timedelta(days=1)
    else:
        #Вытаскиваем данные из response
        date = response['Date']
        USD = response['Valute']['USD']['Value']
        #Записываем данные в файл csv
        with open('dataset.csv', 'a') as f:
            f.write(date)
            f.write(", ")
            f.write(str(USD))
            f.write("\n")
        d += datetime.timedelta(days=1)

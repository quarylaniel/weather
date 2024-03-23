import requests
s_city = "Moscow,RU"
appid = "ba3c02ef35f904b17e5f42e76e8e4f43"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': s_city, 'units': 'imperial', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
    '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
    i['weather'][0]['description'], ">","\r\nВидимость:", i['visibility'], 'm', "\r\nСкорость ветра:",i["wind"]["speed"], "m/c")
print("____________________________")

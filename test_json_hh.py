import requests
import pandas as pd
import json

#Колличество страниц
number_of_pages = 5


job_title = ['Data Analyst', 'Data Scientist', 'Аналитик', 'Аналитик данных']
for job in job_title:
    data=[]
    for i in range(number_of_pages):
        url = 'https://api.hh.ru/vacancies'
        par = {'text': job, 'area':'113','per_page':'10', 'page':i}
        r = requests.get(url, params=par)
        e=r.json()
        data.append(e)
        vacancy_details = data[0]['items'][0].keys()
        df = pd.DataFrame(columns= list(vacancy_details))
        ind = 0
        for i in range(len(data)):
            for j in range(len(data[i]['items'])):
                df.loc[ind] = data[i]['items'][j]
                ind+=1
    csv_name = job+".csv"
    df.to_csv(csv_name)

print(json.dumps(e, indent = 2, sort_keys=True))



for fl in os.listdir('.'):
    
    # Открываем файл, читаем его содержимое, закрываем файл
    f = open('{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()
    print(1)
    # Преобразуем полученный текст в объект справочника
    jsonObj = json.loads(jsonText)
    
    # Получаем и проходимся по непосредственно списку вакансий
    for v in jsonObj['items']:
        
        # Обращаемся к API и получаем детальную информацию по конкретной вакансии
        req = requests.get(v['url'])
        data = req.content.decode()
        req.close()
        
        # Создаем файл в формате json с идентификатором вакансии в качестве названия
        # Записываем в него ответ запроса и закрываем файл
        fileName = '.{}.json'.format(v['id'])
        f = open(fileName, mode='w', encoding='utf8')
        f.write(data)
        f.close()
        
        time.sleep(0.25)
        
print('Вакансии собраны')

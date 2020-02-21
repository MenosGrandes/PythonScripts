from bs4 import BeautifulSoup
import requests
import pendulum
import xlsxwriter
from ics import Calendar, Event

url = 'https://www.triathlete.com/2019/01/training/7033-triathlon-training-plan_338503'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
pretty_soup = soup.prettify()
article_body =  soup.select_one('.article-body')
all_p = article_body.find_all('p')
exercises = []
previous_week = ""
date = pendulum.datetime(2020, 1, 27) #27.01.0219
for p in all_p:
    week = p.find_previous_sibling('h2')
    span = p.select_one('span')
    if span is None:
        continue
    p.span.decompose()
    if week is not None:
        if week != previous_week:
            exercises.append([week.text,date.format('dddd'), p.text,date.format('YYYY-MM-DD')])
            previous_week = week
        else:
            exercises.append(["",date.format('dddd'), p.text,date.format('YYYY-MM-DD')])
    date = date.add(days=1)

c = Calendar()
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('TrainingPlan.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

for week, day, name, date in (exercises):
    worksheet.write(row, col,     week)
    worksheet.write(row, col + 1, day)
    worksheet.write(row, col + 2, name)
    worksheet.write(row, col + 3, date)
    row += 1
    e = Event()
    e.name = name
    e.begin = date
    e.make_all_day()
    c.events.add(e)

workbook.close()
with open('training.ics', 'w') as my_file:
    my_file.writelines(c)
from bs4 import BeautifulSoup
import requests
url = 'https://www.triathlete.com/2019/01/training/7033-triathlon-training-plan_338503'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
pretty_soup = soup.prettify()
article_body =  soup.select_one('.article-body')
all_p = article_body.find_all('p')
exercises = []
previous_week = ""
for p in all_p:
    day = ""
    week = p.find_previous_sibling('h2')
    span = p.select_one('span')
    if span is not None:
        p.span.extract()
        day = span.select_one('strong').text
    if week is not None:
        if week != previous_week:
            exercises.append([week.text,day, p.text])
            previous_week = week
        else:
            exercises.append(["",day, p.text])

    print("~!~!~!")
    
    
    
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('TrainingPlan.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for item, cost, p in (exercises):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    worksheet.write(row, col + 2, p)

    row += 1
workbook.close()

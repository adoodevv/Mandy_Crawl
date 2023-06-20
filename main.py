from bs4 import BeautifulSoup
import requests

html_text = request.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

company_name = jobs.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ', '')
more_info = job.header.h2.a['href']

print(f'Company Name: {company_name.strip()}')
print(f'Skills Required: {skills.strip()}')
print(f'More Information: {more_info}')
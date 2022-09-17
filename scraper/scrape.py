from bs4 import BeautifulSoup
import requests
import json

page = requests.get("https://mhouse.club/dictionary/")#add url

soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all('a', class_='glossary-link-title')
desc = soup.find_all('div', class_='glossary_itemdesc')

results = {}

for element in range(0, len(titles)):
    el_dict = {titles[element].get_text(): {"address": 0, "description": desc[element].get_text(), "points": 0}}
    results.update(el_dict)

json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("words.json", "w") as outfile:
    outfile.write(json_object)

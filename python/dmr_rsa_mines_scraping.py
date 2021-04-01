import requests
import pprint
from bs4 import BeautifulSoup
import csv

URL ='https://www.dmr.gov.za/mineral-policy-promotion/operating-mines/north-west'

results = requests.get(URL)
soup = BeautifulSoup(results.content, 'html.parser')
# print(soup.prettify())

find_result = soup.find_all("div", class_="panel-body")
print(f"count: {len(find_result)}")

# pprint.pprint(find_result[0])
# per_body_content = find_result[0].find_all("div", class_="col-md-6")
# print(f"first mine info element count: {len(per_body_content)}")

# print(per_body_content[0].text)
mines_data_list = []
for i in range(len(find_result)):
    per_mine_content = find_result[i].find_all("div", class_="col-md-6")
    if (len(per_mine_content) > 0):
        mine_dict = {}
        for idx, attr in enumerate(per_mine_content):
            key, val = per_mine_content[idx].text.split(":")
            mine_dict[key.strip()] = val.strip()
        
        mines_data_list.append(mine_dict)

# pprint.pprint(mines_data_list)
print(f"mine data count: {len(mines_data_list)}")

# Get header content
header_list = []
for i in range(len(mines_data_list)):
    keys = list(mines_data_list[i].keys())
    for j, key in enumerate(keys):
        if key not in header_list:
            header_list.append(key)

print(header_list)

# write to csv file
with open("./north_west_active_mines.csv", "w") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=header_list)
    writer.writeheader()
    writer.writerows(mines_data_list)
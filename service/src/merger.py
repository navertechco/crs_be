from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import json
import os 

FILE_PATH = os.path.abspath(__file__)
ROOT_DIR = os.path.dirname(FILE_PATH)
DATA_PATH = os.path.join(ROOT_DIR, ('data.json'))

print(DATA_PATH)

G = open(DATA_PATH, 'r', encoding="utf8")
 
data = json.load(G)
 
cover_doc = os.path.join(ROOT_DIR, ("cover.docx"))
day_doc = os.path.join(ROOT_DIR, ("day.docx"))
end_doc = os.path.join(ROOT_DIR, ("end.docx"))



client_data = {}
tour_data = {}
cover_data = data["cover"]
destinations_data = data["destinations"]
included_data = '-\n'.join(data["end"]["included"])
not_included_data = '-\n'.join(data["end"]["not_included"])
net_rates_data = data["end"]["net_rates"]

for atr in data["client"]:
    client_data[atr["code"]] = atr["value"]
for atr in data["tour"]:
    tour_data[atr["code"]] = atr["value"] 

header = {**client_data, **tour_data, **cover_data}

new_cover = MailMerge(cover_doc)
new_cover.merge(**header) 
new_cover.write(os.path.join(ROOT_DIR, ('cover-output.docx')))

new_end = MailMerge(end_doc)
new_end.merge_rows('room_type', net_rates_data)
new_end.merge(**{"included":included_data})
new_end.merge(**{"not_included":not_included_data})
new_end.write(os.path.join(ROOT_DIR, ('end-output.docx')))


destinations = data["destinations"]

for destination in destinations:
    destination_doc = destination["title"]
    new_day = MailMerge(day_doc)
    days = destination["days"]
    new_day.merge_pages(days)
    for day in days:
        experiences = day["experiences"]
        explist = []
        for experience in experiences:
            exp = '\n\n'.join(list(experience.values()))
            explist.append({"experience":exp,"photo":experience["photo"]})
        new_day.merge_rows('experience', explist)
            
    new_day.write(os.path.join(ROOT_DIR, ('{}-output.docx'.format(destination_doc))))


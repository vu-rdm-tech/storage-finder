import csv
import re
import os

template = [
    "tool",
    "short description",
    "max. storage size",
    "costs",
    "sharing and collaboration",
    "stored at",
    "availability",
    "back-up",
    "versioning",
    "security",
    "get started",
    "more information"
]


# Merge markdown tables to single csv table
def read_table(file):
    info = {}
    with open(file, 'r') as mdfile:
        lines = mdfile.readlines()
    cnt = 0

    for line in lines:
        matching = re.match(r'^\|(.*)\|(.*)\|.*$', line)
        criterion = matching[1]
        value = matching[2]
        if criterion.lower().strip() == 'criterion':
            info['tool'] = value.strip()
        elif criterion.lower().strip() in template:
            info[criterion.lower().strip()] = value
        elif '---' in criterion.lower().strip():
            pass
        else:
            print(f'{criterion} not found in template. Please check ${file}')
        cnt += 1
    return info


listing = os.listdir('..')
print(listing)
ignore=['customised-solutions-description.md', 'table-template.md', 'README.md']

with open('../tools_description.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=template)
    writer.writeheader()
    for file in listing:
        if file.endswith('.md') and file not in ignore:
            print(file)
            info = read_table(f'../{file}')
            writer.writerow(info)



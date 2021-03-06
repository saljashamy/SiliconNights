import xml.etree.ElementTree as ET
import re

# open file to write
f = open('./tags.txt', 'w', encoding='utf-8')
		
# create element tree object
with open('recipe-data.xml', 'r', encoding='utf-8') as file:
	tree = ET.parse(file)
 
# get root element
data = tree.getroot()
count = 1
string = ' '
tags = []

# iterate recipe items
for recipe in data:
	# iterate elements of recipe
	for element in recipe:
		# if ingredientList
		if element.tag == 'tags':
			string = element.text
			string = string.strip('\n')
			current = string.split(',')
			for i in range(0, len(current)):
				current[i] = current[i].strip()
			for tag in current:
				if tag not in tags:
					tags.append(tag)
			count = count + 1
print('# of unique tags:', len(tags))
for item in tags:	
	f.write(item + '\n')
f.close()
print(count)
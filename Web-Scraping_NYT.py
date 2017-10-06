import requests
import os
from bs4 import BeautifulSoup

os.system('clear')

try:
	nyt_data = BeautifulSoup(open("nytimes.html",'r'),'html.parser')
	print("Information taken from cache")
except:
	nyt_data = BeautifulSoup(requests.get("http://www.nytimes.com/pages/todayspaper/index.html").text,'html.parser')
	f = open("nytimes.html",'w')
	f.write(nyt_data.encode('ascii','replace'))
	f.close()
	print("Downloaded from Internet")

div_one = nyt_data.find_all("div",{"class":"story"})

list_of_stories = []
print("Story Information")
for i in range(len(div_one)):
	story_dict = {}

	print(i+1)
	story_dict['Title'] = div_one[i].find('h3').text.strip()
	print("Title: " + story_dict['Title'])

	story_dict['Summary'] = div_one[i].find('p').text.strip()
	print("Summary: " + story_dict['Summary'])

	story_dict['Author'] = div_one[i].find('h6',{'class':'byline'}).text.strip()
	print("Author: " + story_dict['Author'])
	
	try:
		story_dict['Thumbnail'] = div_one[i].find('img')['src'] #.get('src','No thumbnail source')
	except:
		story_dict['Thumbnail'] = ''
	print('Thumbnail:' + story_dict['Thumbnail'])

	list_of_stories.append(story_dict)
	if 'Author' in story_dict and 'Title' in story_dict and 'Summary' in story_dict:
		print("\nStory %d saved successfully\n" % (i+1))

#print(list_of_stories)

# Note: You can also make a class where each variable is saved per story
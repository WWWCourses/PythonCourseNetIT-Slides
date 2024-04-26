import json
from pprint import pprint
from operator import itemgetter

json_file = "pythonbooks.revolunet.com.issues.json"
category = "Beginner"


#read json from file
with open(json_file) as f:
    json_data = json.load(f)


# get only category books
# books = 
# {
# 	"Beginner":[
# 		{
#       "title": 
#       "author":
#       "url"
#     }
# 	],
# 	"Intermediate":[
# 		{
#       "title": 
#       "author":
#       "url"
#     }
# 	],
# }

books = {}

books_list = list(json_data.values())[0]

for i in books_list:
	# pprint.pprint(i)
	# print("~"*50)
	book_category = i['level']
	book_data = {
		"title": i['title'],
    "author":i['author'],
    "url":i['url']
	} 

	if book_category in books.keys():
		books[book_category].append(book_data)
	else:
		books[book_category] = []

count = 1
for i in books["Advanced"]:
	print('{}."{}"\n\t[{}]\n\t{}\n'.format(count,i["title"], i["author"], i["url"]))
	count += 1
# # print the list sorted by "price" 
# for i in sorted(json_data,key=itemgetter("price")):
# 	print(i)
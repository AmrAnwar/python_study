import re 
"""
names_file = open("names.txt",encoding="utf-8")
data = names_file.read()
names_file.close()
"""
with open("names.txt",encoding="utf-8") as open_file:
    data = open_file.read()

# print(data)
# first_name = r'Love'
# last_name = r'Kenneth'
#in the first of the string 
# print(re.match(first_name,data))
# print(re.search(last_name,data))

# phone_number=r'\(\d\d\d\) \d\d\d-\d\d\d'
#-------------------Count-------------------
# phone_number_clear = r'\(?\d{3}\)?-?\s?\d{3}-\d{4}'
# print (re.findall(phone_number_clear,data))

# print(re.findall(r'\w*, \w+',data))

# words_count= r'\w{%s,}'%count

#----------------Set-----------------------
"""
re.IGNORECASE is equl  re.I
"""
# email = r'[-\w\d+.]+@[\w\d.-]+'
# emial_ = r'[-\w+.]+@[\w.-]+'
# print(re.findall(email,data))

# tree_house = r'\s([trehous]{9})\s'
# tree_house_edges = r'\b[trehous]{9}\b'
# print(re.findall(tree_house,data,re.I))

#----------------Negation------------------
"""
re.X is equal re.VERBOSE
"""
# print(re.findall(r'''
# 	\b@[\w\d.-]* #boundary & @...
# 	[^gov\t]+
# 	\b
# ''',data,re.VERBOSE | re.IGNORECASE))

# print(re.findall(r'''
# 	\b[\w-]+, 
# 	\s
# 	[-\w ]+   #explicit spaces 
# 	[^\n\t]+
# 	\b
# ''',data,re.X))

# string = '1234567890'
# re.findall(r'[^567]+',string)
# >>['1234', '890']

#-----------------Groups-------------------
# line = re.search(r'''
# 	^(?P<name>[-\w]*, \s [-\w ]+)\t #name
# 	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email
# 	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})\t #phone
# 	(?P<job>[\w\s]+,\s[\w\s.]+)\t? #job
# 	(?P<twitter>@[\w\d]+)?$ #twitter
# ''',data,re.X|re.MULTILINE)
# print(line)
# print(line.groupdict())

#emails
# string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
# Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
# McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
# Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

# contacts= re.search(r'''
# 	(?P<email>[-\w\d.+]+@[-\w\d.]+),\s #email
# 	(?P<phone>\d{3}-\d{3}-\d{4}) #phone
# ''',string,re.X|re.MULTILINE)

#---------------LOOPS & Compile-----------------------

# line = re.compile(r'''
# 	^(?P<name>(?P<last>[-\w]*), \s (?P<first>[-\w ]+))\t #name
# 	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email
# 	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})\t #phone
# 	(?P<job>[\w\s]+,\s[\w\s.]+)\t? #job
# 	(?P<twitter>@[\w\d]+)?$ #twitter
# ''',re.X|re.MULTILINE)

# print(re.search(line,data).groupdict())
# print(line.search(data).groupdict())

# for match in line.finditer(data):
	# print(match.group('name'))
	# print ('{first} {last} <{email}>'.format
	# 	(**match.groupdict()))
	# print(match.groupdict())
#example:

# string = '''Love, Kenneth: 20
# Chalkley, Andrew: 25
# McFarland, Dave: 10
# Kesten, Joy: 22
# Stewart Pinchback, Pinckney Benton: 18'''

# print(re.findall(r'''
# 	^(?P<last_name>[\w]*),\s  #name
# 	(?P<first_name>[\w ]*): #name
# 	(?P<score>[\d]*)$ #name
# ''',string,re.M|re.X))
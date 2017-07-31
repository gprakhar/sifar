#This script pull out 'n' number of random lines from a text file
#I am using this to get 1000 random lines from the coach_msg text file

import random
import csv
import re

filename = 'datasets/user-sent_quoted-coach_msg_postman_message_Jan18.csv'
number_of_questions = 10
all_lines = []
lines_1k = []

with open(filename) as f:
	reader = csv.reader(f)
	all_lines = list(reader)
#	print len(all_lines)
for i in range(number_of_questions):
	line = random.choice(all_lines)
	letters_only = re.sub("[^a-zA-Z0-9]",           # The pattern to search for
	" ",str(line))
	print letters_only
# ','.join(letters_only
	lines_1k.append(letters_only)

#'''
#	for line in all_lines:
#		if counter < number_of_questions:
#			print line
#			counter = counter + 1
#		else:
#			break
#		selected_line = random.choice(reader)
#		print selected_line
#'''

#for i in range(number_of_questions):
		#line = random.choice(open(filename).readlines())
		#lines_1k.append(line.strip())

#print "Lenght of list is %d" % (len(lines_1k))
#print "The list of lines:"

print lines_1k

for item in lines_1k:
	user_id, text = item
	print '%d,"%s"' % (user_id,text)	

#print ""'\n'.join(lines_1k)
#print lines_1k


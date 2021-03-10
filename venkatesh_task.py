# We have 4 test data. To test with different test data, Just change the replace 'data1' with relavant variabe name in LINE NO:59. 

data1 = """1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4
"""

data2 = """1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6
"""

data3 = """2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14"""

data4 = """3
4
sehwag tweet_id_2
sehwag tweet_id_4
sachin tweet_id_1
sachin tweet_id_3
7
sehwag tweet_id_10
sehwag tweet_id_11
kohli tweet_id_12
sachin tweet_id_13
sachin tweet_id_14
sachin tweet_id_1
sehwag tweet_id_4
5
sachin tweet_id_2
kohli tweet_id_41
kohli tweet_id_1
kohli tweet_id_3
sachin tweet_id_5"""


# created a variable to store the data seperately.
normalized_data = []
# Loop over rows of test data.
for row in data1.splitlines():
	if row.isdigit():
		normalized_data.append([])
	else:
		normalized_data[-1].append(row)


# To remove unwanted empty lists from List
[normalized_data.remove(ele) for ele in normalized_data if not ele]
# Join the content in such a way as sections.
normalized_data = ['\n'.join(i) for i in normalized_data]

# Loopver the sections 
for rec in normalized_data:
	# Empty dictionary to store sectional wise the Maximum tweets count.
	final_data = {}
	op = {row.split()[0]:rec.count(row.split()[0]) for row in rec.splitlines()}
	# Print the Name and Maximum count of tweets
	print('\n'.join(sorted(['{} {}'.format(k, v) for k, v in op.items() if v == max(op.values())])))





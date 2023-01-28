# finding missing value in the array 
# 1 to n in sequence 

li = [1,2,3,4,7,8,6]
len_x = len(li)
for i in range(len_x):
	count = i+1
	if li[i] != count:
		print("missing value in list {}".format(count))
		break



		




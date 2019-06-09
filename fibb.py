def fibb_recursive(x):
	"""Recursive fibbonachi, less code, very slow"""
	if x ==1 or x == 0:
		return 1
	else:
		return fibb_recursive(x-1)+fibb_recursive(x-2)


def fibb_list(x):
	"""Regular fibbonachi, more code, faster then recursive one"""
	arr = []
	k = 0
	for t in range(x):
		if t == 1 or t == 0 or t==2:
			k +=1
			arr.append(t)
		else:
			k = arr[t-2]+arr[t-1]
			arr.append(k)	
	return arr[x-1]


print([fibb_recursive(x) for x in range(10)])
print([fibb_list(x) for x in range(10)])				
			
def single(list):
	if list[0] in list[1:]:
		list[1:].remove(list[0])
		return single(list[1:])
	else:
		return list[0]

list = [1,2,3,4,5,6,1,2,3,4,5]
print single(list)
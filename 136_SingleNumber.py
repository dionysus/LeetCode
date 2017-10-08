def single(list):
	target = list.pop()
	if target in list:
		list.remove(target)
		return single(list)
	else:
		return target

list = [1,2,3,4,5,6,1,2,3,4,5]
print single(list)
#Given numRows, generate the first numRows of Pascal's triangle.

#For example, given numRows = 5,
#Return

#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]


def generate(numRows):

	list = []

	for row in range (1, numRows + 1):

		newRow = []

		for place in range (1, numRows + 1):
			if place == 1 or place == row:
				newRow.append(1)
			if place > 1 and place < row:
 				newRow.append(list[row-2][place-2]+list[row-2][place-1])
		list.append(newRow)
	return list

print generate(6)		

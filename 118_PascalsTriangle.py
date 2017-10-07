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

	for row in range (0, numRows):
		newRow = []
		for place in range (0, row+1):
			if place == 0 or place == row:
				newRow.append(1)
			if place > 0 and place < row:
 				newRow.append(list[row-1][place]+list[row-1][place-1])
		list.append(newRow)
	return list

print generate(8)		

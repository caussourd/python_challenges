
import math

# Note: this function could be transformed into a recursive function
def walk_around_square(first_index, last_index, grid, number):
	# drawing the upper horizontal line of the square (left to right)
	for j in range(first_index, last_index):
		grid[first_index].insert(j, number)
		number += 1

	# drawing the right vertical line of the square (top to bottom)
	for i in range (first_index + 1, last_index):
		# if it's the first call we create the list, otherwise we populate it
		if first_index == 0:
			grid.append([number])
		else:
			grid[i].insert(first_index, number)
		number += 1

	# drawing the bottom horizontal line of the square (right to left)
	for j in range(first_index, last_index - 1):
		grid[last_index - 1 ].insert(first_index, number)
		number += 1

	# drawing the left vertical line of the square (bottom to top)
	for i in range(last_index - 2, first_index, -1):
		grid[i].insert(first_index, number)
		number += 1

	return grid, number


def spiral(n):
	"""'walks' around an NxN square, starting at 1 and spiralling inwards to N^{2}"""
	
	# initialize variables	
	# grid is the matrix n x n
	grid = [[]]
	# number is N that is going to go up to N^{2}
	number = 1

	for i in range(int(math.ceil(n / 2)) + 1):
		grid, number = walk_around_square(i, n - i, grid, number)

	# generate the string
	digits_format = '%0'+str(len(str(n**2)))+'d'
	return '\n'.join([str(' '.join([(digits_format % item) for item in l])) for l in grid])


print spiral(10)

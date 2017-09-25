def climbStairs(n):
	"""
	:type n: int
	:rtype: int
	"""
	#fibonnaci sequence starting at 1, 2...

	#fib(n) = fib(n-1) + fib(n-2)

	sequence = []

	for i in range (0, n):
		if i == 0:
			steps = 1
		else:
			if i == 1:
				steps = 2
			else:
				steps = sequence[i-1] + sequence[i-2]
		sequence.append(steps)

	return sequence[-1]

print climbStairs(7)

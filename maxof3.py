def max_of_three(a,b,c):
	if a >= b:
		if b >= c:
			return a
		elif a >= c:
			return a
		else:
			return c
	elif b >= c:
		return b
	else:
		return c

def max_of_three1(a,b,c):
	if a >= b:
		if b >= c:
			print(a)
		elif a >= c:
			print(a)
		else:
			print(c)
	elif b >= c:
		print(b)
	else:
		print(c)

if __name__ == "__main__":
    import sys
    max_of_three1(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

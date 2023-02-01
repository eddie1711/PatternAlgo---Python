def printArrow(n,z):
	if z==0:
		dem = 0
		for i in range(n-1,-1,-1):
			print(dem*" "+"*"*(i+1))
			dem += 2
		dem -= 4
		for i in range(1,n):
			print(dem*" "+"*"*(i+1))
			dem -= 2
	else:
		dem = n*2-3
		for i in range(n-1,-1,-1):
			print(dem*" "+"*"*(i+1))
			dem -= 2
		dem += 4
		for i in range(1,n):
			print(dem*" "+"*"*(i+1))
			dem += 2
printArrow(5,0)

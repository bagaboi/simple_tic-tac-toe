import sys
print "the cpu wants to win or beat the opponent"
print "enter the following numbers for the respective places on the tic tac toe board"
print "1	2	3"
print "4	5	6"
print "7	8	9"
A="N"
B="N"
matrix=[['.','.','.'],['.','.','.'],['.','.','.']]
for x in xrange(len(matrix)):
	for y in xrange(len(matrix)):
		print matrix[x][y],
	print
while A!="Y" and B!="Y":
	if ('.' not in matrix[0]) and ('.' not in matrix[1]) and ('.' not in matrix[2]):
		for x in xrange(len(matrix)):
			for y in xrange(len(matrix)):
				print matrix[x][y],
			print
		print "the result is a draw"
		sys.exit()
	a=int(input("player A turn"))
	if a<4:
		if matrix[0][(a-1)%3]==".":
			matrix[0][(a-1)%3]='x'
		else:
			print "place already taken"
			continue
	elif a>3 and a<7:
		if matrix[1][(a-1)%3]==".":
			matrix[1][(a-1)%3]='x'
		else:
			print "place already taken"
			continue
	else:
		if matrix[2][(a-1)%3]==".":
			matrix[2][(a-1)%3]='x'
		else:
			print "place already taken"
			continue
	#CHECK HORIZONTAL
	if (matrix[0][0]=='x' and matrix[0][1]=='x' and matrix[0][2]=='x') or (matrix[1][0]=='x' and matrix[1][1]=='x' and matrix[1][2]=='x') or (matrix[2][0]=='x' and matrix[2][1]=='x' and matrix[2][2]=='x'):
		print "A wins"
		A="Y"
		continue
	#CHECK VERTICAL
	elif (matrix[0][0]=='x' and matrix[1][0]=='x' and matrix[2][0]=='x') or (matrix[0][1]=='x' and matrix[1][1]=='x' and matrix[2][1]=='x') or (matrix[0][2]=='x' and matrix[1][2]=='x' and matrix[2][2]=='x'):
		print "A wins"
		A="Y"
		continue
	#CHECK DIAGONAL
	elif (matrix[0][0]=='x' and matrix[1][1]=='x' and matrix[2][2]=='x') or (matrix[0][2]=='x' and matrix[1][1]=='x' and matrix[2][0]=='x'):
		print "A wins"
		A="Y"
		continue
	else:
		if ('.' not in matrix[0]) and ('.' not in matrix[1]) and ('.' not in matrix[2]):
			print "the result is a draw"
			for x in xrange(len(matrix)):
				for y in xrange(len(matrix)):
					print matrix[x][y],
				print
			sys.exit()
		for x in xrange(len(matrix)):
			for y in xrange(len(matrix)):
				print matrix[x][y],
			print
		#B's turn
		b=int(input("player B's turn"))
		if b<4:
			
			if matrix[0][(b-1)%3]==".":
				matrix[0][(b-1)%3]='o'
			else:
				print "place already taken"
				continue
		elif b<7:
			if matrix[1][(b-1)%3]==".":
				matrix[1][(b-1)%3]='o'
			else:
				print "place already taken"
				continue
		else:
			if matrix[2][(b-1)%3]==".":
				matrix[2][(b-1)%3]='o'
			else:
				print "place already taken"
				continue
		#CHECK HORIZONTAL
		if (matrix[0][0]=='o' and matrix[0][1]=='o' and matrix[0][2]=='o') or (matrix[1][0]=='o' and matrix[1][1]=='o' and matrix[1][2]=='o') or (matrix[2][0]=='o' and matrix[2][1]=='o' and matrix[2][2]=='o'):
			print "B wins"
			B="Y"
			continue
		#CHECK VERTICAL
		elif (matrix[0][0]=='o' and matrix[1][0]=='o' and matrix[2][0]=='o') or (matrix[0][1]=='o' and matrix[1][1]=='o' and matrix[2][1]=='o') or (matrix[0][2]=='o' and matrix[1][2]=='o' and matrix[2][2]=='o'):
			print "B wins"
			B="Y"
			continue
		#CHECK DIAGONAL
		elif (matrix[0][0]=='o' and matrix[1][1]=='o' and matrix[2][2]=='o') or (matrix[0][2]=='o' and matrix[1][1]=='o' and matrix[2][0]=='o'):
			print "B wins"
			B="Y"
			continue
	for x in xrange(len(matrix)):
		for y in xrange(len(matrix)):
			print matrix[x][y],
		print
for x in xrange(len(matrix)):
	for y in xrange(len(matrix)):
		print matrix[x][y],
	print
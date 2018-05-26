n = -1
m = -1
Xval = -1
rewardarr = [[0 for i in range(m)] for j in range(n)]		# Creating the board
move_dict = {0:'R', 1:'D', 2:'U', 3:'L'}

def get_utility(prev_utilityarr, oldx, oldy, newx, newy):

	if (newx >= n or newy >= m or newx < 0 or newy < 0):
		return prev_utilityarr[oldx][oldy]
	if (rewardarr[newx][newy] == 'W'):
		return prev_utilityarr[oldx][oldy]
	else:
		return prev_utilityarr[newx][newy]

def print_board(utilityarr):
	for i in xrange(n):
		for j in xrange(m):
			if (rewardarr[i][j] == 'W'):
				print "W",
				continue
			print round(utilityarr[i][j], 3),
		print
	# print "|     |0    |1    |2    |3    |"
	# print '| ---- | ---- | ---- | ---- |'
	# for i in xrange(n):
	# 	print "|**" + str(i) + "**   |",
	# 	for j in xrange(m):
	# 		if (rewardarr[i][j] == 'W'):
	# 			print '**W**   |',
	# 			continue
	# 		if (type(utilityarr[i][j]) == str):
	# 			print utilityarr[i][j], '   |',
	# 		else:
	# 			print round(utilityarr[i][j], 3), '   |',
	# 	print


if __name__ == "__main__":
	n,m = map(int, raw_input().split())							# Number of rows and cols
	#Xval = 15													# Team number
        #Xval = 4
	rewardarr = [[0 for i in range(m)] for j in range(n)]		# Creating the board
	utilityarr = [[0 for i in range(m)] for j in range(n)]		# Creating the board
	delta = Xval * 0.01

	for i in xrange(n):
		rowarr = [float(k) for k in raw_input().split()]
		for j in xrange(m):
			rewardarr[i][j] = rowarr[j]
			utilityarr[i][j] = rewardarr[i][j]


	E,W = map(int, raw_input().split())							# Number of end states and walls

	for i in xrange(E):
		xi, yi = map(int, raw_input().split())
		rewardarr[xi][yi] = 'T'

	for i in xrange(W):
		xi, yi = map(int, raw_input().split())
		rewardarr[xi][yi] = 'W'

	Sx, Sy = map(int, raw_input().split())	# Start state

	unit_reward = input()					# Unit step reward


	loopno = 1
	while(1):
		update = 0
		prev_utilityarr = [[utilityarr[i][j] for j in range(m)] for i in range(n)]
		policyarr = [[0 for j in range(m)] for i in range(n)]
		for i in xrange(n):
			for j in xrange(m):
				if (rewardarr[i][j] in ['T', 'W']):
					continue
				upscore = 0.8 * get_utility(prev_utilityarr,i,j,i-1,j) + 0.1*get_utility(prev_utilityarr,i,j,i,j-1) + 0.1*get_utility(prev_utilityarr,i,j,i,j+1)
				downscore = 0.8 * get_utility(prev_utilityarr,i,j,i+1,j) + 0.1*get_utility(prev_utilityarr,i,j,i,j-1) + 0.1*get_utility(prev_utilityarr,i,j,i,j+1)				
				leftscore = 0.8 * get_utility(prev_utilityarr,i,j,i,j-1) + 0.1*get_utility(prev_utilityarr,i,j,i-1,j) + 0.1*get_utility(prev_utilityarr,i,j,i+1,j)
				rightscore = 0.8 * get_utility(prev_utilityarr,i,j,i,j+1) + 0.1*get_utility(prev_utilityarr,i,j,i-1,j) + 0.1*get_utility(prev_utilityarr,i,j,i+1,j)
				max_score = max(upscore, leftscore, rightscore, downscore)
				if (max_score == rightscore):
					move = 0
				elif (max_score == downscore):
					move = 1
				elif (max_score == leftscore):
					move = 2
				elif (max_score == upscore):
					move = 3
				policyarr[i][j] = move_dict[move]
				new_utility = rewardarr[i][j] + max_score + unit_reward
				if (abs(new_utility-prev_utilityarr[i][j]) > abs(new_utility)*0.01):
					utilityarr[i][j] = new_utility
					update = 1
				utilityarr[i][j] = new_utility
                # print "### Policy for iteration", loopno
		# print_board(policyarr)
                # print
                # print "### Utility for iteration", loopno
		# print_board(utilityarr)
		# print
		if (update == 0):
			break
		loopno+=1

	print_board(utilityarr)


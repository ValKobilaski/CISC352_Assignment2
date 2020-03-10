import heapq

tempBoard = ['XXXXXXXXXX',
			 'X___XX_X_X',
			 'X_X__X___X',
			 'XSXX___X_X',
			 'X_X__X___X',
			 'X___XX_X_X',
			 'X_X__X_X_X',
			 'X__G_X___X',
			 'XXXXXXXXXX']
tempBoard = list(map(lambda u: [x for x in u], tempBoard))


def read_grid(file_name):
	inputGrid = []
	with open(file_name, 'r') as inputF:
		for line in inputF.read().splitlines():
			inputGrid.append(line)
	return inputGrid


def Greedy_Search(grid, diagonal):
	pass


def get_neighbors(graph, currentX, currentY, diagonals=False):
	neighbors = []
	# Left
	if currentX != 0 and graph[currentX-1][currentY] != 'X':
		neighbors.append((currentX-1, currentY))
	# Right
	if currentX != len(graph)-1 and graph[currentX+1][currentY] != 'X':
		neighbors.append((currentX+1, currentY))
	# Up
	if currentY != 0 and graph[currentX][currentY-1] != 'X':
		neighbors.append((currentX, currentY-1))
	# Down
	if currentY != len(graph)-1 and graph[currentX][currentY+1] != 'X':
		neighbors.append((currentX, currentY+1))
	if(diagonals):
		# top left
		if currentX != 0 and currentY != 0 and graph[currentX-1][currentY+1] != 'X':
			neighbors.append((currentX-1, currentY+1))
		# top right
		if currentX != len(graph)-1 and currentY != 0 and graph[currentX-1][currentY+1] != 'X':
			neighbors.append((currentX-1, currentY+1))
		# bottom left
		if currentX != 0 and currentY != len(graph) - 1 and graph[currentX-1][currentY-1] != 'X':
			neighbors.append((currentX-1, currentY-1))
		# bottom right
		if currentX != len(graph)-1 and currentY != len(graph)-1 and graph[currentX+1][currentY+1] != 'X':
			neighbors.append((currentX+1, currentY+1))
	return neighbors


def A_Star(grid, diagonal):

	q = []
	came_from = {}
	cost_so_far = {}

	for row in range(len(grid)):
		for col in range(len(grid[row])):
			if grid[row][col] == 'S':
				startX = row
				startY = col

	for row in range(len(grid)):
		for col in range(len(grid[row])):
			if grid[row][col] == 'G':
				goalX = row
				goalY = col

	start_node = ((chebyshev((startX, startY), (goalX, goalY)) if diagonal else manhattan(
		(startX, startY), (goalX, goalY))), startX, startY)
	came_from[start_node] = None
	cost_so_far[start_node] = 0

	heapq.heappush(q, start_node)

	while len(q) > 0:
		current = heapq.heappop(q)
		if grid[current[1]][current[2]] == 'G':
			break

		for node in get_neighbors(grid, current[1], current[2], diagonal):
			new_cost = cost_so_far[current] + 1
			if node not in cost_so_far:
				priority = new_cost + \
					(chebyshev(current, node) if diagonal else (
						manhattan((goalX, goalY), node)))
				cost_so_far[(priority, node[0], node[1])] = new_cost
				heapq.heappush(q, (priority, node[0], node[1]))
				came_from[(priority, node[0], node[1])] = current

	temp = came_from[current]
	route = [temp]
	while(came_from[temp] is not None):
		route.append(came_from[temp])
		grid[temp[1]] = grid[temp[1]][:temp[2]] + \
			'P' + grid[temp[1]][temp[2]+1:]
		temp = came_from[temp]
	grid[route[-1][1]] = grid[route[-1][1]][:route[-1][2]] + 'S' + grid[route[-1][1]][route[-1][2]+1:]
	return grid

# Takes two points (x1, y1), (x2, y2)
def manhattan(point_a, point_b):
	return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_a[1])


# Takes two points (x1, y1), (x2, y2)
def chebyshev(point_a, point_b):
	return max(abs(point_a[0] - point_b[0]), abs(point_a[1] - point_b[1]))


def main():
	grid = read_grid('pathfinding_a.txt')
	for i in A_Star(grid, False):
		print(i)

	print('\n')

	grid = read_grid('pathfinding_a.txt')
	for i in A_Star(grid, True):
		print(i)

	'''
	grid = read_grid("pathfinding_a.txt")
	Greedy_Search(grid, False)
	A_Star(grid, False)

	grid = read_grid("pathfinding_b.txt")
	Greedy_Search(grid, True)
	A_Star(grid, True)'''


main()

import heapq


def read_grid(file_name):
	inputGrid = []
	inputGrid.append([])
	with open(file_name, 'r') as inputF:
		boardCount=0
		for line in inputF.read().splitlines():
			inputGrid[boardCount].append(line)
			if line == "":
				boardCount+=1
				inputGrid.append([])
	return inputGrid


def Greedy_Search(grid, diagonal):
	return A_Star(grid,diagonal,True)


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


def A_Star(grid, diagonal, greedy=False):

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
	cost_so_far[(start_node[1], start_node[2])] = 0

	heapq.heappush(q, start_node)
	while len(q) > 0:
		#current is priority, x, y
		current = heapq.heappop(q)
		if grid[current[1]][current[2]] == 'G':
			break
		#Node is x and y without priority
		for node in get_neighbors(grid, current[1], current[2], diagonal):
			#If it's greedy this will just always be 0
			new_cost = cost_so_far[current[1], current[2]] + 1 if not greedy else 0
			if not node in cost_so_far:
				priority = new_cost + (chebyshev(node, (goalX, goalY)) if diagonal else (manhattan(node, (goalX, goalY))))
				cost_so_far[(node[0], node[1])] = new_cost
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
	grids_a = read_grid('pathfinding_a.txt')
	with open('pathfinding_a_out.txt', 'w+') as out:
		for grid in grids_a:
			#If statements just to make the printing more legible
			out.write("\nGreedy" if grids_a[0] != grid else 'Greedy')
			out.writelines(map((lambda x: "\n" + x), Greedy_Search(grid, False)))
			out.write("\nA*" if grids_a[0] != grid else 'A*')
			out.writelines(map((lambda x: "\n" + x), A_Star(grid, False)))
	grids_b = read_grid('pathfinding_b.txt')
	with open('pathfinding_b_out.txt', 'w+') as out:
		for grid in grids_b:
			#If statements just to make the printing more legible
			out.write("\nGreedy" if grids_b[0] != grid else 'Greedy')
			out.writelines(map((lambda x: x + "\n"), Greedy_Search(grid, True)))
			out.write("\nA*" if grids_b[0] != grid else 'A*')
			out.writelines(map((lambda x: x + "\n"), A_Star(grid, True)))


main()

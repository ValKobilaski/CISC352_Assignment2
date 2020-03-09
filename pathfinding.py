
def read_grid(file_name):
	with open(file_name, 'r') as inputF:
		for line in inputF:



def Greedy_Search(grid, diagonal):
	pass


def A_Star(grid, diagonal):
	pass


def main():
	grid = read_grid("pathfinding_a.txt")
	Greedy_Search(grid, False)
	A_Star(grid, False)
	
	grid = read_grid("pathfinding_b.txt")
	Greedy_Search(grid, True)
	A_Star(grid, True)

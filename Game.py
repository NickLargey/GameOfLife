import pprint
import time

ALIVE = 0
DEAD = '#'
pp = pprint.PrettyPrinter(indent=4)

class Grid:

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.grid = []
		for i in range(0, height):
			row = []
			for j in range(0, width):
				row.append(DEAD)
			self.grid.append(row)

	def get(self, row, col):
		self.check_valid_coordinates(row, col)
		return self.grid[row][col]

	def set_alive(self, row, col):
		self.check_valid_coordinates(row, col)
		self.grid[row][col] = ALIVE

	def set_dead(self, row, col):
		self.check_valid_coordinates(row, col)
		self.grid[row][col] = DEAD

	def check_valid_coordinates(self, row, col):
		if row >= self.width or col >= self.height or row < 0 or col < 0:
			raise Error('Index out of bounds!')

	def num_live_neighbors(self, row, col):
		live_neighbors = 0
		for i in range(row-1, row+2):
			for j in range(col-1, col+2):
				if i == row and j == col:
					continue
				if self.get(i % self.width, j % self.height) == ALIVE:
					live_neighbors += 1	
		return live_neighbors


class GameOfLife:

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.current_grid = Grid(width, height)
		self.next_grid = Grid(width, height)
		self.set_start_board()

	def set_blinker(self):
		x = round(self.width/2)
		y = round(self.height/2)
		self.current_grid.set_alive(x,y)
		self.current_grid.set_alive(x+1,y)
		self.current_grid.set_alive(x-1,y)
	
	def set_glider(self):
		x = round(self.width/2)
		y = round(self.height/2)
		self.current_grid.set_dead(x,y)
		self.current_grid.set_alive(x+1,y)
		self.current_grid.set_alive(x-1,y+1)
		self.current_grid.set_alive(x,y+1)
		self.current_grid.set_alive(x+1,y+1)
		self.current_grid.set_alive(x,y-1)

	def set_start_board(self):
		self.set_glider()

	def update_cell(self, row, col):
		state = self.current_grid.get(row,col)
		live_neighbors = self.current_grid.num_live_neighbors(row,col)

		if state == ALIVE and live_neighbors < 2:
			self.next_grid.set_dead(row,col)
		elif state == ALIVE and (live_neighbors == 2 or live_neighbors ==3):
			self.next_grid.set_alive(row,col)
		elif state == ALIVE and live_neighbors > 3:
			self.next_grid.set_dead(row, col)
		elif state == DEAD and live_neighbors == 3:
			self.next_grid.set_alive(row, col)
		else:
			self.next_grid.set_dead(row, col) 

	def update(self):
		for i in range(self.width):
			for j in range(self.height):
				self.update_cell(i,j)

	def play(self):
		iterations = 100
		self.print_board()
		for i in range(iterations):
			time.sleep(0.5)
			self.update()
			self.swap_grids()
			self.print_board()

	def swap_grids(self):
		temp = self.current_grid
		self.current_grid = self.next_grid
		self.next_grid = temp

	def print_board(self):
		print('-' * 80)
		pp.pprint(self.current_grid.grid)

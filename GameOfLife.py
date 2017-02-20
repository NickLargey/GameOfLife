import pygame


ALIVE = 1
DEAD = 0

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
        if col >= self.width or row >= self.height or row < 0 or col < 0:
            raise Error('Index out of bounds!')

    def num_live_neighbors(self, row, col):
        live_neighbors = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i == row and j == col:
                    continue
                if self.get(i % self.height, j % self.width) == ALIVE:
                    live_neighbors += 1 
        return live_neighbors


class GameOfLife:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.current_grid = Grid(width, height)
        self.next_grid = Grid(width, height)

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
                self.update_cell(j,i)

    def step(self):
        self.update()
        self.swap_grids()

    def swap_grids(self):
        temp = self.current_grid
        self.current_grid = self.next_grid
        self.next_grid = temp


black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

rows = 115
columns = 165
WIDTH = 5
HEIGHT = 5

MARGIN = 1

pygame.init() 

size = (991, 691)
screen=pygame.display.set_mode(size)

pygame.display.set_caption('Game Of Life')

done = False
playing = False

clock = pygame.time.Clock()

game_of_life = GameOfLife(rows, columns)
print(len(game_of_life.current_grid.grid), len(game_of_life.current_grid.grid[0]))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            game_of_life.current_grid.set_alive(column, row)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            playing = not playing

    screen.fill(black)

    for row in range(rows):
        for column in range(columns):
            color = gray
            if game_of_life.current_grid.get(column, row) == ALIVE:
                color = white
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])

    if playing:
        game_of_life.step()

    clock.tick(10)

    pygame.display.flip()

pygame.quit()







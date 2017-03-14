import pygame

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

width = 5
height = 5

margin = 1

grid = [[0 for x in range(25)] for y in range(25)]

grid[1][5] = 1

pygame.init() 

size = (700, 500)
screen=pygame.display.set_mode(size)

pygame.display.set_caption('Game Of Life')

done = False

clock = pygame.time.Clock()

while not done:
	for event.type in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			column = pos[0] // (width + margin)
			row = pos[1] // (height + margin)
			grid[row][column] = 1
			print('Click ', pos, 'Grid Coordinates: ', row, column)

	screen.fill(gray)

	for row in range(25):
		for column in range(25):
			color = black
			if grid[row][column] == 1:
				color = [white]
			pygame.draw.rect(screen,
							 color,
							 [(margin + width) * column + margin,
							 (margin + height) * row + margin,
							 width,
							 height])

	clock.tick(60)

	pygame.display.flip()

pygame.quit()






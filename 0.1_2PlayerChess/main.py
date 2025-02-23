import pygame
import os
from Board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.update()

def checkmate(color):
	# Dim the screen
	dim_screen = pygame.Surface(WINDOW_SIZE)
	dim_screen.set_alpha(128)
	screen.blit(dim_screen, (0, 0))

	# Display the message
	font = pygame.font.Font(None, 36)
	text = font.render(f"Checkmate. {color} Wins!", True, (255, 255, 255))
	text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
	screen.blit(text, text_rect)
	pygame.display.update()

if __name__ == '__main__':
	running = True
	pygame.display.set_caption(os.getcwd().split('/')[-1])
	while running:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			# Quit the game if the user presses the close button
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: 
       			# If the mouse is clicked
				if event.button == 1:
					board.handle_click(mx, my)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_e:
					board.developer_debug()
		if board.in_checkmate('black'): # If black is in checkmate
			draw(screen)
			checkmate('White')
			pygame.time.wait(8000)
			running = False
		elif board.in_checkmate('white'): # If white is in checkmate
			draw(screen)
			checkmate('Black')
			pygame.time.wait(8000)
			running = False
		# Draw the board
		draw(screen)
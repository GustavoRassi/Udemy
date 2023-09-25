import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600

# Create a window
screen = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Pygame Window")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game here

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black

    # Draw game elements here

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

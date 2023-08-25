import pygame
import random

# Initialize Pygame
pygame.init()

# Define the window size
window_width = 800
window_height = 600

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Set the window title
pygame.display.set_caption("Pac-Man")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Define the Pac-Man character
pacman_size = 30
pacman_x = 400
pacman_y = 300
pacman_speed = 1

# Define the enemy character
enemy_size = 20
enemy_x = random.randint(0, window_width - enemy_size)
enemy_y = random.randint(0, window_height - enemy_size)
enemy_speed = 0.05

# Define the pellets
pellet_size = 10
pellet_spacing = 50
pellet_margin = 10
pellet_list = []
for x in range(pellet_margin, window_width - pellet_size, pellet_spacing):
    for y in range(pellet_margin, window_height - pellet_size, pellet_spacing):
        pellet_list.append(pygame.Rect(x, y, pellet_size, pellet_size))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the Pac-Man character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pacman_x > 0:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT] and pacman_x < window_width - pacman_size:
        pacman_x += pacman_speed
    if keys[pygame.K_UP] and pacman_y > 0:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN] and pacman_y < window_height - pacman_size:
        pacman_y += pacman_speed
    
    # Check for collisions with pellets
    for pellet in pellet_list:
        if pellet.colliderect(pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)):
            pellet_list.remove(pellet)
    
    # Move the enemy character
    if enemy_x < pacman_x:
        enemy_x += enemy_speed
    elif enemy_x > pacman_x:
        enemy_x -= enemy_speed
    if enemy_y < pacman_y:
        enemy_y += enemy_speed
    elif enemy_y > pacman_y:
        enemy_y -= enemy_speed
    
    # Check for collisions with the enemy
    if pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size).colliderect(pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)):
        running = False
    
    # Draw the screen
    screen.fill(BLACK)
    for pellet in pellet_list:
        pygame.draw.rect(screen, WHITE, pellet)
    pygame.draw.circle(screen, YELLOW, (pacman_x + pacman_size // 2, pacman_y + pacman_size // 2), pacman_size // 2)
    pygame.draw.rect(screen, WHITE, pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.display.update()

# Quit Pygame
pygame.quit()

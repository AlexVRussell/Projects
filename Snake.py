import sys
import pygame
import time
import random
# Initialize pygame
pygame.init()

# Set the size of the game board and the size of each snake segment
BOARD_WIDTH = 500
BOARD_HEIGHT = 500
SEGMENT_SIZE = 25

# Set the initial position of the snake and its direction
snake_x = 0
snake_y = 0
snake_direction = (1, 0)  # 1 = right, -1 = left, 2 = down, -2 = up
score = 0
gameOver = "GAME OVER"


# Create a list to store the segments of the snake's body
snake_body = []
snake_length = 5

# Create the game board
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))


# Create the snake's head
snake_head = pygame.Rect((snake_x, snake_y), (SEGMENT_SIZE, SEGMENT_SIZE))
snake_body.append(snake_head)

# Create the food
food = pygame.Rect((random.randint(0, BOARD_WIDTH // SEGMENT_SIZE - 1) * SEGMENT_SIZE,
                   random.randint(0, BOARD_HEIGHT // SEGMENT_SIZE - 1) * SEGMENT_SIZE),
                   (SEGMENT_SIZE, SEGMENT_SIZE))

pygame.display.set_caption('Snake Game')
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)

    # Move the snake
    snake_x += snake_direction[0]
    snake_y += snake_direction[1]
    snake_head = pygame.Rect((snake_x, snake_y), (SEGMENT_SIZE, SEGMENT_SIZE))



    if len(snake_body) > snake_length:
        snake_body.pop(0)

    # Check for collision with food
    # Check for collision with food
    if snake_head.colliderect(food):
        # Move the food to a new random location
        food = pygame.Rect((random.randint(0, BOARD_WIDTH // SEGMENT_SIZE - 1) * SEGMENT_SIZE,
                            random.randint(0, BOARD_HEIGHT // SEGMENT_SIZE - 1) * SEGMENT_SIZE),
                           (SEGMENT_SIZE, SEGMENT_SIZE))
        snake_length += 25
        score += 1

        # Add a new segment to the snake's body
        snake_body.append(snake_head)
    else:
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            snake_body.pop(0)
    # Move the snake
    snake_x += snake_direction[0]
    snake_y += snake_direction[1]



    # Check if the snake has hit the edge of the board
    if snake_x < 0 or snake_x >= BOARD_WIDTH or snake_y < 0 or snake_y >= BOARD_HEIGHT:
        print(gameOver)
        print("Score:", score)
        pygame.quit()
        sys.exit()

    snake_body.append(snake_head)

    # Clear the screen
    screen.fill((0, 0, 0))
    time.sleep(0.01)

    # Draw the snake and food
    for segment in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), segment)
    pygame.draw.rect(screen, (255, 0, 0), food)

    # Update the display
    pygame.display.update()


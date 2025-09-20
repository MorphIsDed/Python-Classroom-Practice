# Snake Game in Python using Pygame
# A simple, classic implementation of the Snake game.

import pygame
import sys
import random

# --- Initialization ---
# Initialize all the imported pygame modules
pygame.init()

# --- Game Configuration ---
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0) # Snake color
RED = (255, 0, 0)   # Food color
GRAY = (40, 40, 40) # Grid color

# Game grid and speed settings
BLOCK_SIZE = 20 # Size of the snake's segments and food
SNAKE_SPEED = 15 # The game's frame rate (controls snake speed)

# --- Game Window Setup ---
# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Classic Python Snake')

# --- Game Clock ---
# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# --- Font Setup ---
# Set up fonts for displaying the score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# --- Helper Functions ---

def show_score(score):
    """
    Renders and displays the current score on the screen.
    """
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])


def draw_snake(snake_body):
    """
    Draws all the segments of the snake.
    """
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])


def draw_grid():
    """
    Draws a grid on the background for better visibility.
    """
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))


def display_message(msg, color):
    """
    Displays a message in the center of the screen.
    """
    mesg = font_style.render(msg, True, color)
    # Center the message text on the screen
    mesg_rect = mesg.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(mesg, mesg_rect)


def game_loop():
    """
    The main function that runs the game logic.
    """
    game_over = False
    game_close = False

    # --- Initial Snake State ---
    # Starting position of the snake (center of the screen)
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    # Variables to track the change in position
    x1_change = 0
    y1_change = 0

    # The snake's body, starting with one block
    snake_body = []
    snake_length = 1

    # --- Initial Food State ---
    # Generate the first piece of food at a random position
    # The position is snapped to the grid defined by BLOCK_SIZE
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # --- Main Game Loop ---
    while not game_over:

        # --- Game Over Screen Loop ---
        while game_close:
            screen.fill(BLACK)
            display_message("You Lost! Press C-Play Again or Q-Quit", RED)
            show_score(snake_length - 1)
            pygame.display.update()

            # Check for user input to quit or restart
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # Restart the game by calling the main loop again

        # --- Event Handling ---
        # Process all user inputs (key presses, window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True # Exit the main loop if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Prevent the snake from reversing on itself
                    if x1_change == 0:
                        x1_change = -BLOCK_SIZE
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == 0:
                        x1_change = BLOCK_SIZE
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == 0:
                        y1_change = -BLOCK_SIZE
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change == 0:
                        y1_change = BLOCK_SIZE
                        x1_change = 0

        # --- Collision Detection (Boundaries) ---
        # Check if the snake has hit the screen edges
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        # --- Update Snake Position ---
        x1 += x1_change
        y1 += y1_change

        # --- Drawing ---
        screen.fill(BLACK)
        draw_grid()
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # --- Update Snake Body ---
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)

        # If the snake's body exceeds its current length, remove the oldest segment
        if len(snake_body) > snake_length:
            del snake_body[0]

        # --- Collision Detection (Self) ---
        # Check if the snake's head has collided with its body
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        # --- Draw Game Elements ---
        draw_snake(snake_body)
        show_score(snake_length - 1)

        # --- Update Display ---
        pygame.display.update()

        # --- Food Consumption ---
        # Check if the snake's head is at the same position as the food
        if x1 == food_x and y1 == food_y:
            # Generate new food at a random position
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1 # Increase the snake's length

        # --- Control Game Speed ---
        clock.tick(SNAKE_SPEED)

    # --- Uninitialize and Quit ---
    pygame.quit()
    sys.exit()

# --- Start the Game ---
if __name__ == "__main__":
    game_loop()
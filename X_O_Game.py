import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("X O Game - Pygame")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Board
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
font = pygame.font.Font(None, 80)

def draw_board():
    screen.fill(WHITE)

    # Grid lines
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)

    # Draw X and O
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * 100 + 30, row * 100 + 10))

def check_winner(player):
    # Rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True

    # Columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"

# Game Loop
running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // 100
            col = x // 100

            if board[row][col] == "":
                board[row][col] = current_player

                if check_winner(current_player):
                    print(f"{current_player} WINS!")
                    pygame.time.delay(1000)
                    reset_game()

                current_player = "O" if current_player == "X" else "X"

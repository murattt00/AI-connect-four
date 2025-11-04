import game_rules as game
import ai as ai
import math
import pygame
import sys

# --- Oyun Mantığı Sabitleri ---
PLAYER_PIECE = 1
AI_PIECE = 2

# --- Renk Sabitleri ---
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

# --- Pygame Başlatma ---
pygame.init()

width = game.Column_count * SQUARESIZE
height = (game.Row_count + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect Four AI")
myfont = pygame.font.SysFont("monospace", 75)

def draw_board(board):
    for c in range(game.Column_count):
        for r in range(game.Row_count):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

def draw_pieces(board):
    for c in range(game.Column_count):
        for r in range(game.Row_count):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


Ai_depth = 2
board = game.create_board()
game_over = False

turn = 1 

draw_board(board)
draw_pieces(board)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
        
            if turn % 2 != 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            
       
            if turn % 2 != 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if game.is_valid_location(board, col):
                    row = game.get_next_open_row(board, col)
                    game.drop_piece(board, row, col, PLAYER_PIECE)

                    if game.check_win(board, PLAYER_PIECE):
                        label = myfont.render("You Win!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
                    
                    turn += 1
                    draw_pieces(board)


    if turn % 2 == 0 and not game_over:
        col, minimax_score = ai.minimax(board, Ai_depth, -math.inf, math.inf, True)

        if game.is_valid_location(board, col):
            pygame.time.wait(500)
            row = game.get_next_open_row(board, col)
            game.drop_piece(board, row, col, AI_PIECE)

            if game.check_win(board, AI_PIECE):
                label = myfont.render("AI Wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

            draw_pieces(board)
            turn += 1

    if not game_over and len(game.get_valid_locations(board)) == 0:
        label = myfont.render("It's a Draw!", 1, BLUE)
        screen.blit(label, (40, 10))
        game_over = True

    if game_over:
        pygame.time.wait(3000)
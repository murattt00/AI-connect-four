# Connect Four with AI

This project is a classic Connect Four game implemented in Python with a graphical user interface built using `pygame`. You can play against a challenging AI opponent that uses the Minimax algorithm to think ahead and make strategic moves.

## Features

-   **Graphical Interface:** A clean and simple game board rendered with `pygame`.
-   **Intelligent AI Opponent:** Play against a computer that won't make random moves. The AI analyzes the board to find the best possible move.
-   **Interactive Controls:** Use your mouse to select a column and drop your piece.

## The AI Engine: Minimax

The artificial intelligence in this game is powered by the **Minimax algorithm**, a classic decision-making algorithm used in two-player turn-based games.

### How it Works:
1.  **Game Tree:** The AI simulates future moves by building a tree of all possible game states.
2.  **Scoring:** It evaluates the board at the end of its simulation depth, assigning a score to each outcome. A winning position gets a high score, a losing position gets a low score, and strategic advantages (like having three pieces in a row) get intermediate scores.
3.  **Maximizing and Minimizing:** The algorithm assumes that you (the player) will always make the best possible move for yourself.
    -   The **Maximizer** (the AI) tries to choose a move that leads to the highest possible score.
    -   The **Minimizer** (the player) is assumed to choose a move that leads to the lowest possible score for the AI.
4.  **Alpha-Beta Pruning:** To speed up the decision-making process, the algorithm uses an optimization called Alpha-Beta Pruning. This allows it to "prune" or ignore branches of the game tree that are guaranteed to be worse than a move it has already found.

This process allows the AI to "look ahead" several moves and choose the one that is most likely to lead to a win or block the player from winning.

## How to Play

1.  Run the `main.py` file.
2.  A game window will appear. The board is blue, empty slots are white.
3.  You play as the **Red** pieces, and the AI plays as the **Yellow** pieces.
4.  When it's your turn, move your mouse to the top of the screen to see where your piece will drop.
5.  Click on a column to drop your piece.
6.  The first player to get four of their pieces in a row (horizontally, vertically, or diagonally) wins!

## Setup and Installation

To run this game, you need to have Python and `pygame` installed.

1.  **Install Python:** If you don't have it, download it from [python.org](https://www.python.org/).
2.  **Install Pygame:** Open your terminal or command prompt and run the following command:
    ```bash
    pip install pygame
    ```

## How to Run the Game

Navigate to the project directory in your terminal and run the main file:

```bash
python main.py
```
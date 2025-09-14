# Connect 4 – Python CLI Game

A command-line version of Connect 4, implemented in Python.
Supports Player vs AI, Player vs Player, and even AI vs AI.

The project is fully containerized with Docker, includes BDD tests with Behave, and is ready to run locally or in CI/CD pipelines.

## Features

Game modes:

 Player vs AI

 Player vs Player

 AI vs AI

AI powered by Minimax algorithm with Alpha-Beta pruning.

Save & load game state using pickle.

ASCII-based board visualization.

Comprehensive BDD testing with Behave + pexpect.

Docker support for easy setup and execution.

## Installation & Setup
Run locally

Requirements:

Python 3.9+

## Play the Game
At startup, select the game mode:

- Game mode player vs ai = 1
- Game mode player vs player = 2
- Game mode ai vs ai = 3

## Save & Load Games

During gameplay:
- Type close to save the current game and exit.

At startup:
- Enter y to load the last saved game.

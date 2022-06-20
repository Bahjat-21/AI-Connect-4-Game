
from email.mime import image
from secrets import choice
from behave import when, then, given
import pexpect

@given("I start the game")
def step_impl(context):
    image_name = "connect4:latest"
    context.proc = pexpect.spawn("docker-compose run connect4")

@when("I choose game mode: {game_mode}")
def step_impl(context,game_mode):
    context.proc.expect("Please choose a game mode: ")
    context.proc.sendline(game_mode)

    
@when("The Instructions appear")
def step_impl(context):
    context.proc.expect( "Game mode player vs ai = 1")

# @when("I choose {player} as my player")
# def step_impl(context,player):
#     context.proc.expect("X or O:")
#     context.proc.sendline(player)


@when("Load old game: {choice}")
def step_impl(context, choice):
    context.proc.expect('Load old game: ')
    context.proc.sendline(choice)

@when("Board and game name appears")
def step_impl(context):
    context.proc.expect("    #######################")

@when("Player {player} enters column {pos}")
def step_impl(context,pos, player):
    context.proc.expect(f"Player {player} enter your move: ")
    context.proc.sendline(pos)

@when("Player {player} enters {close}")
def step_impl(context,close, player):
    context.proc.expect(f"Player {player} enter your move: ")
    context.proc.sendline(close)

@when("AI 1 goes first")
def step_impl(context):
    context.proc.expect("AI 1")

@then("Player {player} wins")
def step_impl(context, player):
    context.proc.expect(f"{player} wins!")

@then("Its a draw")
def step_impl(context):
    context.proc.expect("Its a draw")


@then("Column full")
def step_impl(context):
    context.proc.expect("Column full")

@then("game closed")
def step_impl(context):
    context.proc.expect("Game saved")

@then("old game loaded")
def step_impl(context):
    context.proc.expect("    #######################")

@then("input to large error")
def step_impl(context):
    context.proc.expect("Player X enter your move:")

@then("AI wins")
def step_impl(context):
    context.proc.expect("AI wins!")

@then("AI 1 wins")
def step_impl(context):
    context.proc.expect("AI 1 wins!")

@then("AI 2 wins")
def step_impl(context):
    context.proc.expect("AI 2 wins!")
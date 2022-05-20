
from behave import when, then, given
import pexpect

@given("I start the game")
def step_impl(context):
    image_name = "connect4:latest"
    context.proc = pexpect.spawn(f"docker run -i --rm {image_name}")

@when("The board and the game name appears")
def step_impl(context):
    context.proc.expect( "###############################")

@when("I choose {player} as my player")
def step_impl(context,player):
    context.proc.expect("X oder O:")
    context.proc.sendline(player)

@when("I enter column {pos}")
def step_impl(context,pos):
    context.proc.expect("Your move:")
    context.proc.sendline(pos)

@then("I check the row a")
def step_impl(context):
    context.proc.expect("a | X | X |   |   |   |   |   |")




from behave import when, then, given
import pexpect

@given("I start the program")
def step_impl(context):
    image_name = "connect4:latest"
    context.proc = pexpect.spawn(f"docker run -i --rm {image_name}")

@when("The board and game name appears")
def step_impl(context):
    context.proc.expect( "###############################\n"
                         "######### CONNECT 4 ###########\n"
                         "###############################")

@when("I choose {player}")
def step_impl(context,player):
    context.proc.expect("X oder O:")
    context.proc.sendline(player)

@when("I enter {pos}")
def step_impl(context,pos):
    context.proc.expect("Your move:")
    context.proc.sendline(pos)

@then("I need to enter next move")
def step_impl(context):
    context.proc.expect("Your move")



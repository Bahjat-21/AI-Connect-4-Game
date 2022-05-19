from behave import given, when, then
import pexpect
import os

@given("I start the program")
def step_impl(context):
    try:
        image_name = os.environ["C4_CONTAINWE_IMAGE"]
    except KeyError:
        image_name = "connect-4:latest"
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

@when("I enter my {pos}")
def step_impl(context,pos):
    context.proc.expect("Your move:")
    context.proc.sendline(pos)

@then("I see my {pos} marked on the board")
def step_impl(context, result):
    context.proc.expect("Your move")



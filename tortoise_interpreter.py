"""Implementation of tortoise-language."""
from argument_parsing import ArgumentParser

def main_tortoise(program, filename, verbose, renderer, print_to_screen=print):
    """Main function that interprets a tortoise program."""
    program = sanitize_program(program)
    

    if verbose:
        print_to_screen(f"Executing {filename}, {len(program)} commands found")

    if renderer == 'english' or renderer is None:
        command_to_parse = ArgumentParser(program)
        commands = command_to_parse.english()

        for command in commands:
            print_to_screen(command)


def sanitize_program(program):
    """Get tortoise program ready for interpretation.

    There are unnecessary characters like spaces and comments which we want to get rid of.
    If a command has two parts, the second element of the list will be an empty string.
    Remove this element. Then remove all elements after the first empty string in each list.
    These were the comments at the end of each command."""
    for command in program:
        if len(command) > 1:
            command.pop(1)
            if len(command) > 2:
                del command[command.index(" ") :]
    return program

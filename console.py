#!/usr/bin/python3
"""
This module defimes a command interpreter that is goint to
be used to interact with our end points.

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Implements commands used to operate methods of the classes.

    """
    intro = "Welcome to HBNB"
    prompt = "(hbnb) "

    command_help = {
            'quit': 'Quit command to exit the program.',
            'EOF': 'EOF command to exit the program.',
            'help': 'Provides info about other commands.'
    }

    def do_quit(self, arg):
        """
        Quit command exits the program.

        """
        print("Goodbye...")
        return True

    def do_EOF(self, arg):
        """
        EOF command exits the program.

        """
        print("Goodbye...")
        return True

    def do_help(self, arg):
        """
        Gets help for a command.

        """
        if arg:
            if arg in self.command_help:
                print(self.command_help[arg])
                print("")
            else:
                print("Command not found: {}", arg)
        else:
            print("")
            print("Documented commands (type help <topic>):")
            print("========================================")
            for cmd in self.command_help.keys():
                print(f"{cmd}", end="  ")
            print("")
            print("")

    def emptyline(self):
        """
        Should not execute anything when Enter is pressed.

        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

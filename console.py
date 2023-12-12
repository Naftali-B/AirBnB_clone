#!/usr/bin/env python3
"""
Console module.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        """
        Print help message for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D) to exit the program.
        """
        print()
        return True

    def help_EOF(self):
        """
        Print help message for the EOF command.
        """
        print("EOF command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()


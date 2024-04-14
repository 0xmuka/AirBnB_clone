#!/usr/bin/python3
""" Console Module """

import cmd


class HBNBCommand (cmd.Cmd):
    """
    HBNBCommand
    """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """
        To quit the program with hema

        """
        exit()

    def do_quit(self, line):
        """
        to quit from program
        """
        print("Good Bye")
        print()

    def do_EOF(self, line):
        """
        End of file

        """
        print()
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

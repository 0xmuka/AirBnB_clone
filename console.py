#!/usr/bin/python3
""" Console Module """

import cmd


class HBNBCommand (cmd.Cmd):
    """HBNBCommand"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program
        
        """

        exit()

    def do_EOF(self, line):
        """End of file"""

        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

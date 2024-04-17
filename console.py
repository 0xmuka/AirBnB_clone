#!/usr/bin/python3
""" Console Module """
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand (cmd.Cmd):
    """HBNBCommand"""

    prompt = "(hbnb)"

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            cls = storage.classes()[arg]()
            cls.save()
            print(cls.id)
    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, line):
        """print new line and exit"""

        print()
        return True

    def emptyline(self):
        """empty line don't care"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

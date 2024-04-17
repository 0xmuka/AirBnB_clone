#!/usr/bin/python3
""" Console Module """
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand (cmd.Cmd):
    """HBNBCommand"""

    prompt = "(hbnb)"

    def do_create(self, arg):
        """create new object"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            cls = storage.classes()[arg]()
            cls.save()
            print(cls.id)

    def do_show(self, arg):
        """show object with id"""
        # to handling cmd because take one parmeter all right?
        args = arg.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in storage.classes():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self,arg):
        """delete instance based on the class name and id"""
        # to handling cmd because take one parmeter all right?
        args = arg.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in storage.classes():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

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

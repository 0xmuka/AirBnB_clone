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

    def do_destroy(self, arg):
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

    def do_all(self, arg):
        """Show all objects"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in storage.classes():
            print("** class doesn't exist **")
            return

        objects = storage.all()
        filtered_objects = [str(obj) for obj in objects.values()
                            if obj.__class__.__name__ == arg]

        if filtered_objects:
            print("\n".join(filtered_objects))
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Update an instance"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        attr_name = args[2]
        attr_value = ' '.join(args[3:])

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = class_name + "." + obj_id
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        if attr_name in ["id", "created_at", "updated_at"]:
            print("""** cannot update attribute name:
                  id, created_at, or updated_at **""")
            return

        obj = objs[key]

        setattr(obj, attr_name, attr_value)

        obj.save()

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

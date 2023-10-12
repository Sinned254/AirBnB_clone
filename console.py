#!/usr/bin/python3
""" modlu contaisn class HBNBCommand(cmd.Cmd)
entry point to the interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """implements quit, EOF, to end the program and help,
    and custom prompt (hbnb)"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            all_objs = storage.all()
            key = "{}.{}".format(class_name, obj_id)
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            all_objs = storage.all()
            key = "{}.{}".format(class_name, obj_id)
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representations of all instances"""
        args = arg.split()
        all_objs = storage.all()
        if not arg or args[0] in ["BaseModel", "User", "Place",
                                  "State", "City", "Amenity", "Review"]:
            print([str(all_objs[key]) for key in all_objs])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            all_objs = storage.all()
            key = "{}.{}".format(class_name, obj_id)
            if key in all_objs:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    obj = all_objs[key]
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
            else:
                print("** no instance found **")
        except Exception:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Command to Exit program"""
        return True

    def do_EOF(self, arg):
        """ctrl D to exit program - EOF"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

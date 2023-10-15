#!/usr/bin/python3
""" modlu contaisn class HBNBCommand(cmd.Cmd)
entry point to the interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
SUPPORTED_CLASSES = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """implements quit, EOF, to end the program and help,
    and custom prompt (hbnb)"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file"""
        if not arg:
            print("** class name missing **")
            return
        class_name, *rest = arg.split(" ")
        
        if class_name not in SUPPORTED_CLASSES:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in SUPPORTED_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in SUPPORTED_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print string representations of all instances"""
        args = arg.split()
        all_objs = storage.all()
        if not arg:
            print([str(all_objs[key]) for key in all_objs])
        elif args[0] not in SUPPORTED_CLASSES:
            print("** class doesn't exist **")
        else:
            print([str(all_objs[key]) for key in
                  all_objs if key.startswith(args[0])])

    def do_update(self, arg):
        """Update an instance based on the class name and id by
        adding  or updating attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in SUPPORTED_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objs:
                obj = objs[key]
                setattr(obj, args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Command to Exit program"""
        return True

    def do_EOF(self, arg):
        """ctrl D to exit program - EOF"""
        return True

    def emptyline(self):
        pass

    """def do_destroyall(self, arg):
        
        Deletes all instances of a class
        Usage: destroyall <class name>
        
        if not arg:
            print("** class name missing **")
            return

        class_name, *rest = arg.split(" ")
        if class_name not in SUPPORTED_CLASSES:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            for obj_id, obj in list(instances.items()):
                if obj.__class__.__name__ == class_name:
                    del instances[obj_id]
                    storage.save()"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()

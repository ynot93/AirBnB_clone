#!/usr/bin/python3
"""
This module defimes a command interpreter that is goint to
be used to interact with our end points.

"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Implements commands used to operate methods of the classes.

    """
    prompt = "(hbnb) "

    command_help = {
            'quit': 'Quit command to exit the program.',
            'EOF': 'EOF command to exit the program.',
            'help': 'Provides info about other commands.'
    }

    def do_quit(self, arg):
        """Quit command exits the program

        """
        return True

    def do_EOF(self, arg):
        """EOF command exits the program.

        """
        return True

    def do_help(self, arg):
        """Gets help for a command.

        """
        if arg:
            super().do_help(arg)
        else:
            super().do_help(None)

    def emptyline(self):
        """Should not execute anything when Enter is pressed.

        """
        pass

    def do_create(self, arg):
        """Creates a new instance, saves it and prints the ID.

        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        instance = eval(class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance.

        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes instance and saves the changes to the JSON file.

        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances.

        """
        args = shlex.split(arg)
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        instances = storage.all().values()
        if args:
            instances = [
                    item for item in instances if isinstance(
                        item, eval(args[0]))
            ]
        print([str(item) for item in instances])

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute.

        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        storage.save()

    def default(self, arg):
        """Handle commands in the form <class name>.<method>()

        """
        args = arg.split('.')
        if len(args) >= 2:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            command = args[1]

            if command == 'all()':
                self.do_all(class_name)
            elif command == 'count()':
                count = 0
                instances = storage.all().values()
                for item in instances:
                    if isinstance(item, eval(class_name)):
                        count += 1
                print(count)
            elif command.startswith('show(') and command.endswith(')'):
                instance_id = command.split('(')[1].split(')')[0]
                self.do_show(f"{class_name} {instance_id}")
            elif command.startswith('destroy(') and command.endswith(')'):
                instance_id = command.split('(')[1].split(')')[0]
                self.do_destroy(f"{class_name} {instance_id}")
            elif command.startswith('update(') and command.endswith(')'):
                update_args = command.split('(')[1].split(')')[0].split(', ')
                if len(update_args) == 3:
                    self.do_update(
                            f"{class_name} {update_args[0]} "
                            f"{update_args[1]} {update_args[2]}"
                    )
                elif len(update_args) == 2:
                    for item in update_args:
                        if item.startswith('{') or item.endswith('}'):
                            dict_args = item.strip('{}')
                            arg_list = dict_args.split(': ')
                            self.do_update(
                                    f"{class_name} {update_args[0]} "
                                    f"{arg_list[0]} {arg_list[1]}"
                            )
                    else:
                        print("** invalid command **")
                else:
                    print("** invalid command **")
            else:
                print("** invalid command **")
        else:
            print("** invalid command **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

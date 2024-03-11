#!/usr/bin/python3
""" implementing the HBNB console """
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    available_classes = ["BaseModel", "User"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """ help for quit command """
        print("exiting prompt using quit command")

    def emptyline(self):
        """do no thing when pressing enter or empty line"""
        pass

    def do_EOF(self, line):
        """Exiting the console <command interpretor>"""
        print(" ")
        return True

    def default(self, line):
        print(f"Unknown command, {line}")

    def do_create(self, usr_input):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        else:
            created_instance = eval(f"commands[0]()")
            storage.save()
            print(created_instance.id)

    def do_show(self, usr_input):
        """Usage: show <class> <id> or <class>.show(<id>
        Display the string representation of a class instance of a given id.
        """
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}.format(commands[0], commands[1])"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, usr_input):
        """Deletes an instance based on the class name and id.
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}.format(commands[0], commands[1])"
            if key in objects:
                del object[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, usr_input):
        """prints all string representation of all
        instance based or not on the class name and.
        """
        objects = storage.all()
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in available_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')(0) == commands[0]:
                    print(self.value)

    def do_update(self, usr_input):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}.format(commands[0], commands[1])"
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]
                try:
                    attr_value = eval[atrr_value]
                except Exception:
                    pass
                setattr(obj, atrr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

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

    """def default(self, line):
         print(f"Unknown command, {line}")
    """
    def do_create(self, usr_input):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id  """
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        else:
            created_instance = eval(f"commands[0]()")
            storage.save()
            print(created_instance.id)  
       
    #----------------------------------------------------     
    def do_show(self, usr_input):
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{commands[0]}.{commands[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    #---------------------------------------------------- 
    def do_destroy(self, usr_input):
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del object[key]
                storage.save()
            else:
                print("** no instance found **")
    
    #---------------------------------------------------- 
    def do_all(self, usr_input):
        objects = storage.all()
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.available_classes:
             print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')(0) == commands[0]:
                    print(self.value)

    #---------------------------------------------------- 
    def do_update(self, usr_input):
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]
                try:
                    attr_value = eval[attr_name]
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

#---------------------------------------------------- 
         
if __name__ == '__main__':
     HBNBCommand().cmdloop()

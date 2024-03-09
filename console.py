#!/usr/bin/python3
import cmd
import shlex
#from models.base_model import BaseModel
#from medels import storage

class HBNBCommand(cmd.Cmd):
    prompt = "hbnb >>> "
    valid_classes = ["BaseModel"]
    #---------------------------------------------------- 
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    #---------------------------------------------------- 
    def do_EOF(self, line):
        """Exiting the console <command interpretor>"""
        print()
        return True
    #---------------------------------------------------- 
    def do_emptyline(self):
        """do no thing when pressing enter or empty line"""
        pass
    #---------------------------------------------------- 
    def default(self, line):
         print(f"Unknown command, {line}")
    #---------------------------------------------------- 
    """def do_create(self, usr_input):
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            created_instance = BaseModel()
            created_instance.save()
            print(created_instance.id)  
    """    
    #----------------------------------------------------     
    """ def do_show(self, usr_input):
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
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
    """
    #---------------------------------------------------- 
    """def do_destroy(self, usr_input):
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
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
    """
    #---------------------------------------------------- 
    """def do_all(self, usr_input):
        objects = storage.all()
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in valid_classes:
             print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')(0) == commands[0]:
                    print(self.value)
    """
    #---------------------------------------------------- 
    """def do_update(self, usr_input):
        commands = shlex.split(usr_input)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}.format(commands[0], commands[1])"
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3
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
    """
#---------------------------------------------------- 
         
if __name__ == '__main__':
     HBNBCommand().cmdloop()

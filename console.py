#!/usr/bin/python3
'''Entry point file'''

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''HBNB Command Class'''

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    prompt = '(hbnh) '

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True

    def emptyline(self):
        '''Customised empty line command'''
        print('')

    def do_create(self, line):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        commands = line.split(" ")

        if len(line) < 1:
            print('** class name missing **')
        elif commands[0] not in HBNBCommand.__classes:
            newinstance = BaseModel()
            newinstance.save()
            print(newinstance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        commands = line.split(" ")
        dbobj = storage.all()

        if len(line) < 1:
            print('** class name missing **')
        elif commands[0] not in HBNBCommand.__classes:
            if len(commands) < 2:
                print("** instance id missing **")
            elif f"{commands[0]}.{commands[1]}" not in dbobj:
                print("** no instance found **")
            else:
                print(dbobj[f"{commands[0]}.{commands[1]}"])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        commands = line.split(" ")
        dbobj = storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif commands[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif f"{commands[0]}.{commands[1]}" not in dbobj:
            print("** no instance found **")
        else:
            del dbobj[f"{commands[0]}.{commands[1]}"]
            storage.save()

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        commands = line.split(" ")
        if len(commands) > 0 and commands[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            dbarr = []
            for obj in storage.all().values():
                if len(commands) > 0 and commands[0] == obj.__class__.__name__:
                    dbarr.append(obj.__str__())
                elif len(line) == 0:
                    dbarr.append(obj.__str__())
            print(dbarr)

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair."""
        commands = line.split(" ")
        dbobj = storage.all()

        if len(line) == 0:
            print("** class name missing **")
            return False

        if commands[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        if len(commands) == 1:
            print("** instance id missing **")
            return False

        if f"{commands[0]}.{commands[1]}" not in dbobj:
            print("** no instance found **")
            return False

        if len(commands) == 2:
            print("** attribute name missing **")
            return False

        if len(commands) == 3:
            print("** value missing **")
            return False

        if len(commands) == 4:
            obj = dbobj[f"{commands[0]}.{commands[1]}"]
            if commands[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[commands[2]])
                obj.__dict__[commands[2]] = valtype(commands[3])
            else:
                obj.__dict__[commands[2]] = commands[3]

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

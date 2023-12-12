#!/usr/bin/python3
<<<<<<< HEAD
"""The HBNB console."""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models import store
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Does nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """ cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal end of the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Creates a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            store.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Displays the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = store.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes a class instance of a given id."""
        argl = parse(arg)
        objdict = store.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            store.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Displays string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in store.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieves the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in store.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Updates a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = store.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        store.save()


if __name__ == "__main__":
=======
"""
the entry point to the command interpreter
"""


import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ command line interpreter"""
    prompt = "(hbnb) "
    all_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def do_EOF(self, line):
        """ Interprets Ctrl + D
        """
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        It ignores the last nonempty
        command entered and does nothing
        """
        pass

    def do_create(self, line):
        """Creates a new BaseModel instance
        Args:
            None
        Prints id of the new BaseModel instance
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        else:
            base1 = HBNBCommand.all_classes[line]()
            base1.save()
            print(base1.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id. Example: $ show BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id. Example: (hbnb)  destroy BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                del(all_instances[ke_y])
                storage.save()

    def do_all(self, line):
        """
        Prints the string representation of all instances
        Example: (hbnb) all BaseModel
        or (hbnb) all
        """
        obj_list = []
        objs = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    obj_list.append(val)
            else:
                val = str(objs[key])
                obj_list.append(val)
        print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: (hbnb)
        update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        elif len(a_list) == 2:
            print("** attribute name missing **")
        elif len(a_list) == 3:
            print("** value missing **")
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                setattr(obj, a_list[2], a_list[3])
                storage.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        If this method is not overridden, it prints an error message and
        returns.
        """
        if len(line) == 0:
            return
        else:
            args = line.split('.')
            class_arg = args[0]
            if class_arg in HBNBCommand.all_classes:
                if len(args) == 2:
                    if args[1] == "all()":
                        HBNBCommand.do_all(self, class_arg)
                    elif args[1] == "count()":
                        print((HBNBCommand.instance_count(self, class_arg)))
                    elif str(args[1])[:4] == "show":
                        string = args[1]
                        c_id = string[6:-2]
                        l_ine = str(class_arg) + " " + str(c_id)
                        HBNBCommand.do_show(self, l_ine)
                    elif str(args[1])[:7] == "destroy":
                        string = args[1]
                        c_id = string[9:-2]
                        l_ine = str(class_arg) + " " + str(c_id)
                        HBNBCommand.do_destroy(self, l_ine)
                    elif str(args[1])[:6] == "update":
                        a_slc = args[1][7:-1]
                        my_list = a_slc.split(", ")
                        _id = my_list[0][1:-1]
                        if type(my_list[1]) == dict:
                            for att, val in my_list[1].items():
                                l = class_arg + " " + _id + " " + att + val
                                HBNBCommand.do_update(self, l)
                        else:
                            if my_list[2][0] == '"' and my_list[2][-1] == '"':
                                val = my_list[2][1:-1]
                            else:
                                val = my_list[2]
                            if my_list[1][0] == '"' and my_list[1][-1] == '"':
                                attr = my_list[1][1:-1]
                            else:
                                attr = my_list[1]
                            l = str(class_arg + " " + _id + " " + attr +
                                    " " + val)
                            HBNBCommand.do_update(self, l)
                    else:
                        pass
                else:
                    print("Try: {}.all() or all {}".format(args[0], args[0]))
            else:
                print("*** Unknown syntax: {}".format(line))
                return

    def instance_count(self, line):
        """
        Returns a list containing string representation of instances
        """
        count = 0
        obj_list = []
        all_list = []
        all_instances = storage.all()
        if line == "":
            for k, obj in all_instances.items():
                all_list.append(str(obj))
                count = count + 1
            return(count)
        elif line in HBNBCommand.all_classes.keys():
            for k, v in all_instances.items():
                if line == v.__class__.__name__:
                    ke_y = line + "." + str(v.id)
                    obj_list.append(all_instances[ke_y])
                    count = count + 1
            return(count)

if __name__ == '__main__':
>>>>>>> naf_tasks
    HBNBCommand().cmdloop()

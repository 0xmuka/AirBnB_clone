#!/usr/bin/python3
import cmd 
class HBNBCommand(cmd.Cmd):
    """ 
    HBNBCommand
    """
    prompt = "(hbnb)"
    def do_quit (self , line) :
        """
        To quit the program with hema 
        
        """
        return True 

    def do_EOF (self , line) :
        """
        End of file
         
        """
        return True  
    
    def do_help(self, arg: str) -> bool | None:

        """
        to do help
        
        """
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    

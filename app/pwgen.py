
# A few functions to call and return pwgen output
from os import name
from subprocess import run

class Pwgen:
    # Private
    def __init__(self, flags=[]):
        self.__flags = flags
        self.__command = ['pwgen']
        # If not Unix, raise error.
        if not (self.__is_unix()):
            raise Exception("[1]: This code only runs on Unix-based machines.")

    def __is_unix(self) -> bool:
        if (name != 'posix'):
            return False
        else:
            return True
    
    # Operations 
    def pwgen(self) -> str:
        result = run(self.get_command(), capture_output=True, text=True)
        if not (result.returncode):
            return result.stdout
        raise Exception(f"[1]: {result.stderr}")  # If not success, raise error
    
    def print_command(self) -> None:
        cmd_str = " ".join(self.get_command())
        print(cmd_str)
        
    # Accessors
    def get_flags(self) -> list:
        return self.__flags

    def get_command(self) -> list:
        return self.__command

    # Mutators
    def set_flags(self, new_flags: list) -> None:
        self.__flags = new_flags
    
    def set_command(self, new_command: list) -> None:
        self.__command = new_command


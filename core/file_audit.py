from pathlib import Path

class FileAudit():
    def __init__(self, list_of_files: list, /) -> None:
        self.list_of_files = list_of_files
        self.files = [ Path(file) for file in list_of_files ]

    
    def file_exists(self) -> bool:
        for file in self.files:
            if not file.is_file():
                raise FileNotFoundError(f'File not exists {file.name}')


    def check_mode_valid(self, mode) -> bool:
        # Checking OCTAL mode
        try:
            int(mode) # Checking if the number can be converted to an integer
        except ValueError:
           raise ValueError(f'The provided parameter cannot be converted to the int type {mode=}')
        
        if len(mode) > 4: # Checking if the number has the correct number of digits
            raise ValueError(f'The provided mode cannot have more than 4 digits {mode=}')
        elif len(mode) < 4:
            raise ValueError(f'Please provide exactly 4 digits for the mode parameter {mode=}')

        for number in mode: # Checking if the number is in octal format
            if int(number) > 7 or int(number) < 0:
                raise ValueError(f'The number provided is not valid for mode permission {number=}')

    
    def check_permissions(self, mode: str) -> list:
        """
        Verifies if the files have the expected permissions.

        Args:
            mode (str): The permissions in octal format (e.g., '0644', '0755').
                        Symbolic notation (e.g., 'rwxr-xr-x') is not supported.
                        Must be a string of digits 0-7 and have a length of 4.

        Returns:
            list: A list of tuples containing the filename and its current permissions.
        """
        # Checking if files exist
        self.file_exists()
        
        # Checking if file mode parameter is valid
        self.check_mode_valid(mode)
        
        list_of_verified_files = []
        for file in self.files:
            file_permissions = oct(file.stat().st_mode)[-4:]
            if file_permissions == mode:
                checked_file_boolean = True
            else:
                checked_file_boolean = False

            list_of_verified_files.append((checked_file_boolean, file.resolve(), file_permissions))

        return list_of_verified_files


    def change_permissions(self, mode: str, filepath: str) -> None:
        """
        Change the permissions of the files to the provided mode.

        Args:
            mode (str): The permissions in octal format (e.g., '0644', '0755').
                        Symbolic notation (e.g., 'rwxr-xr-x') is not supported.
                        Must be a string of digits 0-7 and have a length of 4.
            
            filepath (str): The path to the file.
        """
        print(f'Executing {filepath}')
        

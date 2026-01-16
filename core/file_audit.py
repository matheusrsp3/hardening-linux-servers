from pathlib import Path

class FileAudit():
    def __init__(self, list_of_files: list, /) -> None:
        self.list_of_files = list_of_files
        self.files = [ Path(file) for file in list_of_files ]

    
    def file_exists(self) -> bool:
        for file in self.files:
            if not file.is_file():
                raise FileNotFoundError(f'File not exists {file.name}')


    def check_mode(self, mode):
        # Checking OCTAL mode
        try:
            int(mode)
        except ValueError:
           raise ValueError(f'The provided parameter cannot be converted to the int type {mode=}')
        else:
            return True

    
    def check_permissions(self, mode: str) -> None:
        # Checking if files exist
        self.file_exists()
        
        # Checking if file mode parameter is valid
        self.check_mode(mode)
        
        print(f'Checking permissions...')
        for file in self.files:
            file_permissions = oct(file.stat().st_mode)[-4:]
            print(f'File permissions: {file.name} {file_permissions}')
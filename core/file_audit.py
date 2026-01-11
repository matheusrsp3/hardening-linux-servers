from pathlib import Path

class FileAudit():
    def __init__(self, list_of_files: list, /) -> None:
        self.list_of_files = list_of_files
        self.files = [ Path(file) for file in list_of_files ]

    
    def file_exists(self) -> bool:
        for file in self.files:
            if not file.is_file():
                return False

        return True

    
    def check_permissions(self) -> None:
        if not self.file_exists():
            # TODO: Adjust to display the file name
            raise FileNotFoundError(f'File not exists')
        
        print(f'Checking permissions...')
import os
import shutil
from .common import FileUploaderInterface


class LocalFileMover(FileUploaderInterface):

    def __init__(self, **kwargs) -> None:
        self.destination_path = kwargs.get("destination_path")
        self.id = kwargs.get("id")
        self.file_path = kwargs.get("file_path")
        self.file_name =  kwargs.get("file_name")

    @staticmethod
    def upload_type() -> str:
        return "local"

    def upload_file(self) -> bool:
        if not os.path.isfile(self.file_path):
            raise ValueError(f"The file {self.file_path} does not exist.")

        final_location = os.path.join(
            self.destination_path, os.path.basename(self.file_path)
        )
        try:
            shutil.copy(self.file_path, final_location)
            print(f"File {self.file_path} copied successfully to {final_location}.")
            return True
        except Exception as e:
            print(f"Failed to copied {self.file_path} to {final_location}: {e}")
            return False


# Example usage:
# mover = LocalFileMover('/home/joseph/projects/nsp-data-sender/tests/docs', 'your-id')
# mover.upload_file('/home/joseph/projects/nsp-data-sender/LICENSE')

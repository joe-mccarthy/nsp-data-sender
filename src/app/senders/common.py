from abc import ABC, abstractmethod
import json
from datetime import datetime
import os

class FileUploaderInterface(ABC):

    status: str = "pending"
    file_path: str = None
    file_name: str = None
    created: datetime = datetime.now()

    @abstractmethod
    def upload_file(self) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def upload_type(self) -> str:
        pass

    def to_json(self) -> str:
        data = {
            "file_path": self.file_path,
            "file_name" : self.file_name,
            "sender_id": self.id,
            "status": self.status,
            "type": self.upload_type(),
            "timestamp": self.created.isoformat(),
        }
        return json.dumps(data)

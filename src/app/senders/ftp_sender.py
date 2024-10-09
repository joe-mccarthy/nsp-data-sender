import ftplib
import paramiko
import os
from .common import FileUploaderInterface


class FTPUploader(FileUploaderInterface):
    def __init__(self, port=21, **kwargs):
        self.host = kwargs.get("host")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.port = kwargs.get("port", port)
        self.id = kwargs.get("id")
        self.file_path = kwargs.get("file_path")
        self.file_name =  kwargs.get("file_name")


    @staticmethod
    def upload_type() -> str:
        return "ftp"

    def upload_file(self) -> bool:
        if not os.path.isfile(self.file_path):
            raise ValueError(f"The file {self.file_path} does not exist.")

        file_name = os.path.basename(self.file_path)
        try:
            with ftplib.FTP() as ftp:
                ftp.connect(self.host, self.port)
                ftp.login(self.username, self.password)
                with open(self.file_path, "rb") as file:
                    ftp.storbinary(f"STOR {file_name}", file)
            print(f"File {file_name} uploaded successfully to FTP server {self.host}.")
            return True
        except Exception as e:
            print(f"Failed to upload {file_name} to FTP server {self.host}: {e}")
            return False


class SFTPUploader(FileUploaderInterface):
    def __init__(self, port=22, **kwargs):
        self.host = kwargs.get("host")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.port = kwargs.get("port", port)
        self.id = kwargs.get("id")
        self.file_path = kwargs.get("file_path")
        self.file_name =  kwargs.get("file_name")

    @staticmethod
    def upload_type() -> str:
        return "sftp"

    def upload_file(self) -> bool:
        if not os.path.isfile(self.file_path):
            raise ValueError(f"The file {self.file_path} does not exist.")

        file_name = os.path.basename(self.file_path)
        try:
            transport = paramiko.Transport((self.host, self.port))
            transport.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(self.file_path, file_name)
            sftp.close()
            transport.close()
            print(f"File {file_name} uploaded successfully to SFTP server {self.host}.")
            return True
        except Exception as e:
            print(f"Failed to upload {file_name} to SFTP server {self.host}: {e}")
            return False


class FTPSUploader(FileUploaderInterface):
    def __init__(self, port=21, **kwargs):
        self.host = kwargs.get("host")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.port = kwargs.get("port", port)
        self.id = kwargs.get("id")
        self.file_path = kwargs.get("file_path")
        self.file_name =  kwargs.get("file_name")

    @staticmethod
    def upload_type() -> str:
        return "ftps"

    def upload_file(self) -> bool:
        if not os.path.isfile(self.file_path):
            raise ValueError(f"The file {self.file_path} does not exist.")

        file_name = os.path.basename(self.file_path)
        try:
            with ftplib.FTP_TLS() as ftps:
                ftps.connect(self.host, self.port)
                ftps.login(self.username, self.password)
                ftps.prot_p()  # Secure data connection
                with open(self.file_path, "rb") as file:
                    ftps.storbinary(f"STOR {file_name}", file)
            print(f"File {file_name} uploaded successfully to FTPS server {self.host}.")
            return True
        except Exception as e:
            print(f"Failed to upload {file_name} to FTPS server {self.host}: {e}")
            return False

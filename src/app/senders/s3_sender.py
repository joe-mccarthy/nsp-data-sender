import boto3
import os
from .common import FileUploaderInterface


class S3Uploader(FileUploaderInterface):
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.file_path = kwargs.get("file_path")
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=kwargs.get("aws_access_key_id"),
            aws_secret_access_key=kwargs.get("aws_secret_access_key"),
            region_name=kwargs.get("region_name"),
        )
        self.bucket_name = kwargs.get("bucket_name")
        self.bucket_path = kwargs.get("bucket_path")
        self.file_name =  kwargs.get("file_name")

    @staticmethod
    def upload_type() -> str:
        return "s3"

    def upload_file(self) -> bool:
        if not os.path.isfile(self.file_path):
            raise ValueError(f"The file {self.file_path} does not exist.")

        file_name = os.path.basename(self.file_path)
        final_path = (
            os.path.join(self.bucket_path, file_name) if self.bucket_path else file_name
        )
        with open(self.file_path, "rb") as f:
            self.s3_client.upload_fileobj(f, self.bucket_name, final_path)
            print(f"File {file_name} uploaded successfully to {self.bucket_name}.")
            return True

        print(f"Failed to upload {file_name} to {self.bucket_name}: {e}")
        return False


# Example usage:
# uploader = S3Uploader( bucket_name= 'my-bucket', id='your-id', file_path='path/to/your/file.txt', aws_access_key_id='key', aws_secret_access_key='secret', region_name='eu-west-2')
# print(uploader.to_json())
# uploader.upload_file()

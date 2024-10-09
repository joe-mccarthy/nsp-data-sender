from .ftp_sender import FTPUploader, SFTPUploader, FTPSUploader
from .s3_sender import S3Uploader
from .file_system import LocalFileMover


class FileUploaderFactory:
    @staticmethod
    def get_uploader(uploader_type, **kwargs):
        if uploader_type == FTPUploader.upload_type():
            return FTPUploader(**kwargs)
        elif uploader_type == SFTPUploader.upload_type():
            return SFTPUploader(**kwargs)
        elif uploader_type == S3Uploader.upload_type():
            return S3Uploader(**kwargs)
        elif uploader_type == FTPSUploader.upload_type():
            return FTPSUploader(**kwargs)
        elif uploader_type == LocalFileMover.upload_type():
            return LocalFileMover(**kwargs)
        else:
            raise ValueError(f"Unknown uploader type: {uploader_type}")


# Example usage:
# factory = FileUploaderFactory()
# ftp_uploader = factory.get_uploader('ftp', host='ftp.example.com', username='user', password='pass')
# sftp_uploader = factory.get_uploader('sftp', host='sftp.example.com', username='user', password='pass')
# s3_uploader = factory.get_uploader('s3', bucket_name='my-bucket', aws_access_key_id='key', aws_secret_access_key='secret', region_name='us-west-1')
# local_mover = factory.get_uploader('local')

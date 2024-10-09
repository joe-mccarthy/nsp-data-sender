from pytest import raises
from src.app.senders.sender import (
    FileUploaderFactory,
    FTPUploader,
    SFTPUploader,
    S3Uploader,
    LocalFileMover,
    FTPSUploader,
)


def test_get_ftp_uploader():
    uploader = FileUploaderFactory.get_uploader(
        "ftp",
        host="ftp.example.com",
        username="user",
        password="pass",
        file_path="test",
        id="id",
    )
    assert isinstance(uploader, FTPUploader)


def test_get_sftp_uploader():
    uploader = FileUploaderFactory.get_uploader(
        "sftp",
        host="sftp.example.com",
        username="user",
        password="pass",
        file_path="test",
        id="id",
    )
    assert isinstance(uploader, SFTPUploader)


def test_get_s3_uploader():
    uploader = FileUploaderFactory.get_uploader(
        "s3",
        id="id",
        bucket_name="my-bucket",
        file_path="test",
        aws_access_key_id="key",
        aws_secret_access_key="secret",
        region_name="us-west-1",
    )
    assert isinstance(uploader, S3Uploader)


def test_get_ftps_uploader():
    uploader = FileUploaderFactory.get_uploader(
        "ftps",
        host="ftps.example.com",
        username="user",
        password="pass",
        file_path="test",
        id="id",
    )
    assert isinstance(uploader, FTPSUploader)


def test_get_local_file_mover():
    uploader = FileUploaderFactory.get_uploader(
        "local", destination_path="dest", file_path="test", id="id"
    )
    assert isinstance(uploader, LocalFileMover)


def test_get_unknown_uploader():
    with raises(ValueError):
        FileUploaderFactory.get_uploader("unknown")

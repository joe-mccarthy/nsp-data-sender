from typing import List
from dataclasses import dataclass

@dataclass
class Configuration:
    id: str = None
    type: str = None
    host: str = None
    username: str = None
    password: str = None
    port: int = None
    file_path: str = None
    bucket_name: str = None
    bucket_path: str = None
    aws_access_key_id: str = None
    aws_secret_access_key: str = None
    region_name: str = None
    destination_path: str = None
    file_name: str = None

def get_single_configuration(configuration_location: str, configuration_id: str) -> Configuration:
    configurations = get_configurations(configuration_location)
    for configuration in configurations:
        if configuration.id == configuration_id:
            return configuration
    return None

def get_configurations(configuration_location: str) -> List[Configuration]:
    ftp = Configuration(
        id="1",
        port=4324,
        type="ftp",
        username="username",
        password="password",
        host="testHost.ftp",
    )
    sftp = Configuration(
        id="2",
        port=43,
        type="sftp",
        username="username",
        password="password",
        host="testHost.sftp",
    )
    ftps = Configuration(
        id="3",
        port=21,
        type="ftps",
        username="username",
        password="password",
        host="testHost.ftps",
    )
    local = Configuration(id="4", type="local", destination_path="testPath")
    s3 = Configuration(
        id="5",
        type="s3",
        bucket_name="bucketName",
        file_path="testPath",
        aws_access_key_id="key",
        aws_secret_access_key="secret",
        region_name="region",
    )
    return [ftp, sftp, ftps, local, s3]

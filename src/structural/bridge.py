# bridge example
# the bridge pattern is used to decrease the number of classes, lowering the complexity of the algorthm in this way
# see: https://refactoring.guru/design-patterns/bridge for a complete example
from abc import ABC, abstractmethod
from typing import List, Tuple
import random, string


# abstractions
class Protocol(ABC):
    @abstractmethod
    def download(self, data: str):
        pass

    @abstractmethod
    def upload(self, data: str):
        pass


class FileServer(ABC):
    _protocol: Protocol

    def __init__(self, protocol: Protocol) -> None:
        self._protocol = protocol

    @abstractmethod
    def login(self, login_data: Tuple(str, str)):
        pass

    def _get_data(self, file_path: str) -> str:
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(15))

    @abstractmethod
    def upload_files(self, file_paths: List[str]):
        pass

    @abstractmethod
    def download_files(self, file_paths: List[str]):
        pass


# concrete protocols
class FTPProcotol(Protocol):
    def upload(self, data: str):
        print(f"Uploading data: b'{data}' Using protocol: 'FTP'")

    def download(self, data: str):
        print(f"Downloading data: b'{data}' Using protocol: 'FTP'")


class HTTPProtocol(Protocol):
    def upload(self, data: str):
        print(f"Uploading data: b'{data}' Using protocol: 'HTTP'")

    def download(self, data: str):
        print(f"Downloading data: b'{data}' Using protocol: 'HTTP'")


# concrete file servers
class LimitedFileServer(FileServer):
    def login(self, login_data: Tuple(str, str)):
        print(f"Logged as {login_data[0]}")

    def upload_files(self, file_paths: List[str]):
        for fp in file_paths:
            print(f"LimitedServer: Upload path {fp}")
            data = self._get_data(fp)
            self._protocol.upload(data)

    def download_files(self, file_paths: List[str]):
        limit = 3
        current_index = 1

        for fp in file_paths:
            if current_index >= limit:
                print("Download limit reached, stopping downloads")
                break

            print(f"LimitedServer: Download path {fp}")
            data = self._get_data(fp)
            self._protocol.download(data)
            current_index += 1


class OpenFileServer(FileServer):
    def login(self, login_data: Tuple(str, str)):
        print("Login is not needed in this server")

    def upload_files(self, file_paths: List[str]):
        for fp in file_paths:
            print(f"OpenServer: Upload path {fp}")
            data = self._get_data(fp)
            self._protocol.upload(data)

    def download_files(self, file_paths: List[str]):
        for fp in file_paths:
            print(f"OpenServer: Download path {fp}")
            data = self._get_data(fp)
            self._protocol.download(data)

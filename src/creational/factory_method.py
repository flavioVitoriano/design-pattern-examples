# Factory Method Example
# In this code, we will create a factory method for creating different outputs for exporting data
# it is important to note that factory methods can also be used inside classes and another abstractions

from abc import ABC, abstractmethod
from typing import Literal, Union
import json
import pickle

# First we need to create a base class for all the exporters
class Exporter(ABC):
    @abstractmethod
    def export(self, data: Union[dict, list]):
        pass


# An Export for JSON
class JsonExporter(Exporter):
    def export(self, data: Union[dict, list]):
        return json.dumps(data)


# An Export for Binary
class BinaryExporter(Exporter):
    def export(self, data: Union[dict, list]):
        return pickle.dumps(data)


# This will be our factory method
def ExportFactory(format_type=Union[Literal["binary"], Literal["json"]]) -> Exporter:
    if format_type == "binary":
        return BinaryExporter()
    if format_type == "json":
        return JsonExporter()

    raise ValueError("Invalid export format provided")


if __name__ == "__main__":
    my_data = [
        {"name": "Monalisa Overdrive", "author": "Willian Gibson"},
        {"name": "I have no mouth, and i must scream", "author": "Harlan Ellison"},
    ]

    # here we can create the objects using factories
    json_exporter = ExportFactory(format_type="json")
    binary_exporter = ExportFactory(format_type="binary")

    json_data = json_exporter.export(my_data)
    binary_data = binary_exporter.export(my_data)

    print(f"Type: {type(json_data)}. Output: {json_data}")
    print(f"Type: {type(binary_data)}. Output: {binary_data}")

# singleton example
# in this example, we will implement a version of singleton, using the implicit way.
from __future__ import annotations


class Singleton:
    # we need to initialize the instance with None, for the state sharing
    _instance: Singleton = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class GlobalData(Singleton):
    pass


if __name__ == "__main__":
    # these two are the same object
    global_variables = GlobalData()
    global_variables_2 = GlobalData()

    assert global_variables is global_variables_2

    global_variables.log_stack = ["1", "2", "3"]

    assert global_variables.log_stack == global_variables_2.log_stack

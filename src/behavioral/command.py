class Receiver:
    """the receiver classes can contain the bussiness logic of the application"""
    def __init__(self) -> None:
        pass

    def execute_action(self) -> None:
        pass


class BaseCommand:
    """Base Command"""
    def __init__(self) -> None:
        pass

    def execute_request(self):
        raise NotImplementedError("Not implemented")


class SimpleCommand(BaseCommand):
    """This command contain the bussiness logic internally"""
    def execute_request(self):
        print("Executing simple command")


class CommandWithReceiver(BaseCommand):
    """This command delegates the bussiness logic to a receiver class"""
    def __init__(self, receiver: Receiver) -> None:
        self._receiver: Receiver = receiver

    def execute_request(self):
        print("Delegating bussiness logic to a receiver")
        self._receiver.execute_action()


class Invoker:
    """The invoker is a class that makes requests to command objects"""
    # example of usage
    def set_callback_command(self, cmd: BaseCommand):
        self._callback_command = cmd
    
    def on_callback(self):
        self._callback_command.execute_request()

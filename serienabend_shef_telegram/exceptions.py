class SerienabendShefError(Exception):
    def __init__(self, message: str, command_error: str) -> None:
        super().__init__(message)
        self.command_error = command_error

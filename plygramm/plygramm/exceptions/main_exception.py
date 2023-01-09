class AppError(Exception):
    def __init__(self, message: str, *extra_args: object) -> None:
        super().__init__(message)

        self.message = message
        self.extra_args = extra_args or {}

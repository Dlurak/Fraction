class NoDivisionError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ToManyValuesError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class ToFewValuesError(Exception):
    def __init__(self, messge: str):
        super().__init__(messge)
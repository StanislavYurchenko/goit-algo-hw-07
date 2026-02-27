from field import Field


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        if not self.value.isdigit() or len(self.value) != 10:
            raise ValueError("Phone number must be a 10-digit string.")
from typing import NamedTuple

class User(NamedTuple):
    id: int
    first_name: str
    email: str
    last_name: str
    avatar: str
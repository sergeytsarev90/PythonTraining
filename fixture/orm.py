from pony.orm import *


class ORMFixture:


    db = Database()

    class ORMGroup:
        id = PrimaryKey(int)
        name = Optional(str)
        header
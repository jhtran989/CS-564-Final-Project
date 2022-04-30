from enum import Enum, auto


class Table():
    def __init__(self, tableName):
        self.tableName = tableName
        self.attributes = {}

    @classmethod
    def tableFactory(cls, tableName):
        table = cls(tableName)

        if tableName == TableEnum.REMAINS:
            for name, member in Remains.__members__.items():
                table.attributes[member] = None
        elif tableName == TableEnum.BIOLOGICAL_PROFILE:
            for name, member in BiologicalProfileEnum.__members__.items():
                table.attributes[member] = None
        else:
            return None

        return table

class TableEnum(Enum):
    REMAINS = auto()
    BIOLOGICAL_PROFILE = auto()

class Remains(Enum):
    REMAINS_ID = auto()

class BiologicalProfileEnum(Enum):
    SEX = auto(),
    AGE = auto(),
    ANCESTRY = auto(),
    STATUE = auto()

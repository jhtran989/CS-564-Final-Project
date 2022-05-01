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
        elif tableName == TableEnum.METHOD:
            for name, member in MethodEnum.__members__.items():
                table.attributes[member] = None
        elif tableName == TableEnum.REFERENCE:
            for name, member in ReferenceEnum.__members__.items():
                table.attributes[member] = None
        elif tableName == TableEnum.BIOAFFINITY:
            for name, member in BioaffinityEnum.__members__.items():
                table.attributes[member] = None

            table.attributes[BioaffinityEnum.BIOAFFINITY_ID] = \
                BioaffinityEnum.BIOAFFINITY_ID.value
        elif tableName == TableEnum.AGE:
            for name, member in AgeEnum.__members__.items():
                table.attributes[member] = None

            table.attributes[AgeEnum.AGE_ID] = \
                AgeEnum.AGE_ID.value
        elif tableName == TableEnum.STATURE:
            for name, member in StatureEnum.__members__.items():
                table.attributes[member] = None

            table.attributes[StatureEnum.STATURE_ID] = \
                StatureEnum.STATURE_ID.value
        elif tableName == TableEnum.INDIVIDUALIZING_CHARACTERISTICS:
            for name, member in IndividualizingCharEnum.__members__.items():
                table.attributes[member] = None
        else:
            return None

        return table

    def __str__(self):
        # finalString = f"{self.tableName.value()}: "

        # for key, value in self.attributes.items():
        #     finalString

        return self.tableName.name + ": " + self.attributes.__str__()

class TableEnum(Enum):
    REMAINS = auto(),
    BIOLOGICAL_PROFILE = auto(),
    METHOD = auto(),
    REFERENCE = auto(),
    BIOAFFINITY = auto(),
    AGE = auto(),
    STATURE = auto(),
    INDIVIDUALIZING_CHARACTERISTICS = auto()

class Remains(Enum):
    REMAINS_ID = auto()

    def __repr__(self):
        return self.name

"""
Hard-code the internal IDs (already taken care of with "auto()")

BIOLOGICAL_PROFILE_ID = 0,
SEX = 1,
AGE = 2,
BIOAFFNITY = 3,
STATUE = 4,
"""
class BiologicalProfileEnum(Enum):
    BIOLOGICAL_PROFILE_ID = auto(),
    SEX = auto(),
    AGE = auto(),
    BIOAFFNITY = auto(),
    STATURE = auto(),

    def __repr__(self):
        return self.name

class MethodEnum(Enum):
    METHOD_ID = auto(),
    METHOD = auto(),
    COMPARISON_GROUPS = auto(),
    ESTIMATE = auto(),
    REFERENCE_ID = auto()

    def __repr__(self):
        return self.name

class ReferenceEnum(Enum):
    REFERENCE_ID = auto(),
    REFERENCE = auto()

    def __repr__(self):
        return self.name

class AgeEnum(Enum):
    AGE_ID = BiologicalProfileEnum.AGE,
    AGE_ESTIMATE = auto()

    def __repr__(self):
        return self.name

class BioaffinityEnum(Enum):
    BIOAFFINITY_ID = BiologicalProfileEnum.BIOAFFNITY,
    BIOAFFINITY_ESTIMATE = auto()

    def __repr__(self):
        return self.name

class BioaffinityAttributesEnum(Enum):
    AFRICAN = auto(),
    ASIAN = auto(),
    EUROPEAN = auto()

    def __repr__(self):
        return self.name

class StatureEnum(Enum):
    STATURE_ID = BiologicalProfileEnum.STATURE,
    AGE_ESTIMATE = auto()

    def __repr__(self):
        return self.name

class IndividualizingCharEnum(Enum):
    IC_NOTES = auto()

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    table = Table(TableEnum.REMAINS)
    table.attributes[Remains.REMAINS_ID] = 123

    print(f"{Remains.REMAINS_ID.name}")
    print(f"{table}")

    print(f"{Remains.__members__.items()}")

# class DocMethod:
#     def __init__(self, methodId):
#
#
# class BioaffinityTable:
#     def __init__(self, bioaffinityId):
#         self.bioaffinityId = bioaffinityId

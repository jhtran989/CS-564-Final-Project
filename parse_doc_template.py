import re

import docx
from my_table import *
from parse_doc import *


# Print DEBUGS
PRINT_TABLE = True
PRINT_BIOAFFINITY_TABLE = False

# FIXME: for now, working with only one report
remainsId = 0

def parseText(doc, tableTotal):
    fullText = getText(doc)

    # first line
    firstLine = re.search(r"RE:  Forensic anthropological analysis of (.*) "
                          r"discovered in ((.*), (.*)).", fullText)
    typeRemain = firstLine.group(1)
    country = firstLine.group(3)
    state = firstLine.group(4)

    print(f"First Line:")
    print(f"type of remain: {typeRemain}")
    print(f"country: {country}")
    print(f"state: {state}")
    print()

    # get sex
    sexLine = re.search(r"Biological Profile\n"
                          r"Sex: (.*)", fullText)
    sex = sexLine.group(1)

    print(f"Sex:")
    print(f"sex: {sex}")
    print()

    # get bioaffinity
    bioaffinityLine = re.search(r"Bioaffinity/Ancestry: (.*)\n"
                                r"(.*)", fullText)
    bioaffinity = bioaffinityLine.group(1)
    bioaffinityNotes = bioaffinityLine.group(2)

    # add to table
    bioaffinityTable = tableTotal.getTable(TableEnum.BIOAFFINITY)
    # bioaffinityTable[]

    print(f"Bioaffinity:")
    print(f"bioaffinity: {bioaffinity}")
    print(f"notes: {bioaffinityNotes}")
    print()

    # get age
    ageLine = re.search(r"Age: ((.*)-(.*)) years old", fullText)
    startAge = ageLine.group(2)
    endAge = ageLine.group(3)

    print(f"Age:")
    print(f"start: {startAge}")
    print(f"end: {endAge}")
    print()

    # get stature
    statureLine = re.search(r"Stature: ((.*?)-(.*?)) inches\n"
                            r"(.*)", fullText)
    startStature = statureLine.group(2)
    endStature = statureLine.group(3)
    statureNotes = statureLine.group(4)

    print(f"Stature:")
    print(f"start: {startStature}")
    print(f"end: {endStature}")
    print(f"notes: {statureNotes}")
    print()

    # get individualizing characteristics
    individualizingCharLine = re.search(r"Individualizing characteristics:\n"
                                        r"(.*)", fullText)
    individualizingCharNotes = individualizingCharLine.group(1)

    print(f"Individualizing Characteristics:")
    print(f"notes: {individualizingCharNotes}")
    print()


def parseBiologicalProfileTable(doc, tableTotal):
    tableData = getTable(doc, 0)
    biologicalProfileLine = tableData[0][1]
    individualizingCharLine = tableData[1][1]
    perimortemTraumaLine = tableData[2][1]

    # biological profile values
    biologicalProfileValues = re.search(r"BIOLOGICAL PROFILE:(.*)\n"
                                            r"SEX:(.*)\n"
                                            r"AGE:(.*)\n"
                                            r"ANCESTRY:(.*)\n"
                                            r"STATURE:(.*)\n",
                                            biologicalProfileLine)

    sex = biologicalProfileValues.group(1).strip()
    age = biologicalProfileValues.group(2).strip()
    ancestry = biologicalProfileValues.group(3).strip()
    stature = biologicalProfileValues.group(4).strip()

    # add values to biological profile table
    bfTable = tableTotal.getTable(TableEnum.BIOLOGICAL_PROFILE)
    bfTable[BiologicalProfileEnum.SEX] = sex
    bfTable[BiologicalProfileEnum.AGE] = age
    bfTable[BiologicalProfileEnum.BIOAFFNITY] = ancestry
    bfTable[BiologicalProfileEnum.STATURE] = stature

    # individualizing characteristics values
    individualCharValues = re.search(r"INDIVIDUALIZING CHARACTERISTICS:"
                                        r"(.*)\n",
                                        individualizingCharLine)

    individualCharNotes = individualCharValues.group(1).strip()

    # add values to individualizing characteristics table
    icTable = tableTotal.getTable(TableEnum.INDIVIDUALIZING_CHARACTERISTICS)
    icTable[IndividualizingCharEnum.IC_NOTES] = individualCharNotes

    # individualizing characteristics values
    perimortemTraumaValues = re.search(r"PERIMORTEM TRAUMA:"
                                     r"(.*)\n",
                                     perimortemTraumaLine)

    perimortemTraumaNotes = perimortemTraumaValues.group(1).strip()


# all parsing of table below are STATIC (tables remain at the same relative
# position in the doc -- i.e., no extra tables than listed in the template)
def parseBioaffnityTable(doc):
    tableData = getTable(doc, 1)

    if PRINT_BIOAFFINITY_TABLE:
        print(f"{tableData}")


class TableEncapsular():
    def __init__(self):
        self.tables = []

    def addTable(self, table):
        self.tables.append(table)

    def getTable(self, tableEnum):
        for table in self.tables:
            if tableEnum == table.tableName:
                return table

        return None


if __name__ == "__main__":
    doc_filename = f"case_reports/DRAFTCaseReport_template.docx"
    doc = docx.Document(doc_filename)

    # initialize the tables
    tableTotal = TableEncapsular()
    for tableEnum in TableEnum.__members__.items():
        tableTotal.addTable(Table(tableEnum))

    remainsTable = tableTotal.getTable(TableEnum.REMAINS)
    remainsTable[Remains.REMAINS_ID] = remainsId

    #print(f"{getText(doc)}")
    parseText(doc, tableTotal)
    parseBioaffnityTable(doc)

    print(f"table output:")
    print(f"table 0:")
    print(f"{getTable(doc, 0)}")
    print(f"table 1:")
    print(f"{getTable(doc, 1)}")
    print(f"table 2:")
    print(f"{getTable(doc, 2)}")
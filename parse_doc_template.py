import re

import docx
import my_table
from parse_doc import *


# Print DEBUGS
PRINT_TABLE = True

def parseText(doc):
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


# all parsing of table below are STATIC (tables remain at the same relative
# position in the doc -- i.e., no extra tables than listed in the template)
def parseBioaffnityTable(doc):
    tableData = getTable(doc, 1)


if __name__ == "__main__":
    doc_filename = f"case_reports/DRAFTCaseReport_template.docx"
    doc = docx.Document(doc_filename)

    #print(f"{getText(doc)}")
    parseText(doc)

    print(f"table output:")
    print(f"table 0:")
    print(f"{getTable(doc, 0)}")
    print(f"table 1:")
    print(f"{getTable(doc, 1)}")
    print(f"table 2:")
    print(f"{getTable(doc, 2)}")
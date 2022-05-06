import re

import docx
import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *

# TODO: download stuff from nltk...
#nltk.download('punkt')
#nltk.download("averaged_perceptron_tagger")

import my_table
from parse_doc import *


# Print DEBUGS
PRINT_DOC = False
PRINT_METHOD = False


def parseText(doc):
    fullText = getText(doc)
    if PRINT_DOC:
        print(f"{fullText}")

    # fullText = "jkfl;jaldf (Thensd 1937) jkljak;f (Tkldsfjl and Rkdjlf 1990) " \
    #            "jaf;dl (Tkjfdsl et al. 1926) fajds"

    #TODO: in order to include the section headers, we have to determine
    # whether a paragraph is considered a section header (like # of words
    # less than 8) and then grab the chunk of text in between sections
    # headers to search for methods...

    # first, pattern match with regex to get a list of "candidate" strings of
    # methods
    # ASSUMING the year of the method is enclosed in "()" -- non-greedy
    # also leaves some room for whitespace on either side of the parentheses...
    # to search from right to left, need the regex module, not re...

    # split into two cases:
    # - Author(s) (Year)
    # - (Author(s) Year)
    # where Author(s) can be further pattern-matched below...
    methodCandidates = re.findall(r"[A-Z].*?(?:\([0-2][0-9]{3}.*?\))|"
                                  r"\([A-Z].*?[0-2][0-9]{3}.*?\)",
                                  fullText)

    # BEFORE REMOVING capturing of various groups
    # methodCandidates = re.findall(r"([A-Z].*?(\([0-2][0-9]{3}.*?\)))|"
    #                               r"(\([A-Z].*?[0-2][0-9]{3}.*?\))",
    #                               fullText)

    # original
    # methodCandidates = re.findall(r"(\(.*?[0-2][0-9]{3}.*?\))",
    #                               fullText)

    # methodCandidates = re.findall(r"(\((?:.*?[0-2][0-9]{3}.*?)?\))",
    #                               fullText)
    if PRINT_METHOD:
        print(f"{methodCandidates}")

        for candidate in methodCandidates:
            print(f"{candidate}")

    methodCandidates = '\n'.join(methodCandidates)

    # now need to remove all the punctuation...unless we want to preserve the
    # original format...so add it to the grammar for noun phrasing below?
    fullTextTokenize = word_tokenize(methodCandidates)
    methodPosTags = nltk.pos_tag(fullTextTokenize)
    if PRINT_METHOD:
        print(f"{methodPosTags}")



    # IMPORTANT: the ordering the the patterns MATTERS -- like for Buikstra
    # and Ubelaker (1994), we want to check the "and" case (i.e., two authors)
    # first before the single author case
    # NOTICE: seems like we can only have one split on a ":" per pattern...so
    # we need to repeat the same pattern name
    # crazy long expression...

    # TODO: change "et al." phrase to be <.*><.*><\.>
    methodGrammar = r"""
        NP: {<\(><NN.*>(<CC><NN.*>|<.*><.*><\.>)*<CD>(<\:><NN.*>(<CC><NN.*>|<.*><.*><\.>)*<CD>)*<\)>}
        NP: {<NN.*>(<CC><NN.*>|<.*><.*><\.>)*<\(><CD><\)>(<\:><NN.*>(<CC><NN.*>|<.*><.*><\.>)*<\(><CD><\)>)*}
        NP: {<\(><NN.*><CC><NN.*><CD><\)>}
            {<\(><NN.*><.*><.*><\.><CD><\)>}
            {<\(><NN.*><CD><\)>}
            {<NN.*><CC><NN.*><\(><CD><\)>}
            {<NN.*><.*><.*><\.><\(><CD><\)>}
            {<NN.*><\(><CD><\)>}
        """

    methodParser = nltk.RegexpParser(methodGrammar)
    methodTree = methodParser.parse(methodPosTags)
    if PRINT_METHOD:
        print(f"{methodTree}")

    for a in methodTree:
        if isinstance(a, nltk.tree.Tree):
            if a.label() == "NP":
                if PRINT_METHOD:
                    print()
                    print(a)

                words = [lf[0] for lf in a.leaves()]

                # the spaces (if applicable) are added right before each
                # word, so the first word doesn't count...
                parsedWord = [words[0]]
                wordsIter = words[1:]

                if PRINT_METHOD:
                    print(f"{words[0]}")

                # front parentheses check (since we don't want a space AFTER,
                # so it would have to be applied on the NEXT word)
                if words[0] == '(':
                    frontParenCheck = True
                else:
                    frontParenCheck = False

                # need to break the outer loop as well
                falsePositive = False
                for word in wordsIter:
                    # now, need to weed out phrases that aren't methods (e.g.,
                    # (Figure 11))
                    if word.lower() == "figure":
                        falsePositive = True

                        # parsed word still constructed for DEBUG purposes
                        #break

                    if PRINT_METHOD:
                        print(f"{word}")

                    if frontParenCheck:
                        parsedWord += f"{word}"
                        frontParenCheck = False
                    else:
                        if word == '(':
                            frontParenCheck = True

                        if word == '.' or word == ')' or word == ';':
                            parsedWord += f"{word}"
                        else:
                            parsedWord += f" {word}"

                finalWord = "".join(parsedWord)
                if falsePositive:
                    print(f"False positive, skipped: {finalWord}")
                else:
                    print(f"{finalWord}")

                #print()

                # for lf in a.leaves():
                #     print(f"{lf}")
                #
                #     currWord = lf[0]
                #     if currWord == '.':
                #         print("".join(currWord), end="")
                #     else:
                #         print(" ".join(currWord), end="")

                # print(" ".join([lf[0] for lf in a.leaves()]))

    # doesn't draw for me...maybe with Mac M1?
    #methodTree.draw()


if __name__ == "__main__":
    doc_filename = f"case_reports/FA802.BU-35.docx"
    doc = docx.Document(doc_filename)

    #print(f"{getText(doc)}")
    parseText(doc)

    # print(f"table output:")
    # print(f"table 0:")
    # print(f"{getTable(doc, 0)}")
    # print(f"table 1:")
    # print(f"{getTable(doc, 1)}")
    # print(f"table 2:")
    # print(f"{getTable(doc, 2)}")
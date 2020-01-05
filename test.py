from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import collections


def iter_block_items(parent):
    """
    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
        # print(parent_elm.xml)
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def getWordsFromBlock(block):
    words = []
    for word in block.text.split(" "):
        if word != " " and word != "\n" and word != "":
            words.append(word)

    return words

def getWordsFromTable(table):
    words = []
    for row in table.rows:
        for cell in row.cells: 
            for paragraph in cell.paragraphs:  
                for word in paragraph.text.split("\t"):
                    if word != " " and word != "\n" and word != "":
                        words.append(word)
    
    return words

def anydup(thelist):
    dubs = []
    seen = set()
    for x in thelist:
        if x in seen: 
            dubs.append(x)
        seen.add(x)
    return dubs

def getDublicates(filename):
    document = Document(filename)
    allWords = []
    for block in iter_block_items(document):
        if isinstance(block, Paragraph):
            allWords += getWordsFromBlock(block)
        elif isinstance(block, Table):
            allWords += getWordsFromTable(block)

    dubs = anydup(allWords)

    for dub in dubs:
        print("dub:" + dub)

    #output = [(key, (len(list(group)) + 1)) for key, group in groupby(dubs)]
    output=collections.Counter(dubs)

    for key in output.keys():
        output[key] += 1

    return output.items()


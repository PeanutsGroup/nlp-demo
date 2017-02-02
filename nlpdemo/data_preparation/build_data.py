# -*- coding: utf-8 -*-
#

from openpyxl import load_workbook
import re

def retrieve_contents(infile, outfile):
    wb = load_workbook(infile)
    ws = wb.active
    cells = ws['C']
    with open(outfile, 'w') as of:
        regex = re.compile('\r\n|\n')
        for cell in cells:
            if cell.row < 1:
                continue
            of.write(regex.sub(' ', str(cell.value)) + '\n')


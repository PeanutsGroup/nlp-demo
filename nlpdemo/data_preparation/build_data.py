# -*- coding: utf-8 -*-
#

import os
import re
from openpyxl import load_workbook

def iterate_all_xlsx(inpath):
    if os.path.isfile(inpath):
        yield inpath
    else:
        for f in os.listdir(inpath):
            if os.path.splitext(f)[1] == '.xlsx':
                yield os.path.join(inpath, f)

def retrieve_contents(inpath, outfile):
    regex = re.compile('\r\n|\n')
    with open(outfile, 'w') as of:
        for infile in iterate_all_xlsx(inpath):
            #print(infile)
            wb = load_workbook(infile)
            ws = wb.active
            cells = ws['C']
            #print(len(cells) - 1)
            for cell in cells:
                if cell.row < 2:
                    continue
                of.write(regex.sub(' ', str(cell.value)) + '\n')


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:41:47 2017
Modified on Thu Dec 21 11:22:00 2017

@author: 210008967
"""

import xlrd

workbook = xlrd.open_workbook('./data_input/cip 883333.xls')

# worksheet = workbook.sheet_by_name('Name of the Sheet')

worksheet = workbook.sheet_by_index(0)

max_rows = worksheet.nrows
max_cols = worksheet.ncols

crow = 0;
for crow in range(0, max_rows):
    ccol = 0
    line = ""
#    print("row " + crow)
    for ccol in range(0, max_cols):
        line = line + str(worksheet.cell(crow, ccol).value) + ","
#        print(worksheet.cell(crow, ccol).value)
    print(line.rstrip(","))

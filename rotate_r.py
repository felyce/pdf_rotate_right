#!/usr/bin/env python
# -*- coding: utf-8; -*-

from pyPdf import PdfFileWriter, PdfFileReader
import os, os.path
import sys

def rotate(_filename):
    print "Rotate all page of PDF:", _filename

        input_filename = _filename.replace(".pdf", ".pdf.bak")
            output_filename = _filename

            rotated = None
            original = None
            page_num = 0

            # start
            os.rename(_filename, input_filename)

            with open(input_filename, "rb") as origin:
                original = PdfFileReader(origin)
                page_num = original.getNumPages()

            rotated = PdfFileWriter()

            for i in xrange(0, page_num):
                rotated.addPage( original.getPage(i).rotateClockwise(90) )

            with open(output_filename, "wb") as outputStream:
                rotated.write(outputStream)

if __name__ == "__main__":
    for f_name in sys.argv[1:]:
        rotate(f_name)


# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 14:04:33 2015

@author: david
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = StringIO.StringIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, "Hello world")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("/home/david/Documents/hospitalfax/RIHRecordsRequest (1).pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()

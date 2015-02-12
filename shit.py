from PyPDF2 import PdfFileWriter, PdfFileReader
output = PdfFileWriter()

ipdf = PdfFileReader(open('/home/david/Documents/hospitalfax/RIHRecordsRequest (1).pdf', 'rb'))
wpdf = PdfFileReader(open('/home/david/Documents/hospitalfax/test2.pdf', 'rb'))
watermark = wpdf.getPage(0)

for i in xrange(ipdf.getNumPages()):
    page = ipdf.getPage(i)
    page.mergePage(watermark)
    output.addPage(page)

with open('/home/david/Documents/hospitalfax/test.pdf', 'wb') as f:
   output.write(f)
   

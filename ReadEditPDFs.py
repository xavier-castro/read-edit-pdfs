#! python3

import PyPDF2

# Opening the PDF and printing out the text of the first page
pdfFile = open('samplePDF.pdf', 'rb') # rb -> read/binary mode needed since pdfs are binary files
reader = PyPDF2.PdfFileReader(pdfFile) # Returns a PdfReader object for the file
print(reader.numPages) # Prints how many pages the pdf is
page = reader.getPage(0) # Assigns the first page the page variable
print(page.extractText()) # Attempts to get the text from the PDF

# Getting all of the text from the PDF document
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

# Adding, Removing, and Reordering pages of a PDF document (it is hard to change the contents of a PDF)
# Combining PDFs together
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter() # Creates a new PDF with 0 content for right now

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page) # Writes the content of page and adding it to the writer PDF document

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page) # Writes the content of page and adding it to the writer PDF document

outputFile = open('combinedminutes.pdf', 'wb') # wb -> write binary mode since we are creating a new pdf
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
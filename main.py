import PyPDF2 as p

# list of pdfs
pdFiles = ["1.pdf", "2.pdf"]

# create a new pdf merger
merger = p.PdfMerger()

for fileName in pdFiles:
    # open files
    file = open(fileName, 'rb')
    # read files
    reader = p.PdfReader(file)
    # append to the merger
    merger.append(reader)
    # close file
    file.close()

# write the merged file
merger.write("merged.pdf")

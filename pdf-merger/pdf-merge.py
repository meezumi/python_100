import PyPDF2
import sys
import os

# documentation: "https://pypdf2.readthedocs.io/en/3.0.0/"

path = "./pdfs"
pathOut = "/mergedPDF"

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        # print(file)
        merger.append(file)
    merger.write("combinedLabViva.pdf")

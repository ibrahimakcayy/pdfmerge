from pypdf import PdfMerger
import os

merger = PdfMerger()

for i in os.listdir():
    if i[-4::]==".pdf":
        merger.append(i)

merger.write("result.pdf")
merger.close()

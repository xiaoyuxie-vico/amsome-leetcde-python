# Awesome Leetcde in Python


# Combine pdfs
```python
from PyPDF2 import PdfFileMerger

pdfs = ['1._two_sum.pdf', '128._longest_consecutive_sequence.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
```

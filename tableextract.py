import pdfkit

pdf_file = open('Pathophysiology_of_disease_pdf.pdf', 'rb')
html_file = pdfkit.from_file(pdf_file, "htmlrep.html")
pdf_file.close()

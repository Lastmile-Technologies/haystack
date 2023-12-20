import os
import PyPDF2
from reportlab.pdfgen import canvas
import docx2txt
# from docx import savedocx
def save_text_to_pdf(text, pdf_path):
    # Create a PDF document
    pdf_canvas = canvas.Canvas(pdf_path)

    # Set the font and size
    pdf_canvas.setFont("Times-Roman", 12)

    # Write text to the PDF
    pdf_canvas.drawString(100, 700, text)

    # Save the PDF
    pdf_canvas.save()

for filename in os.listdir("MachineTranslation"):
    if filename.endswith(".docx"):
        filepath = os.path.join("MachineTranslation", filename)
        text = docx2txt.process(filepath)
        print(text)
        txt_file_path = "pdfOutput/"+filename.replace(".docx", ".txt")
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
        # with open(filepath, "r", encoding='utf-8') as f:
        #     text = f.read().decode("utf-8")
        #     print(text)
            # save_text_to_pdf(text, "pdfOutput/"+filename+".txt")


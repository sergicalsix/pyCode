import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_formatted_json_to_pdf(formatted_json, pdf_file):
    pdf = canvas.Canvas(pdf_file, pagesize=letter)
    pdf.setFont("Courier", 10)
    text_lines = formatted_json.split('\n')

    x = 50
    y = 750

    for line in text_lines:
        pdf.drawString(x, y, line)
        y -= 12

        if y < 50:
            pdf.showPage()
            y = 750

    pdf.save()


# JSONデータを読み込む
with open('data.json', 'r') as f:
    json_data = json.load(f)

formatted_json = json.dumps(json_data, indent=4)
##print(formatted_json)

pdf_file = "output.pdf"

convert_formatted_json_to_pdf(formatted_json, pdf_file)

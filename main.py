from fpdf import FPDF

from text import HEAD, BODY

# Constants
FONT_SIZE = 10
NAME = "Denis_Sazonov"
COMPANY = "Maltego"

# Replace special characters
head_ascii = HEAD.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-")
body_ascii = BODY.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-")

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=10)  # Margin in mm
pdf.set_font("Arial", size=FONT_SIZE)  # Font and size

# HEAD
for line in head_ascii.strip().split('\n'):
    pdf.cell(0, 8, line, ln=1, align='R')  # Line height and right alignment

pdf.ln(5)  # New line

# BODY
for line in body_ascii.strip().split('\n'):
    pdf.multi_cell(0, 8, line)  # Line height

# Save PDF
filename = f"{NAME}_Cover_Letter_{COMPANY}.pdf"
pdf.output(filename)

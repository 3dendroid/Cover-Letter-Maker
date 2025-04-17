from fpdf import FPDF

from text import TEXT

compact_cover_letter_ascii = TEXT

# Create a new one-page PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=10)
pdf.set_font("Arial", size=12) # Font and size

# Add text to the PDF
for line in compact_cover_letter_ascii.strip().split('\n'):
    pdf.multi_cell(0, 8, line) # line height

# Save the compact PDF
compact_pdf_path = "Cover_Letter.pdf"
pdf.output(compact_pdf_path)
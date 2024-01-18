from fpdf import FPDF, util

class MyPDF(FPDF):
    def header(self):
        # Set font properties
        self.set_auto_page_break(False)
        self.set_font("helvetica", "B", 40)

        # Set text alignment to center
        self.cell(0, 10, txt="CS50 Shirtificate", align="C")
        self.ln(40)
        self.image("shirtificate.png", x=0,)

    def footer(self):
        # Empty footer
        pass

# Create a PDF object
pdf = MyPDF(orientation="P", unit="mm", format="A4")

# Add a page
pdf.add_page()
pdf.set_font("helvetica", "B", 24)
name = input("Name: ")
pdf.set_text_color(255,255,255)
pdf.cell(0,-300,txt=f"{name} took CS50",align="C")

# Output the PDF
pdf.output("shirtificate.pdf")


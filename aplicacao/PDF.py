from reportlab.pdf import canvas
pdf =canvas.Canvas("teste.pdf")
pdf.drawString(100,200,"WXEMPLO DE PDF")
pdf.save()

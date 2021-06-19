from pathlib import Path
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from reportlab.pdfgen import canvas
import webbrowser as wb

class BillGenerator:
    def __init__(self):
        self.packet = io.BytesIO()
        self.c = canvas.Canvas(self.packet) #pagesize=(1036,781
    def billGen(self,data):
        # data is a dictionary with all the data needed to add to the reciept
        self.c.setFont('Helvetica',14)
        self.c.drawString(120,245,text= data['Name'])       # Name
        self.c.drawString(142,228,text=data['Phone'])       # Phone
        self.c.drawString(157,211,text = data['Batch'])     #Batch
        self.c.drawString(590,277,text = data['Date'])      # Date
        self.c.drawString(647,245,text = data['Tid'])       # Transaction Id
        self.c.drawString(642,228,text = data['Iid'])       # Installment ID
        self.c.drawString(110,110,text = data['Ino'])       # Installment Number
        self.c.drawString(240,110,text = data['Cname'])     # Course Name
        self.c.drawString(420,110,text = data['mode'])      # Mode of payment
        self.c.drawString(570,110,text = data['amount_paid'])    # Amount Paid
        self.c.drawString(115,48,text = data['total_pending'])   # Total Pending
        self.c.drawString(330,48,text = data['total_paid'])      # Total Paid
        self.c.drawString(600,48,text = data['next_idate'])      # Next Installment Date
        self.c.save()

        home = str(Path.home())+'/'                         # Gets the home directory of the system
        path = os.path.join(home,'Desktop')                 # We are creating the Folder in Desktop

        if 'Bill Reciepts' not in list(os.listdir(path)):   # Create a folder for the receipts to be in.
            os.mkdir(path+'/Bill Reciepts')                 # this adds a folder

        path = path + '/Bill Reciepts/' + 'Invoice_' + data['Tid'] + '_' + data['Date'] + '.pdf' # The name of each bill reciepts

        #Use the path variable to set the path where the invoice will be set
        self.packet.seek(0)
        new_pdf = PdfFileReader(self.packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open("invoice.pdf", "rb"))      #This is the Template for the Reciept.
        output = PdfFileWriter()
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open(path, "wb")
        output.write(outputStream)
        outputStream.close()
        #if we want to directly open the pdf in compter do the following code below:
        wb.open(path)

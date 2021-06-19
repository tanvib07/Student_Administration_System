from billGenerator import *

# data is the dictionary with all the data that is required for generating a bill receipt.
# All the values of the dictionary should be string. Make sure all values passed are converted to string.
data = { 'Name': 'Jack Sparrow', #self.final_name
         'Phone': '8087032795',  #stud id ...phone no
         'Batch': 'RHEL7OCT',    #stud id ...batch id...batch name
         'Date': '21-12-2020',   #trans_date
         'Tid': '21',            #install id...stud id...trans_id
         'Iid':'321',            #self.installment_id
         'Ino': '3',             #installment_no
         'Cname':'Linux RHEL 7', #stud id ...course id...course name
         'mode': 'Cash',         #self.mode_of_payment
         'amount_paid': '15000', #self.trans_amt
         'total_pending': '35000',#total_amt - total_paid
         'total_paid': '20000',  #total_paid
         'next_idate': '12-01-2021'} #installment table...payment_id ...fetchone ..not paid ...install_date

bill = BillGenerator()   # Creating a instance of BillGenerator
bill.billGen(data)       # Passing the dictionary to billGen Function
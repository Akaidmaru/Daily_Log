# EXPORT DATETIME SO I CAN GET THE EXACT TIME OF THE CALL
# CREATE DICTIONARY TO WORK
import openpyxl
import time
wb = openpyxl.Workbook()
hoja = wb.active
hoja.append(('Start Time', 'End Time', 'Phone Number', 'Status', 'Policy', 'Note'))

def agregar_valores():  # FUNCTION TO ADD THE LAST VALUES OF THE CLAIM AND SAVE.
    for r in result:
        hoja.append(r)
    wb.save('prueba3.xlsx')
# I START A INFINITE LOOP TO KEEP THE PROGRAM WORKING
while True:
    # I ASK FOR Q TO EXIT OR BLANK TO CONTINUE.
    flag = input("Press enter to record time or 'q' to exit: ")
    if flag == 'q':
        break
    else:
        start_time = time.strftime("%I:%M") #dt.now()
        p_n = input("Phone number: ")
        note = input("Reason:").lower()
#INFO, 2) CLAIM, 3) INTERPRETATION, 4) PAYMENT , 5) UPDATES, 6) UW
        if note == 'claim' or note == 'update' or note == 'payment':
            policy = input("Policy Number: ")
            status = input("Insert status to get end time:")
            end_time =  time.strftime("%I:%M") # MODIFIED TIME FOR ONLY HOUR AND MIN.
            result = {(start_time, end_time,
                p_n, status, policy, note)}
            agregar_valores()
        elif note == 'info' or note == 'interpretation' or note == 'uw':
            status = input("Insert status to get end time:")
            policy = '-'
            end_time =  time.strftime("%I:%M") # MODIFIED TIME FOR ONLY HOUR AND MIN.
            result = {(start_time, end_time,
                p_n, status, policy, note)}
            agregar_valores()
            
        

# HERE THE REPORT SHOULD BE SAVED.



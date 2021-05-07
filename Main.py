# EXPORT DATETIME SO I CAN GET THE EXACT TIME OF THE CALL
# CREATE DICTIONARY TO WORK
from datetime import datetime as dt
filename = 'daily_report.txt'
policy = '-'
report = {}
# I START A INFINITE LOOP TO KEEP THE PROGRAM WORKING
while True:
    # I ASK FOR Q TO EXIT OR BLANK TO CONTINUE.
    flag = input("Press enter to record time or 'q' to exit: ")
    if flag == 'q':
        break
    else:
        start_time = dt.now()
        p_n = input("Phone number: ")
        note = input("Reason:").lower()
#INFO, 2) CLAIM, 3) INTERPRETATION, 4) PAYMENT , 5) UPDATES, 6) UW
        if note == 'claim' or note == 'update' or note == 'payment':
            policy = input("Policy Number: ")
            status = input("Insert status to get end time:")
            end_time = dt.now()
            result = str(start_time) + ' ' + str(end_time) + ' ' + \
                p_n + ' ' + status + ' ' + policy + ' ' + note  
            with open(filename, 'a') as file_object:
                file_object.write(result)
        elif note == 'info' or note == 'interpretation' or note == 'uw':
            status = input("Insert status to get end time:")
            end_time = dt.now()
            result = str(start_time) + ' ' + str(end_time) + ' ' + \
                p_n + ' ' + status + ' ' + policy + ' ' + note
            with open(filename, 'a') as file_object:
                file_object.write(result)

# HERE THE REPORT SHOULD BE SAVED.



from csv import DictWriter
import os

def add_data_to_csv(row):
    field_names = ['Name', 'Gender', 'Stream', 'Internship', 'CGPA', 'Hostel', 'Backlog', 'Predicted']
    try:
        with open('student_data.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(row)
            f_object.close()
            return True
    except:
        return False
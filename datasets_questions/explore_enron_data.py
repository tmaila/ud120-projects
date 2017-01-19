#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import pandas as pd
import numpy as np
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

email_count = 0
salary_count = 0
total_payments_count = 0


for k in enron_data:
    if not enron_data[k]["salary"] == "NaN":
        salary_count = salary_count + 1
    if not enron_data[k]["email_address"] == "NaN":
        email_count = email_count + 1
    if not enron_data[k]["total_payments"] == "NaN":
        total_payments_count = total_payments_count + 1
print salary_count
print email_count
print total_payments_count
print len(enron_data)
print float(total_payments_count)/len(enron_data)
print 1.0 - float(total_payments_count)/len(enron_data)

#names = ["Lay Kenneth L", "Skilling Jeffrey K", "Fastow Andrew S"]
#for name in names:
#    print enron_data[name.upper()]

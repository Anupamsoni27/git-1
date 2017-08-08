import csv
a1=""
a2=""
a3=""
f = open('list.csv')
csvfile = csv.reader(f)

for row in csvfile:
    s1_row = row[0]
if "china" in s1_row:
    a2 = "CH"
elif "japan" in s1_row:
    a2 = "JP"

if "HDPE" in s1_row:
    a1 = "HDPE_TRADE"
elif "EPS" in s1_row:
    a1 = "EPS_TRADE"

s2_row = row[1]
if "Destination" in row[1]:
    a3 = "EXPORTS"
elif "Origin" in row[1]:
    a3 = "IMPORTS"

print("EU.IHS." + a1 + "_" + a2 + "." + a3)


"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

infile = open('school_data.json', 'r')

schools = json.load(infile)
conf_schools = [372, 108, 107, 130]

#print(type(schools))

# how many schools are there in the file?

print("The total number of schools are: " , (len(schools)))
print()

print("Universities that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons and report graduation rate for Women over 75% ")
print()

for i in schools:
    if i['NCAA']['NAIA conference number football (IC2020)'] in conf_schools:
        if i['Graduation rate  women (DRVGR2020)'] > 75:
            print(f"Name of university: {i['instnm']}")
            print(f"Graduation rate for women: {i['Graduation rate  women (DRVGR2020)']}")
            print()

print("Universities that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons and total price for in-state students living off campus over $50,000")
print()

for i in schools:
    if i['NCAA']["NAIA conference number football (IC2020)"] in conf_schools:
        if i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] is not None:
            if i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
                print(f"Name of university: {i['instnm']}")
                print(f"Total price for in-state students living off campus: {i['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']}")
                print()

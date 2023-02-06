'''
      the eq_data file is a json file that contains detailed information about
      earthquakes around the world for a period of a month.

      NOTE: No hard-coding allowed except for keys for the dictionaries

      1) print out the number of earthquakes

      2) iterate through the dictionary and extract the location, magnitude, 
         longitude and latitude of the location and put it in a new
         dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
         magnitude > 6. Print out the new dictionary.

      3) using the eq_dict dictionary, print out the information as shown below (first three shown):

      Location: Northern Mid-Atlantic Ridge
      Magnitude: 6.2
      Longitude: -36.0923
      Latitude: 35.4364


      Location: 166km SSE of Muara Siberut, Indonesia
      Magnitude: 6.1
      Longitude: 100.0208
      Latitude: -2.8604


      Location: 14km ENE of Puerto Madero, Mexico
      Magnitude: 6.6
      Longitude: -92.2981
      Latitude: 14.7628

      '''



import json

infile = open('eq_data.json', 'r')

eq = json.load(infile)
   #print(type(eq))

print("The number of earthquares are: ", len(eq['features']))
print()


eq_dict1 = {}
list_eq = []
for i in range(len(eq['features'])):
   if eq['features'][i]['properties']['mag'] > 6:
      eq_dict = {}
      location = eq['features'][i]['properties']['place']
      magnitude = eq['features'][i]['properties']['mag']
      longitude = eq['features'][i]['geometry']['coordinates'][0]
      latitude = eq['features'][i]['geometry']['coordinates'][1]
      eq_dict["Location"] =  location
      eq_dict["Magnitude"] =magnitude
      eq_dict["Longitude"] = longitude
      eq_dict["Latitude"] = latitude      
      list_eq += [eq_dict]


eq_dict1['earthquakes'] = list_eq
print(eq_dict1)
print()


for i in eq_dict1['earthquakes']:     
   print("Location:", i['Location'])
   print("Magnitude:", i['Magnitude'])
   print("Longitude:", i['Longitude'])
   print("Latitude", i['Latitude'])
   print()


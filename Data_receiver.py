# this code is crap. just used as a location holder untill newer version is created


import cgi
form = cgi.FieldStorage()
kingdom =  form.getvalue('kingdom')
phylum =  form.getvalue('phylum')
clas =  form.getvalue('class')
order = form.getvalue('order')
family = form.getvalue('value')
genus =  form.getvalue('genus')
species = form.getvalue('species')
print("Kingdom = ",kingdom)
print("Phylum = ",phylum)
print("Class = ", clas)
print("Order = ",order)
print("Family = ",family)
print("Genus = ",genus)
print("Species = ",species)

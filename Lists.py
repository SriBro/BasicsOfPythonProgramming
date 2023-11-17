colleges = ["TCSC","TCET","VJTI","College of Engineering","Reva","Presidency"]
#Access 1st element of list
print(colleges[0])
#Change 4th element
colleges[3] = "COE"
#Access part of list(3rd index is excluded)
print(colleges[0:3])
#Adding another element at end
colleges.append("IIT")
#Adding element in between
colleges.insert(6,"NIT")
#Removing an element
colleges.remove("Presidency")
print(colleges)
#Adding more elements to list
print(colleges+["Stanford","Oxford"])
print(len(colleges))
print(max(colleges))
print(min(colleges))



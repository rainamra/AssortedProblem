#1
sample_data = "3, 5, 7, 23"
sample_data = sample_data.replace(",", "")
newdataArr = sample_data.split()
print("In List: ", newdataArr)
print("In Tuple: ",tuple(newdataArr))
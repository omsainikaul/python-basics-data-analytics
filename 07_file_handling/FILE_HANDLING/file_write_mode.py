a = "Om is good"  #string is given

file = open("om.txt", "w")   #om.txt file will be created automatically and "w" means it will be open in write mode
file.write(a)                #.write is used to add or write data in the file

file.close()                 #closes the file and save the changes

#by write the txt file created on it's own






#there are so many file types like:

# "r" -	Read file
# "w" -	Write (overwrites file)
# "a" -	Append (adds data)
# "x" -	Create new file
# "r+" - Read and write
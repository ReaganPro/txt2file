#create .txt files
#file name with extension = vkc
#Text = tkct
def crt(nm,tkct):
 print("creator function called")
 file=open(nm,"w+")
 file.write(tkct)
 print ('writing to the file')
 file.close()
 print (f"creating {nm} and writing to the file...")
 return True

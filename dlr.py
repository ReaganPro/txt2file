
import os

def dlt2(dk):
 os.remove(dk)
 if not os.path.exists(dk):
  print ('successfully deleted!')
  return True
 elif os.path.exists(dk):
  print ('delete failed')
  return False


def dlt(fn):
    if os.path.exists(fn):
     print("The file exists!")
     return dlt2(fn)
    elif not os.path.exists(fn):
     er1="The file does not exist."
     print(er1)
     return False
     
     

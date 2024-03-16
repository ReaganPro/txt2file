import random
chrs = ["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","J","K","L","M","N","P","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"]
def gen(lg):
 nr=int(lg)
 cv=random.choice(chrs)
 while nr>1:
  r1=random.choice(chrs)
  cv=f"{cv}{r1}"
  nr=nr-1
 return(cv)

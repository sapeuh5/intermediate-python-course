def kika():
   import random
   
   #print("Keep it logically awesome.")
   f=open("quotes.txt","a")
   f.write("Et cela c'est la fin\n")
   f.close()
   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()
   last=len(quotes)-1
   rnd=random.randint(0,last)
   rnd1=random.randint(0,last)
   print(quotes[rnd],end='')
   print(quotes[rnd1],end='')

if __name__== "__main__":
  kika()

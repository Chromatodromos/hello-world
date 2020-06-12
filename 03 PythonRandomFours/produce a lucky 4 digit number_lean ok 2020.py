#ανακάτεψε την τετράδα. r η θέση που θα τουμπάρει με τον πρώτο αριθμό
def scrabble(theInput):
    import random
    a = theInput[0]
    b = theInput[1]
    c = theInput[2]
    d = theInput[3]
    r=random.randint(0,3)
    
    if r==1:
        t=a
        a=b
        b=t
    if r==2:
        t=a
        a=c
        c=t
    if r==3:
        t=a
        a=d
        d=t
    theOutput=a+b+c+d    
    return(theOutput)

#παραγωγή αριθμών 504 για κάθε ψηφίο, συνολικά 5040 αριθμοί    
import random
guesses=[]
for a in range(0,10):
         for b in range(0,10):
               if a!=b:
                  for c in range(0,10):
                      if b!=c and a!=c:
                          for d in range(0,10):
                               if c!=d and d!=b and d!=a:
                                   guesses.append(str(a)+str(b)+str(c)+str(d))
#παραγωγή 10 τυχερών τετράδων, μία για κάθε ψηφίο 0..9
lucky=[]
theList=[]
for i in range (0,10):    
    indx=random.randint((i*504),((i*504)+503))
    lucky.append(guesses[indx])
print("-"*15)
print("Tυχερή δεκάδα")
print("-"*15)
for i in range(0,10):
    theList.append([i,scrabble(lucky[i])])
    print (theList[i])
print("-"*41)
print("Eρωτήσεις με ανακατεμένη σειρά απαντήσεων")
print("-"*41) 
#Ανακάτεψε τυχαία τη σειρά των ερωτήσεων
j=1 
for i in range(9,-1,-1):
    print("Ερώτηση:",j,"\t","[σωστή απάντηση, τετράδα απαντήσεων]",theList.pop(random.randint(0,i)))
    print()
    j+=1


      
                                   
                                   

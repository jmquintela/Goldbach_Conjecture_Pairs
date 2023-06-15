import time

import numpy as np


def closest_value(l:list, n:int):
    
    def find_index(dict, value):
        
        for key, val in dict.items():
            if val == value:
                return key
        return None

    d = {}  
    
    for i in range(len(l)):
        if (n - l[i]) >= 0:
            d[i] = n - l[i]
    
    return find_index(d, min(d.values()))


def primes(n):
    
   # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
   #prime calculation
       
   limit = n
   end = limit + 1
   composite = np.zeros(((end + 7) // 8,), dtype = np.uint8)
   
   for i in range(3, int(end ** 0.5 + 2.01)):
       
       if not (composite[i // 8] & (1 << (i % 8))):
           
           for j in range(i * i, end, i):
                            
             composite[j // 8] |= 1 << (j % 8)
               
   return np.array([2] + [i for i in range(3, end, 2)
       if not (composite[i // 8] & (1 << (i % 8)))], dtype = np.uint32)
    
   
def GolbachConjecture(n, p, debug=False):
      
  if debug : 
      
   print("Primes: {} \n".format(p))
  
  pSum = [] 

  loopIter = 0
 
  removeMax = False 
  
  maxP=[]
  
  nStart = n
       
  def GolbachConjecturePairs( p, loopIter = 0, n= 0 , maxP=[] , pSum=[], removeMax = False , nStart = 0 , debug=False ):
     
     sliceN = closest_value(p, n)
     sliceN2 = sliceN+1
     pList = p[:sliceN2]
     
     if debug : 
      
       print("n {}\n loopiter: {}\n removeMax: {} \n".format(n,loopIter,removeMax))
          
     #slice List    
     
     
     if debug :
        
       print("slice index: {}\n prime List : {}\n sliced Prime List: {} \n".format(sliceN,p, pList))  
    
     #we get ride of any MaxPrime who end up with a 1 at the end of the sum
    
     if removeMax == True:
        
       #only if Previous Solution didn't work we remove previous MAX
         
       pList = [i for i in pList if i not in maxP]
       
       if debug :
            
        print("prime List with Max removed: {} \n, maxP: {} \n: ".format(pList, maxP))  
    
     
     pListSort = sorted(pList,reverse=True)
     
     if debug :
         
      print("Sorted Prime List: {} \n".format(pListSort))  
    
     p1 = int(pListSort[0])
          
     
     if debug :
            
       print("MaxPrime P1: {} \n ".format(p1))  
     
     
     if loopIter == 0 :
       
        #We Only Append the Last Avaiblable Max on the start of the loop 
      
        maxP.append(p1)
            
     if debug :
          
        print("maxP : {} \n".format(maxP))
       
            
     pSum.append(p1)
     
        
     if debug :
       
         print("pSum : {} \n ".format(pSum))  
          
     n2 = (n - p1)
                                         
             
     if n2 != 0 :
          
         
        if len(pSum) >= 2:
          
            loopIter = 0
            removeMax = True
            pSum = []
            return GolbachConjecturePairs(p,loopIter, nStart , maxP , pSum, removeMax,nStart,debug )
        
        if n2 == 1:
          
            removeMax = True
            loopIter = 0
            pSum = []
            
            return GolbachConjecturePairs(p, loopIter, nStart, maxP , pSum, removeMax,nStart,debug )
     
        if n2 != 1:
              
             removeMax = False   
             loopIter += 1
             
             return GolbachConjecturePairs(p,loopIter, n2 , maxP ,pSum , removeMax, nStart,debug)
           
                
     if n2 == 0 :
       
       
         if len(pSum) > 2:
             
             
           loopIter = 0
           
           pSum = [] #reset the sum 
           
           RemoveMax = True #but remove the latest MaxP we added
           
           return GolbachConjecturePairs(p, loopIter, nStart , maxP , pSum, removeMax,nStart,debug)
         
         
         if len(pSum) == 2: 
             
             
           # This is our Valid Pair, got it!.
                   
           return pSum
     
  return  GolbachConjecturePairs(p, loopIter,n,maxP,pSum,removeMax ,nStart,debug)



def GolbachConjectureToN(N):
   '''This writes All the pair to the N number and gives the time it take per each one'''    
   p = primes(N)
   N = list(range(2, N+1))
   Tsum=[]
   with open('log2.txt', 'w') as f:
                
    for x in N:
             
     if x%2 == 0:
       
        prime_tic = time.perf_counter()         
        x1 = GolbachConjecture(x ,p, debug=False)
        prime_toc = time.perf_counter()
        golbachTime = prime_toc - prime_tic
        Tsum.append(golbachTime)
        
        f.write("\n Number : {} \n Pairs = {}\n RunTime = {} Secs \n ".format(x,x1,golbachTime)) 
    total = sum(Tsum)
    f.write("\n Total Time: {} Secs \n".format(total))  
                     
#n = 1000000
#print(GolbachConjectureToN(n))
    
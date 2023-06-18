import time
from random import randrange

import numpy as np


def nearestEqualOrSmallerIndex(n:int, indexSlicers, initialL, debug=False):
  
  n2 = 0
  l = initialL[indexSlicers[0]:indexSlicers[1]]
  
  if debug:
      print("index Slicers: {} \n\n l: {} \n\n n : {} \n\n ".format(indexSlicers,l,n))     
  
  for x,v in enumerate(l):
  
    IfEqual = (v == n)
    IfLess = (v < n)
    IfBigger = (v > n)

    index = indexSlicers[0] + x 
        
    if debug:
      
      conditions = []
      v2 = initialL[index]  
      conditions.append(IfEqual)
      conditions.append(IfLess)
      conditions.append(IfBigger)
      
      print("conditions : {} \n\n n: {} \n x: {} \n index: {} \n value loop: {} \n value on list: {} ".format(conditions,n,x,index,v,v2))   
   
    if IfEqual:
        n2 = index 
        break
    if IfLess:
        #we append the index of the values
        n2 = index  
        
    if IfBigger:
        n2 = index-1    
        break  
  if debug:
      print("n final: {} ".format(n2))  
 
  return n2
  #Give us the last appenden object 
       
def equalOrSmallerIndexOnListToN(n:int, l:list, debug=False):  
    # l is a sorted list
    
    lenL = len(l)
    leftSlice = 0
    rightSlice = lenL
    indexSlicers=[leftSlice,rightSlice]
    initialL = l
    d = 100
    
    def FindNearNumberbyHalfingSignComparison(d:int,n:int,lenL:int,indexSlicers:list, initialL:list,debug=False) -> list:
             
      ifNBiggerThanlenL = ( initialL[-1] <= n)    
      if ifNBiggerThanlenL:    
        return lenL-1        
      ifLenNLessorEqualltoD = (lenL <= d)
       
      if  ifLenNLessorEqualltoD:    
        #we short the loop when we reach d element        
        return nearestEqualOrSmallerIndex(n,indexSlicers,initialL,debug)          
      
      #We pick a random position on this range  
                       
      random = int(randrange(lenL-1))
      
      index = indexSlicers[0] + random
      value = initialL[index] 
      conditions=[]
       
      IfBigger = ( value < n)
      IfEqual = (value == n)
      IfLess = ( value > n)
      
      if debug:
        
       conditions.append(IfBigger)
       conditions.append(IfEqual)
       conditions.append(IfLess)
       print( "lenL : {}, n: {} \n Conditions: {} \n Value :  {}\n Index :  {}  \n Slicing index : {} \n".format(lenL,n,conditions,value,index,indexSlicers) )
  
      if IfEqual:
    
         return  index
        
      if IfBigger:
        
         indexSlicers[0] = index          
         l = initialL[indexSlicers[0]:indexSlicers[1]]
         lenL = len(l)
         
         return FindNearNumberbyHalfingSignComparison(d,n, lenL,indexSlicers, initialL, debug )
      
      #and slice the parts from the array that are   

      if IfLess:
         indexSlicers[1] = index                   
         l = initialL[indexSlicers[0]:indexSlicers[1]]
         lenL = len(l)
         return FindNearNumberbyHalfingSignComparison(d,n , lenL ,indexSlicers, initialL, debug)
      
      
    return FindNearNumberbyHalfingSignComparison(d, n, lenL, indexSlicers, initialL, debug )
   
def primes(n):
   # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
       
   limit = n
   end = limit + 1
   composite = np.zeros(((end + 7) // 8,), dtype = np.uint8)
   
   for i in range(3, int(end ** 0.5 + 2.01)):       
       if not (composite[i // 8] & (1 << (i % 8))):      
           for j in range(i * i, end, i):                        
             composite[j // 8] |= 1 << (j % 8)
               
   return np.array([2] + [i for i in range(3, end, 2)
       if not (composite[i // 8] & (1 << (i % 8)))], dtype = np.uint32)
    
def goldbachConjecture(n, p, debug=False):
      
  if debug :       
   print("Primes: {} \n".format(p))  
  pSum = [] 
  loopIter = 0 
  removeMax = False   
  maxP=[]  
  nStart = n  
  
  def goldbachConjecturePairs( p, loopIter = 0, n = 0 , maxP=[] , pSum=[], removeMax = False , nStart = 0 , debug=False ):     
    
     if nStart<=2:
      return [2]
     sliceN = equalOrSmallerIndexOnListToN(n,p,debug)
     if debug:
      print("N Pair number : {} \n current n : {} \n Index on p(sliceN): {} \n p[sliceN] : {} \n pList = p[:sliceN+1] : {}\n  ".format(nStart,n,sliceN,p[sliceN], p[:sliceN+1]  ))
     pList = p[:sliceN+1]   
     if debug :       
       print("n {}\n loopiter: {}\n removeMax: {} \n".format(n,loopIter,removeMax))          
     #we get ride of any MaxPrime who end up with a 1 at the end of the sum  
     if removeMax == True:
       #only if Previous Solution didn't work we remove previous MAX     
       pList = [i for i in pList if i not in maxP]     
       if debug :           
        print("prime List with Max removed: {} \n, maxP: {} \n: ".format(pList, maxP))      
     pListSort = sorted(pList,reverse=True)    
      
     if debug :     
      print("Sorted Prime List: {} \n".format(pListSort))    
     p1 = pList[-1]
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
            return goldbachConjecturePairs(p,loopIter, nStart , maxP , pSum, removeMax,nStart,debug )       
        if n2 == 1:          
            removeMax = True
            loopIter = 0
            pSum = []            
            return goldbachConjecturePairs(p, loopIter, nStart, maxP , pSum, removeMax,nStart,debug )   
        if n2 != 1:        
             removeMax = False   
             loopIter += 1
             return goldbachConjecturePairs(p,loopIter, n2 , maxP ,pSum , removeMax, nStart,debug)                       
     if n2 == 0 :
  
         if len(pSum) > 2:
           loopIter = 0
           pSum = [] #reset the sum 
           removeMax = True #but remove the latest MaxP we added
           return goldbachConjecturePairs(p, loopIter, nStart , maxP , pSum, removeMax,nStart,debug)      
         if len(pSum) == 2:      
           # This is our Valid Pair, got it!.
           MaxPLen= int(len(maxP))
           if debug:
            print("n: {}\nMaxP : {} \nPsum: {}\n".format(nStart,MaxPLen,pSum))
           return pSum
         
  return  goldbachConjecturePairs(p, loopIter,n,maxP,pSum,removeMax ,nStart,debug)

def goldbachConjecturePair(n:int,debug=False):
  
   '''This writes on pair each one'''   
   prime_tic = time.perf_counter()  
   p = primes(n)
   prime_toc = time.perf_counter()
   primeTime = prime_toc - prime_tic
   print("prime list runTime: {} \n".format(primeTime))
   n = list(range(2, n+2,2))
   nAndPairs=[]
   runTime=[]
   
   for e,x in enumerate(n):
     gold_tic = time.perf_counter()   
     x1 = goldbachConjecture(x,p,debug)
     gold_toc = time.perf_counter()
     itemTime = gold_toc - gold_tic
     runTime.append(itemTime)
     nAndPairs.append(x)
     nAndPairs.append(x1)
     if debug:
      print("\n Number : {} \n Pairs = {}\n RunTime = {} Secs \n".format(x,x1,itemTime))                     
              
   return runTime,nAndPairs      
             
n = 100000
debug=False
t,p = goldbachConjecturePair(n , debug)

print("Goldbach prime pairs sums: {} \n total Run Time: {} seconds \n".format(p,sum(t)))
#print("total Run Time: {} seconds \n Prime List: {}".format(sum(t),p))
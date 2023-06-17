import time

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
    v2 = initialL[index]  
    
    if debug:
      conditions = []
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
       
def equalorSmallerIndexOnListToN(n:int, l:list, debug=False):
    
    # l is a sorted list
    lenL = len(l)
    leftSlice = 0
    rightSlice = lenL
    indexSlicers=[leftSlice,rightSlice]
    initialL = l
    d = 100
  
    def findNearNumberbyHalfingSignComparison(d:int,n:int,lenL:int,indexSlicers:list, initialL:list,debug=False) -> list:
             
      ifNBiggerThanlenL = ( initialL[-1] <= n)    
      if ifNBiggerThanlenL:    
        return lenL-1
      ifLenNLessorEqualltoD = (lenL <= d)
      if  ifLenNLessorEqualltoD:    
        #we short the loop when we reach d element        
        return nearestEqualOrSmallerIndex(n,indexSlicers,initialL,debug)          
            
      half = int(lenL/2)
      index = indexSlicers[0] + half
      value = initialL[index] 
      
       
      IfBigger = (n > value)
      IfEqual = (n == value)
      IfLess = (n < value)
      
      if debug:
       conditions=[]
       conditions.append(IfBigger)
       conditions.append(IfEqual)
       conditions.append(IfLess)
       print( "lenL : {}, n: {} \n Conditions: {} \n Value :  {}\n Index :  {}  \n Slicing index : {} \n".format(lenL,n,conditions,value,index,indexSlicers))
      
      if IfEqual:    
         return  index   
      if IfBigger:
         indexSlicers[0] = index          
         l = initialL[indexSlicers[0]:indexSlicers[1]]
         lenL = len(l)
         
         return findNearNumberbyHalfingSignComparison(d,n, lenL,indexSlicers, initialL, debug )  

      if IfLess:
         indexSlicers[1] = index                   
         l = initialL[indexSlicers[0]:indexSlicers[1]]
         lenL = len(l)
         return findNearNumberbyHalfingSignComparison(d,n , lenL ,indexSlicers, initialL, debug)

    return findNearNumberbyHalfingSignComparison(d, n, lenL, indexSlicers, initialL, debug )
    
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
    
def golbachConjecture(n, p, debug=False):
      
  if debug :       
   print("Primes: {} \n".format(p))  
  pSum = [] 
  loopIter = 0 
  removeMax = False   
  maxP=[]  
  nStart = n  
  def golbachConjecturePairs( p, loopIter = 0, n = 0 , maxP=[] , pSum=[], removeMax = False , nStart = 0 , debug=False ):     
     sliceN = equalorSmallerIndexOnListToN(n,p,debug)
     sliceN2 = sliceN+1
     pList = p[:sliceN2]     
     if debug :       
       print("n {}\n loopiter: {}\n removeMax: {} \n".format(n,loopIter,removeMax))          
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
            return golbachConjecturePairs(p,loopIter, nStart , maxP , pSum, removeMax,nStart,debug )       
        if n2 == 1:          
            removeMax = True
            loopIter = 0
            pSum = []            
            return golbachConjecturePairs(p, loopIter, nStart, maxP , pSum, removeMax,nStart,debug )   
        if n2 != 1:        
             removeMax = False   
             loopIter += 1
             return golbachConjecturePairs(p,loopIter, n2 , maxP ,pSum , removeMax, nStart,debug)                       
     if n2 == 0 :
  
         if len(pSum) > 2:
       
           loopIter = 0
           pSum = [] #reset the sum 
           removeMax = True #but remove the latest MaxP we added
           return golbachConjecturePairs(p, loopIter, nStart , maxP , pSum, removeMax,nStart,debug)      
         if len(pSum) == 2:      
           # This is our Valid Pair, got it!.
           return pSum   
  return  golbachConjecturePairs(p, loopIter,n,maxP,pSum,removeMax ,nStart,debug)

def golbachConjecturePair(n:int,debug=False):
  
   '''This writes on pair each one'''   
   prime_tic = time.perf_counter()  
   p = primes(n)
   prime_toc = time.perf_counter()
   n = list(range(2, n+1,2))
   nAndPairs=[]
   runTime=[]
   for e,x in enumerate(n):
     prime_tic = time.perf_counter()   
     x1 = golbachConjecture(x ,p, debug)
     gold_toc = time.perf_counter()
     itemTime = prime_toc - prime_tic
     runTime.append(itemTime)
     nAndPairs.append(x)
     nAndPairs.append(x1)
     if debug:
      print("\n Number : {} \n Pairs = {}\n RunTime = {} Secs \n ".format(x,x1,itemTime)) 
   
   total = sum(runTime)                  
   print(total)              
   return runTime,nAndPairs      
             
n = 1000000

print(golbachConjecturePair(n , debug=False))

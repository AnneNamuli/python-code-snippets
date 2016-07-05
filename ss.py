def find_missing(A, B):
  
  switch, long_ , short = False, 0, 0
  
  long_ = max(len(A), len(B))
  short = min(len(A), len(B))
  
  A.sort()
  B.sort()
  longArray, shortArray = [], []
  if (long_ == 0 and short == 0) or (long_ == short):
    return 0
    
  if (len(B) > len(A)):
    longArray = B
  else:
    longArray = A
   
  if (len(B) > len(A)):
    shortArray = A
  else:
    shortArray = B
  
  for j in range(short):
    if longArray[i] == shortArray[i]:
      switch = True
  if switch == False:
    return longArray[j]
      
      
      
print(find_missing([4,66,7], [66, 77, 7, 4]))
def addup(first, last, incr=1):
 if first > last:
     sum = -1
 else:
     sum=0
 for i in range(first,last+1, incr):
     sum=sum+i
 return sum

print(addup(1,10,2))

#!/usr/bin/env python
a = [90,55,37,36,14,20,74,68,34,10]

print("Old A: {}".format(a))
for i in range(len(a)-1):
  if(a[i] < a[i+1]):
    a[i+1],a[i] = a[i],a[i+1]
  for n in range(len(a)-1):
    if(a[n] < a[n+1]):
      a[n+1],a[n] = a[n],a[n+1]
print("New A: {}".format(a))

# Bubble-sort

$cat -n bsort.py
     1  #!/usr/bin/env python
     2  a = [90
     3  ,55
     4  ,37
     5  ,36
     6  ,14
     7  ,20
     8  ,74
     9  ,68
    10  ,34
    11  ,10]
    12  print("Old A: {}".format(a))
    13  for i in range(len(a)-1):
    14    if(a[i] < a[i+1]):
    15      a[i+1],a[i] = a[i],a[i+1]
    16    for n in range(len(a)-1):
    17      if(a[n] < a[n+1]):
    18        a[n+1],a[n] = a[n],a[n+1]
    19  print("New A: {}".format(a))
$./bsort.py
Old A: [90, 55, 37, 36, 14, 20, 74, 68, 34, 10]
New A: [90, 74, 68, 55, 37, 36, 34, 20, 14, 10]
$


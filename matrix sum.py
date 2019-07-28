#Initialize matrix a
a=[[1, 3, 5],
  [2, 6, 7],
  [6, 8, 9]]

#Calculates number of rows and columns present in given matrix  

rows=len(a)
cols=len(a[0])

#Calculates sum of each row of given matrix  

for i in range(0,rows):
   sumrow=0
   for j in range(0,cols):
       sumrow=sumrow+a[i][j]
   print("sum of "+ str(i+1) +" rows: " + str(sumrow))

#Calculates sum of each column of given matrix  

for i in range(0,rows):
   sumcol=0
   for j in range(0,cols):
       sumcol+=a[j][i]
   print("sum of "+ str(i+1) +" cols: " + str(sumcol))


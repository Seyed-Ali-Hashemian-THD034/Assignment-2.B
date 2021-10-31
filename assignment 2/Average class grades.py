#Average class grades 
import math

count = int( input('How many students do you have?'))

grade = []

for i in range(count) :
   lesson = float(input(' enter Coding class scores :'))
   grade.append( lesson)

x = sum (grade)
average = x / count
print ('Average:' , average )       # Average class grades 

maximom = max (grade)
print ('max:' , maximom )           # Max score  

minimom = min (grade)
print ('min:' , minimom )           # Min score 
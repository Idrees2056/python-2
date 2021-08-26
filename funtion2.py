#swapping the files
from os import read


z=open("text.txt","r")
k=z.read()

f=open("text2.txt","r")
d=f.read()

z=open("text.txt","w")
z.write(d)

f=open("text2.txt","w")
f.write(k)
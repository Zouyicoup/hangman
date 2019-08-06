#1

# Filepath=os.path.join("Documents","Yi's Folder","X1393 other tests","Zach yarn tensile","Raw data","Specimen_RawData_1.csv")
#Filepath=os.path.join("~‎⁨Users","yizou","Documents","Python","RawData_1.csv")

import os
import csv

CSV_filepath = os.path.expanduser("~/Desktop/RawData_1.csv")

with open(CSV_filepath, "r") as f:
    r=csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

#2
a=input("give me a answer: ")

with open("answer.txt", "w") as f:
    f. write(a)
    f. write(a*2)

import csv
with open ("answer.csv", "w") as f:
    w=csv.writer(f, delimiter=",")
    w.writerow(a)
    w.writerow(a*2)

    
#3

movies=[["sfd","dfgd","hsrdgf"],[1,2,3],["er","sfd",4]]
print(movies)
import csv
with open("movie.csv","w") as f:
    w=csv.writer(f, delimiter=",")
    w.writerow(movies)

with open("movie2.csv","w") as f:
    w=csv.writer(f, delimiter=",")
    for row in movies:
        w.writerow(row)

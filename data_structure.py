#data structure
#collection
#list ,dictionary ,set
scores=[90 ,78,56 ,84, 80 ,23 ,34 ,23 , 67 ,64 ,67 , 26,89]
#access a score
print(scores [0])
print(scores [1])

#add scores
scores.append(51)
print(scores )

#remove
scores.remove(78)
print(scores )

print(len(scores))

print(scores.count(23))

scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)

# slice a list
top_5 = scores[1:5]
print(top_5)

#slicing a list in python

#dictionary

person ={ "name" :"Veronicah", "age":18 ,"county":"Nairobi"}
print(person ["name"])
print(person ["age"])


#set
days={ "mon" , "tue" , "wed" , "thu" , "fri" }
print(days)

for s in scores:
    if s < 50:
      print(s)














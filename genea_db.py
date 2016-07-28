from py2neo import Node, Relationship, Graph, authenticate
import string
import random
from titlecase import titlecase
#import numpy as np
#import json


#(give your  "localhost/neo4j userName/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")

Author_name=[]
Author_id=[]
#Citation_matrix=np.empty((45,45))

Matrix = [[0 for x in range(45)] for y in range(45)] 

def Author_Generator(size=6, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size))) + " " + titlecase(''.join(random.choice(chars) for _ in range(size))) 
#for i in range(0,5):
#	Author_Generator()


	#a = Author_Generator()
	#a1=a
	#a = graph.merge_one("Author", "Name",a1 )

#r1 = random.randint(0,10)
for i in range(0,40):
	Author_name.append(Author_Generator())
	Author_id.append((i))
	a=Node("Author", ID=Author_id[i],Name=Author_name[i])
	#a.properties["Name"]=Author_name[i]
	graph.merge(a)


for i in range(0,5):
	r1 = random.randint(0,40)
	Author_id.append((i+40))
	Author_name.append(Author_name[r1])
	a=Node("Author", ID=Author_id[i+40],Name=Author_name[i+40])
	graph.merge(a)

for i in range(0,45):
	for j in range(0,45):
		r1 = random.randint(0,50)
		r2 = random.randint(5,25)
		if i == j:
			Matrix[i][j]=r2
			
		else:
			Matrix[i][j]=r1
			
#for i in Author_id:
	#print (Author_id[i],' ',Author_name[i],' ', i)
#print (Author_id)
#print (Matrix)
j=1
i=0

while (j < 40):
 	
	#a=Relationship(Author_id[i], "Advisor_of",Author_id[j])
	#graph.merge(a)
	q1="MATCH (n:Author{ID:"+str(Author_id[i])+"}),(m:Author{ID:"+str(Author_id[j])+"})  CREATE UNIQUE (n)-[:Advisor_of{Wt:1}]->(m)"
	graph.evaluate(q1)
	j+=1
	#b=Relationship(Author_id[i], "Advisor_of",Author_id[j])
	#graph.merge(b)
	q1="MATCH (n:Author{ID:"+str(Author_id[i])+"}),(m:Author{ID:"+str(Author_id[j])+"})  CREATE UNIQUE (n)-[:Advisor_of{Wt:1}]->(m)"
	graph.evaluate(q1)
	i+=1
	j+=1


for i in range(40,44):
	r1 = random.randint(5,35)
	#a=Relationship(Author_id[i], "Advisor_of",Author_id[r1])
	#graph.merge(a)




	#q1="MATCH (n:Author)-[:Lives_in]->(Country {name:'"+x+"'}) RETURN n.name"
	#res=graph.cypher.execute(q1)

	print(r1)
	q1="MATCH (n:Author{ID:"+str(Author_id[i])+"}),(m:Author{ID:"+str(Author_id[r1])+"})  CREATE UNIQUE (n)-[:Advisor_of{Wt:2}]->(m)"
	graph.evaluate(q1)
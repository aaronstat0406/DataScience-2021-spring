
data=open("IMDB-Movie-Data.csv","r")
list1=[]
for line in data:
	list1.append(line.strip())
data.close()
for i in range(len(list1)):
	list1[i]=list1[i].split(",")  
#初始資料


#以下為備忘錄:
#========================================================
#list1[]= 初步整理的資料(1001*11,含變數名稱 ,第四題後被去掉)
#actors_1=[] 每部電影的演員list(1000*4?)
#actors_new=[] 不重複的演員名單
#director_1=[] 不重複的導演清單
#co_actors=[] 導演合作過的演員清單

#注意:
#賦值時,be cautious 空list是沒有index可以提取,所以用append

#(1)
rating=[]
for i in range(1,len(list1)):
	if list1[i][5]=="2016":
		rating.append(list1[i][7]) #create 2016所有電影rating的list
t3rating=rating[0:3] #找出前三高的排名
t3movies=[] 
for i in range(1,len(list1)):
	if list1[i][7] in t3rating and list1[i][5]=="2016": 
		t3movies.append(list1[i][1])

print("=======================================================================")
print("Top-3 movies with the highest ratings in 2016")
for i in range(len(t3movies)):
	print(t3movies[i])

#(2)
actors_1=[]
for i in range(1,len(list1)):
	actors_1.append(list1[i][4])
for i in range(len(actors_1)):
	actors_1[i]=actors_1[i].replace("| ","|")
	actors_1[i]=actors_1[i].split("|") 

actors_new=[]
for i in range(len(actors_1)):
	for j in range(len(actors_1[i])):
		if actors_1[i][j] not in actors_new:
			actors_new.append(actors_1[i][j])

print(len(actors_new))  #不重複的演員名單

revenue_all=[] #存所有不重複演員的revenue
for i in range(len(actors_new)):
	temp_rev=[] #暫存某演員的所有revenue
	#temp_rev_avg=[] #暫存某演員的平均revenue
	for j in range(1,len(list1)):
			if actors_new[i] in list1[j][4]:
				if list1[j][9]!="":
					temp_rev.append(float(list1[j][9])) #將revenue以float串接
	if len(temp_rev)==0:   #遺失的revenue
		revenue_all.append(0) 
	else:
		revenue_all.append(sum(temp_rev)/len(temp_rev))
#print(revenue_all)
m=max(revenue_all) #找最大值
print("===========================================================")
print("The actor generating the highest average revenue? ")
for i in range(len(revenue_all)):
	if revenue_all[i]==m:
		print(actors_new[i])

#(3)
emma_rating=[]
name="Emma Watson"
for i in range(1,len(list1)):
	if name in list1[i][4]:
		rate=float(list1[i][7])
		emma_rating.append(rate) #製造Emma's rating的list
print("=======================================================================")
print("The average rating of Emma Watson's movies")
print(sum(emma_rating)/len(emma_rating))

#(4)
director_1=[]
director_1.append(list1[1][3])
for i in range(1,len(list1)):
	judge=0 #判斷
	j=0
	while j <len(director_1):
		if list1[i][3]==director_1[j]:
			judge=1 #當有導演重複 
		j=j+1
	if judge==0:
		director_1.append(list1[i][3])	
#print(director_1) #director不重複的清單

del list1[0] #去掉變數名稱
co_actors=[]
for i in range(len(director_1)):
	temp=[]
	for j in range(len(actors_1)):
		if list1[j][3]==director_1[i]:
#			print(director_1[i],":",j,actors_1[j])
			for k in range(len(actors_1[j])):
				if actors_1[j][k] not in temp:
					temp.append(actors_1[j][k])
	co_actors.append(len(temp))
#print(co_actors)

TOP_3 = [0 for i in range(3)]
T_index = [0 for i in range(3)]

for i in range(len(co_actors)):
	for j in range(3):
		if co_actors[i] > TOP_3[j]:
			del TOP_3[2]
#			del T_index[2]
			TOP_3.insert(j, co_actors[i])
#			T_index.insert(j,i)
			break

print("=======================================================================")
print("Top-3 directors who collaborate with the most actors")
for i in range(3):
	for j in range(len(co_actors)):
		if co_actors[j] == TOP_3[i]:
			print(TOP_3[i],":",director_1[j])
#print(TOP_3)

#(5)
genre_fix=[]
for i in range(len(list1)):
	genre_fix.append(list1[i][2])
for i in range(len(genre_fix)):
	genre_fix[i]=genre_fix[i].replace("| ","|")
	genre_fix[i]=genre_fix[i].split("|") 
#print(genre_fix) #二維list

num_genre=[]
for i in range(len(actors_new)):
	save=[]
	for j in range(len(list1)):
		if actors_new[i] in list1[j][4]:
			for k in range(len(genre_fix[j])):
				if genre_fix[j][k] not in save:
					save.append(genre_fix[j][k])	
	num_genre.append(len(save))
	#print(num_genre)
#print(len(num_genre))
print("=======================================================================")
print("Top-2 actors playing in the most genres of movies?")


for i in range(2):
	top=max(num_genre)
	for j in range(len(actors_new)):
		if top==num_genre[j]:
			print(actors_new[j],":",num_genre[j])
			num_genre[j]=min(num_genre) #把原先的最大值改為最小值，避免出事

#(6)
for i in range(len(list1)):  #整理list1中的演員清單
	list1[i][4]=list1[i][4].replace("| ","|")
	list1[i][4]=list1[i][4].split("|")

#print(len(list1)) 1000
#print(len(actors_new)) 1985
gap_year=[]

for i in range(len(actors_new)):
	year=[]
	for j in range(len(list1)):
		if actors_new[i] in list1[j][4]:
				year.append(int(list1[j][5])) #放入所有電影的年分
	if len(year)==0:
		gap_year.append(0) #只演過一部電影演員的gap=0
	else:
		gap_year.append(max(year)-min(year))
#print(gap_year)
#print(len(gap_year))
print("=======================================================================")
print("Top-3 actors whose movies lead to the largest maximum gap of years")

num = 0
for i in range(3):  #同第五題做法
	top=max(gap_year)
	for j in range(len(actors_new)):
		if top==gap_year[j]:
			print(actors_new[j],":",gap_year[j])
			num+=1
			gap_year[j]=min(gap_year)
	if num >= 3:
		break

#(7)
dir_and_indir=[] #
joh="Johnny Depp"
dir=[]
"""
for i in range(len(list1)):
	for j in range(len(list1[i][4])):
		if joh in list1[i][4] and list1[i][4][j] not in dir: 
			dir.append(list1[i][4][j])
dir.remove(joh)
"""
#print(dir) #direct actors work with Johnny
dir.append(joh)

#def dir_func(directs):
judge=1
while judge>0:
	start=len(dir)
	for i in range(len(dir)):
		for j in range(len(list1)):
			for k in range(len(list1[j][4])):
				if dir[i] in list1[j][4] and list1[j][4][k] not in dir:
					dir.append(list1[j][4][k])
					#dir_func(list1[j][4][k])
	end=len(dir) #檢查一輪
	judge=end-start

dir.remove(joh) 
print("=======================================================================")
print("all actors who collaborate with Johnny Depp in direct and indirect ways")
for i in range(len(dir)):
	print(dir[i])

print("total",":",len(dir))
#print(count)





"""
for i in range(len(dir)):
	indir=[]
	for j in range(len(list1)):
		for k in range(len(list1[j][4])):
			if dir[i] in list1[j][4] and list1[j][4][k] not in indir:
				indir.append(list1[j][4][k])
	#print(indir) # direct workers對應的 indirect workers
	dir_and_indir.append(dir[i])
	for m in range(len(indir)):
		if indir[m] not in dir_and_indir:
			dir_and_indir.append(indir[m]) #dir[i],indir[m] 丟到 dir_and_indir 
"""




#print(dir_and_indir)



"""
for i in range(len(actors_new)):
	dir=[]
	for j in range(len(list1)):
		if actors_new[i] in list1[j][4]:
			for k in range(len(list1[j][4])):
				if actors_new[i]!=list1[j][4][k] and list1[j][4][k] not in dir: 
					dir.append(list1[j][4][k]) 
	#print(dir) #actors_new[i]的不重複的合作演員名單
	indir=[]
	for m in range(len(dir)):
		for j in range(len(list1)):
			if dir[m] in list1[j][4]:
				for k in range(len(list1[j][4])):
					if dir[m]!=list1[j][4][k] and list1[j][4][k] not in indir:
						indir.append(list1[j][4][k]) 
	if actors_new[i] in indir:
		indir.remove(actors_new[i])
	#print(indir)
	dir_and_indir.append(len(indir))
#print(dir_and_indir)
"""

	


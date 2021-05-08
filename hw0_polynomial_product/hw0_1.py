# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:28:36 2021

@author: Aaron Lin
"""
def multiply(poly_1,poly_2): #副程式呼叫
	#poly_1=poly_n[i]
	#poly_2=poly_n[i+1]
	
	temp_sign=[]
	for j in range(len(poly_1)):
		for k in range(len(poly_2)):
			sign=0
			if poly_1[j][0]=="+" and poly_2[k][0]=="+":  #判斷+-號
				sign+=1
			if poly_1[j][0]=="-" and poly_2[k][0]=="-":  
				sign+=1
			if poly_1[j][0]=="+" and poly_2[k][0]=="-":  
				sign-=1
			if poly_1[j][0]=="-" and poly_2[k][0]=="+":  
				sign-=-1
			temp_sign.append(sign)
	#print(temp_sign) #各多項式的係數,第一輪相乘後出現000000? 注意datatype
	
	multi=[] #save兩個()內poly相乘整理的結果
	
	temp_poly_1=[]
	print(poly_1)
	for j in range(len(poly_1)):
		space1=[]
		space1+=27*[0] #space
		a1=poly_1[j].find("*")
		a2=poly_1[j].find("^")
		#print(poly_1[j][1:a1])
		space1[0]=int(poly_1[j][1:a1]) #係數
		for k in range(len(poly_1[j])):
			if 65<=ord(poly_1[j][k])<=90:
				space1[ord(poly_1[j][k])-64]=int(poly_1[j][k+2])
		temp_poly_1.append(space1)

	#print(temp_poly_1)

	temp_poly_2=[]
	print(poly_2)
	for l in range(len(poly_2)):
		space2=[]
		space2+=27*[0]
		b1=poly_2[l].find("*")
		b2=poly_2[l].find("^")
		space2[0]=int(poly_2[l][1:b1])
		for m in range(len(poly_2[l])):
			if 65<=ord(poly_2[l][m])<=90:
				space2[ord(poly_2[l][m])-64]=int(poly_2[l][m+2])
		temp_poly_2.append(space2)
	#print(temp_poly_2)

	n1=0 #處理係數的正負號
	n=len(poly_1)*len(poly_2)
	for i in range(len(temp_poly_1)):
		for j in range(len(temp_poly_2)):
			temp=[]
			for k in range(27):
				if k==0:
					temp.append(temp_poly_1[i][k]*temp_poly_2[j][k])
					while n1<n:
						if temp_sign[n1]==-1:  #係數有負號,記得要補
							temp[0]=int("-"+str(temp[0]))

							n1+=1
							break
						else:
							n1+=1
							break
				else:
					temp.append(temp_poly_1[i][k]+temp_poly_2[j][k])
			#print(temp) #任兩個()中的string 相乘的結果

			multi.append(temp)

	print(multi) #二維list,len=poly_1*poly*2,每個multi[i]有27個index(待合併)
	multi_str=[]
	for i in range(len(multi)):
		temp=""
		if multi[i][0]>0:
			temp+="+"
		temp=temp+(str(multi[i][0]))+"*"
		
		for j in range(1,len(multi[i])):
			if multi[i][j]!=0:
				temp=temp+str(chr(j+64))+"^"+str(multi[i][j])
		temp+="$"
		multi_str.append(temp)		
	return multi_str


poly=input("Please input polynomial:")
poly=poly.strip("(")
poly=poly.strip(")")
poly=poly.split(")(")
print(poly)
i=0
poly_n=[]  
#poly_n=[0 for i in range(len())]
#for _ in range(len(poly)):
   # poly_n.append(0)
#print(poly_n)

for i in range(len(poly)):
    poly_n.append(0) #獲得一個新空間
    poly_n[i]=poly[i].replace("+"," +")
    poly_n[i]=poly_n[i].replace("-"," -")
    poly_n[i]=poly_n[i].split(" ")

#print(poly_n) #製造一個二維list
for i in range(len(poly_n)):
	for j in range(len(poly_n[i])):
		poly_n[i][j]+="$" #終止字元
		if 65<=ord(poly_n[i][j][0])<=90: #出現A-Z
			poly_n[i][j]="+1*"+poly_n[i][j][0:]
		if poly_n[i][j][0]=="+" and 65<=ord(poly_n[i][j][1])<=90:
			poly_n[i][j]="+1*"+poly_n[i][j][1:]
		if poly_n[i][j][0]=="-" and 65<=ord(poly_n[i][j][1])<=90:
			poly_n[i][j]="-1*"+poly_n[i][j][1:]
		if 48<=ord(poly_n[i][j][0])<=57: #出現0-9常數
			poly_n[i][j]="+"+poly_n[i][j]
		if 65<=ord(poly_n[i][j][-2])<=90: 
			poly_n[i][j]=poly_n[i][j][:-1]+"^1$"
		for k in range(len(poly_n[i][j])):
			if 65<=ord(poly_n[i][j][k])<=90 and 65<=ord(poly_n[i][j][k+1])<=90:
				poly_n[i][j]=poly_n[i][j][0:k+1]+"^1"+poly_n[i][j][k+1:]
			 

#print(poly_n) #格式化
# *=star ^=power $=dollar

for i in range(len(poly_n)-1): #相乘的次數為總括號數-1
	poly_n[i+1]=multiply(poly_n[i],poly_n[i+1])
#做出multi後,得到的是各多項式相乘後的係數 以及A-Z的power,要把他重新整合成原本poly_1(同項合併)
#這樣才能繼續用副程式計算


final_poly=poly_n[-1] #為包含多個不等長的string的list 
print(final_poly) 
output=""
#output 需要符合:
#1.同變數且同次數可合併 (照原本list index的順序即可)
#2.不同變數之間的*原本就已忽略
#3.power為1可省略
#4.不同項以+或-連接
for i in range(len(final_poly)):
	final_poly[i]=final_poly[i].split("*")
print(final_poly)
# 二維list

output=""
for i in range(len(final_poly)):
	temp_str=final_poly[i][1]
	temp=[final_poly[i][0],temp_str]
	n=i+1
	while n<len(final_poly):
		if temp_str==final_poly[n][1]: #有重複的var
			temp[0]=str(int(final_poly[i][0])+int(final_poly[n][0]))
			if int(temp[0])>0:
				temp[0]="+"+temp[0]
		n=n+1
	temp[1]=temp[1].replace("$","")
	temp[1]=temp[1].replace("^1","")

	if temp[0]=="+1":
		temp[0]="+"
	if temp[0]=="-1":
		temp[0]="-"
	if temp[0]=="+" or temp[0]=="-":
		output+=temp[0]+temp[1]
	else:
		output+=temp[0]+"*"+temp[1]

if output[0]=="+":
	output=output[1:]


print("=====================================================================")
print("Output Result",":",output)



"""
	if i==0:
		temp[0]=temp[0].replace("+","")
	if i>0:
		temp[0]=temp[0].replace("+1","+")
		temp[0]=temp[0].replace("-1","-")
	"""

	#output+=temp[0]+"*"+temp[1]
	#print(temp)




"""
for i in range(len(final_poly)):
	temp=[]
	while n<len(final_poly):
		
	for j in range(i,len(final_poly)):
		if final_poly[i][2]==final_poly[j][2]:
			final_poly[i][1]=str(int(final_poly[i][1])+int(final_poly[j][1]))
			del final_poly[j]
print(final_poly)


"""
"""
var=[] #測試變數
for i in range(len(final_poly)):
	temp=""
	#for j in range(len(final_poly[i])):
	a=final_poly[i].find("*")   #every string has only one "*" and "$"
	b=final_poly[i].find("$") # so we can use it to test whether the variables are same 
	var.append(final_poly[i][a:b])

sub="^1"
for i in range(len(var)):
	if sub in var[i]:
		var.remove(sub)
print(var) #尚有重複變數
"""
"""
final=[]
for i in range(len(var)):
	if var[i] not in final:
		final.append(var[i])
		#print(0)

	else:
		#print(1)
		n=final.find(var[i]) #重複變數的index
		fianl[n]=str(int(fianl[n][0:2])+int(fianl_poly[i][0:2]))+final[n][2:]
print(final)
"""

"""

"""
"""
#def delvar(var):
	#new=[]
	#for i in var:
		#if i not in new:
			#new.append(fianl_poly[i][0:a])
			#new.append(i)
	#print(delvar(var))

	#return new
"""









"""

"""
"""
	for j in range(len(poly_n[i])):
		co=[]
		var=[]
		power=[]
		a1=poly_n[i][j].find("*")
		a2=poly_n[i][j].find("^")
		a3=poly_n[i][j].find("$")
		for k in range(len(poly_n[i+1])): #poly_n[i],poly_n[i+1]長度不一定相同
			co_temp=[]
			var_temp=[]
			power_temp=[]	
			b1=poly_n[i+1][k].find("*")
			b2=poly_n[i+1][k].find("^")
			b3=poly_n[i+1][k].find("$")
			c1=int(poly_n[i][j][1:a1])*int(poly_n[i+1][k][1:b1]) #係數
			c2=poly_n[i][j][a1+1:a2]+poly_n[i+1][k][b1+1:b2]     #未知數
			c3=int(poly_n[i][j][a2+1:a3])+int(poly_n[i+1][k][b2+1:b3]) #次方
			co_temp.append(c1)
			var_temp.append(c2)
			power_temp.append(c3)
			print(co_temp)
			print(var_temp)
			print(power_temp)
"""

		




	





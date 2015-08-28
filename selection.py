'''
Author:		Veerendra
Desription:	Selection Sort
'''
def selection_srt(lst): 
	for i in range(len(lst)-1):
		index=i
		for j in range((i+1),len(lst)):
			if(lst[j]<lst[index]):
				index=j
		temp=lst[i]
		lst[i]=lst[index]
		lst[index]=temp

lst=[1,2,4,568,7,3,2,6]
selection_srt(lst)
print(lst)

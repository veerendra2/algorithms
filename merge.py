'''
Author: 	Veerendra
Desciption:	Merge Sort
'''
def merge_srt(lst):
	if(len(lst)>1):
		mid=len(lst)//2
		left=lst[:mid]
		right=lst[mid:]
		merge_srt(left)
		merge_srt(right)
		i,j,k=0,0,0
		while(len(right)>i and len(left)>j):
			if(right[i]<=left[j]):
				lst[k]=right[i]
				i=i+1
			else:
				lst[k]=left[j]
				j=j+1
			k=k+1
		while(len(right)>i):
			lst[k]=right[i]
			i=i+1
			k=k+1
		while(len(left)>j):
			lst[k]=left[j]
			j=j+1
			k=k+1

lst=[1,23,4,56,7]
merge_srt(lst)
print(lst)

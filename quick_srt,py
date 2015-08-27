def quick_srt(lst,start,end):
	if(start<end):
		inx=partition(lst,start,end)
		quick_srt(lst,start,inx-1)
		quick_srt(lst,inx+1,end)

def partition(lst,start,end):
	piv=lst[end]
	index=start
	tmp=0
	for i in range(end):
		if(lst[i]<=piv):
			tmp=lst[i]
			lst[i]=lst[index]
			lst[index]=tmp
			index=index+1
	lst[end]=lst[index]
	lst[index]=piv
	return index

lst=[1,6,9,8,4,3,6,9,9]
end=(len(lst)-1)
quick_srt(lst,0,end)
print(lst)

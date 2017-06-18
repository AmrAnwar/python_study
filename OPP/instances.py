def combiner(list):
	order_list=[]
	sum_list=0
	for item in list:
		if isinstance(item,str):
			#order_list.insert(0,item)  >>wrong
			order_list.append(item)
		else:
			sum_list += item
	return (''.join(order_list)+str(sum_list))


print(combiner(["apple", 5.2, "dog", 8]))

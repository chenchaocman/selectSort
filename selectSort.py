

def insetSort(arry):

	for j in xrange(0,len(arry)):

		for i in xrange(j+1,len(arry)):

			if arry[i]>arry[j]:

				tem = arry[i]
				arry[i] = arry[j]
				arry[j] = tem

	return arry
				



if __name__ == '__main__':

	newarr = insetSort([1,2,3,-1,11,7,99,-11111,-98,99,99])

	print(newarr)
			

	



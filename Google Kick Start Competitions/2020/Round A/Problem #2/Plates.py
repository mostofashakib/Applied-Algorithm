# Time complexity: O(n*m)
# Space Complexity: O(n)

def MaximumBeautyValue(number_of_stacks, number_of_elements, array_of_arrays, limit):
	def select_first_element_remove(array_of_arrays):
		temp = []

		for i in range(len(array_of_arrays)):
			if len(array_of_arrays[i]) != 0:
				temp.append(array_of_arrays[i][0])

		if temp[0] == temp[-1]:
			return 0

		maximum = max(temp)

		for i in range(len(array_of_arrays)):
			if len(array_of_arrays[i]) != 0:
				if max(array_of_arrays[i]) == maximum:
					array_of_arrays[i].remove(maximum)

		return maximum

	def recursiveMaximum(array_of_arrays, limit):
		maximum = 0
		array = []

		for i in range(len(array_of_arrays)):
			if len(array_of_arrays[i]) <= limit:
				array.append(sum(array_of_arrays[i]))
			else:
				array.append(sum(array_of_arrays[i][:limit]))

		return max(array)

	MaximumBeautyValue = 0
	i = 0

	while i < limit:
		temp = select_first_element_remove(array_of_arrays)

		if temp != 0:
			MaximumBeautyValue += temp
			limit -= 1
		else:
			MaximumBeautyValue +=  recursiveMaximum(array_of_arrays, limit)
			break


	return MaximumBeautyValue



print("Testing # 1 " + str(MaximumBeautyValue(2, 4, [[10, 10, 100, 30], [80, 50, 10, 50]], 5)))

print("Testing # 2 " + str(MaximumBeautyValue(3, 2, [[80,80], [15, 50], [20,10]], 3)))
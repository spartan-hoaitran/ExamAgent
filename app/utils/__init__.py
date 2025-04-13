import numpy as np

def reshape_matrix(a: list[list], new_shape: tuple[int, int]) -> list[list]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	reshaped_matrix=np.zeros(new_shape)
	row=0
	column=0
	for i in a:
		for j in i:
			reshaped_matrix[row][column]=j
			column+=1
			if column==new_shape[1]:
				row+=1
				column=0
	return reshaped_matrix.tolist()
print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (4, 2)))
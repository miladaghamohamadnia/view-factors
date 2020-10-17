from functools import singledispatch
import numpy as np
from PIL import Image


def normalize_vec(v):
  return v/sum(v**2)**.5

class HemiCube(object):
	def __init__(self, dim = 300, distortOnly = True, nearDist = 0.01, farDist = 100.0, saveToFile = False):
		self.dim = dim
		self.nearDist = nearDist
		self.farDist = farDist
		#Initialize hemicube and scaling masks
		self.topMask = [0]*dim*dim
		#NOTE: The FOV of the face is 90 degrees
		forwardVec = np.array([0,0,1])
		total = 0.0
		for y in range(0, dim):
			for x in range(0, dim):
				index = y*dim+x
				xcoord = 2*float(x-dim/2)/float(dim)
				ycoord = 2*float(y-dim/2)/float(dim)
				dirVec = np.array([xcoord, ycoord, 1])
				dirVec = normalize_vec(dirVec)
				if distortOnly:
					self.topMask[index] = np.dot(dirVec, forwardVec)
				else:
					self.topMask[index] = np.dot(dirVec,forwardVec)**2
				total = total + self.topMask[index]

		self.sideMask = [0]*dim*(int(dim/2))
		leftVec = np.array([-1,0,0])
		for y in range(0, int(dim/2)):
			for x in range(0, dim):
				index = y*dim+x
				xcoord = 2*float(x-dim/2)/float(dim)
				ycoord = 2*float(y)/float(dim)
				dirVec = np.array([-1, xcoord, ycoord])
				dirVec = normalize_vec(dirVec)
				if distortOnly:
					self.sideMask[index] = np.dot(dirVec, leftVec)
				else:
					self.sideMask[index] = np.dot(dirVec, forwardVec) * np.dot(dirVec, leftVec)
				#There are 4 hemicube sides so count each weight 4x
				total = total + 4*self.sideMask[index]
		if saveToFile:
			im = Image.new("RGB", (dim, dim))
			pix = im.load()
			for y in range(0, dim):
				for x in range(0, dim):
					val = int(self.topMask[y*dim+x]*255)
					pix[x, dim-y-1] = (val, val, val)
			im.save("topMask.png")
			im = Image.new("RGB", (dim, int(dim/2)))
			pix = im.load()
			for y in range(0, int(dim/2)):
				for x in range(0, dim):
					val = int(self.sideMask[y*dim+x]*255)
					pix[x, int(dim/2)-y-1] = (val, val, val)
			im.save("sideMask.png")
		#Now normalize so that the sum of all incoming energy is 1
		for i in range(0, len(self.topMask)):
			self.topMask[i] = self.topMask[i]/total
		for i in range(0, len(self.sideMask)):
			self.sideMask[i] = self.sideMask[i]/total	
		np.save("topMask.npy", np.array(self.topMask))
		np.save("sideMask.npy", np.array(self.sideMask))
		

import matplotlib.pyplot as plt
if __name__ == '__main__':
	cube = HemiCube(saveToFile=True)
	print(cube.topMask[122:444])
	plt.imshow(np.array(cube.sideMask).reshape(-1, cube.dim))
	plt.show()

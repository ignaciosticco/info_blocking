import numpy as np
import matplotlib.pyplot as plt
import math

data = np.genfromtxt('in.bloc_info_225p_v8_g0', delimiter = ' ')


speed = data[:,0]
pressure = data[:,1]

def variables_promedio(data):
	i=250*10  # num_indiv*cantidad de iter hasta 5000 (para sacar los primeros 5s)
	p=0
	N=0
	v=0	
	while i<len(pressure):
		if speed[i]!=0:
			p+=pressure[i]
			v+=speed[i]
			N+=1
		i+=1

	avg_v = v/N
	avg_v = "%.2f" % avg_v
	avg_v = float(avg_v)	

	avg_p = p/N		
	avg_p = "%.2f" % avg_p
	avg_p = float(avg_p)

	out = [avg_v,avg_p]
	return out

print(variables_promedio(data))

	

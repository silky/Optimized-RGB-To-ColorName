#!/usr/bin/env python
# rgb2colorname.py
# by wilsonmar@gmail.com, ayush.original@gmail.com, https://github.com/paarthneekhara
# Usage: 
# Explained in https://github.com/jetbloom/rgb2colorname/blob/master/README.md
# KDTree Implementation details http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree
# This will be upgraded to 3 dimensional arrays
import numpy as np
from scipy import spatial


# define function:
#def find_nearest_vector(array, value):
#  # http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html
#  idx = np.array([np.linalg.norm(x+y) for (x,y,z) in array-value]).argmin()
#  return array[idx]


#Naive Solution- incomplete
#def find_index_of_nearest_xyz(x_array,y_array, z_array, x_point, y_point,z_point):
	#write loop
#    distance = (x_array-x_point)**2 + (y_array-y_point)**2 +(z_array-z_point)**2 
#    idx,idy,idz = numpy.where(distance==distance.min())
#    return idx[0],idy[0],idz[0]




#combined_x_y_arrays = numpy.dstack([y_array.ravel(),x_array.ravel()])[0]
#points_list = list(points.transpose())


#def do_kdtree(RGB,points):
#    mytree = scipy.spatial.cKDTree(RGB)
#    dist, indexes = mytree.query(points)
#    return indexes


n=571 # based on program output.
#A=np.empty((n,n,n))
#A = np.random.random((10,2))*100
#### Paste in contents of rgb_combined_v01.csv.txt below: ###

#TODO: Remove array and use dataframe to import from csv
A = np.array([ \

[240,248,255] \

,[250,235,215] \

,[255,239,219] \

,[238,223,204] \

,[205,192,176] \

,[139,131,120] \

,[0,255,255] \

,[127,255,212] \

,[127,255,212] \

,[118,238,198] \

,[102,205,170] \

,[69,139,116] \

,[240,255,255] \

,[240,255,255] \

,[224,238,238] \

,[193,205,205] \

,[131,139,139] \

,[245,245,220] \

,[255,228,196] \

,[255,228,196] \

,[238,213,183] \

,[205,183,158] \

,[139,125,107] \

,[0,0,0] \

,[255,235,205] \

,[0,0,255] \

,[0,0,255] \

,[0,0,238] \

,[0,0,205] \

,[0,0,139] \

,[138,43,226] \

,[165,42,42] \

,[255,64,64] \

,[238,59,59] \

,[205,51,51] \

,[139,35,35] \

,[222,184,135] \

,[255,211,155] \

,[238,197,145] \

,[205,170,125] \

,[139,115,85] \

,[95,158,160] \

,[152,245,255] \

,[142,229,238] \

,[122,197,205] \

,[83,134,139] \

,[127,255,0] \

,[127,255,0] \

,[118,238,0] \

,[102,205,0] \

,[69,139,0] \

,[210,105,30] \

,[255,127,36] \

,[238,118,33] \

,[205,102,29] \

,[139,69,19] \

,[255,127,80] \

,[255,114,86] \

,[238,106,80] \

,[205,91,69] \

,[139,62,47] \

,[100,149,237] \

,[255,248,220] \

,[255,248,220] \

,[238,232,205] \

,[205,200,177] \

,[139,136,120] \

,[220,20,60] \

,[0,255,255] \

,[0,255,255] \

,[0,238,238] \

,[0,205,205] \

,[0,139,139] \

,[0,0,139] \

,[0,139,139] \

,[184,134,11] \

,[255,185,15] \

,[238,173,14] \

,[205,149,12] \

,[139,101,8] \

,[169,169,169] \

,[0,100,0] \

,[189,183,107] \

,[139,0,139] \

,[85,107,47] \

,[202,255,112] \

,[188,238,104] \

,[162,205,90] \

,[110,139,61] \

,[255,140,0] \

,[255,127,0] \

,[238,118,0] \

,[205,102,0] \

,[139,69,0] \

,[153,50,204] \

,[191,62,255] \

,[178,58,238] \

,[154,50,205] \

,[104,34,139] \

,[139,0,0] \

,[233,150,122] \

,[143,188,143] \

,[193,255,193] \

,[180,238,180] \

,[155,205,155] \

,[105,139,105] \

,[72,61,139] \

,[47,79,79] \

,[151,255,255] \

,[141,238,238] \

,[121,205,205] \

,[82,139,139] \

,[0,206,209] \

,[148,0,211] \

,[255,20,147] \

,[255,20,147] \

,[238,18,137] \

,[205,16,118] \

,[139,10,80] \

,[0,191,255] \

,[0,191,255] \

,[0,178,238] \

,[0,154,205] \

,[0,104,139] \

,[105,105,105] \

,[30,144,255] \

,[30,144,255] \

,[28,134,238] \

,[24,116,205] \

,[16,78,139] \

,[178,34,34] \

,[255,48,48] \

,[238,44,44] \

,[205,38,38] \

,[139,26,26] \

,[255,250,240] \

,[255,250,240] \

,[34,139,34] \

,[255,0,255] \

,[220,220,220] \

,[248,248,255] \

,[255,215,0] \

,[255,215,0] \

,[238,201,0] \

,[205,173,0] \

,[139,117,0] \

,[218,165,32] \

,[255,193,37] \

,[238,180,34] \

,[205,155,29] \

,[139,105,20] \

,[128,128,128] \

,[190,190,190] \

,[0,0,0] \

,[3,3,3] \

,[26,26,26] \

,[255,255,255] \

,[28,28,28] \

,[31,31,31] \

,[33,33,33] \

,[36,36,36] \

,[38,38,38] \

,[41,41,41] \

,[43,43,43] \

,[46,46,46] \

,[48,48,48] \

,[5,5,5] \

,[51,51,51] \

,[54,54,54] \

,[56,56,56] \

,[59,59,59] \

,[61,61,61] \

,[64,64,64] \

,[66,66,66] \

,[69,69,69] \

,[71,71,71] \

,[74,74,74] \

,[8,8,8] \

,[77,77,77] \

,[79,79,79] \

,[82,82,82] \

,[84,84,84] \

,[87,87,87] \

,[89,89,89] \

,[92,92,92] \

,[94,94,94] \

,[97,97,97] \

,[99,99,99] \

,[10,10,10] \

,[2,102,102] \

,[105,105,105] \

,[107,107,107] \

,[110,110,110] \

,[112,112,112] \

,[115,115,115] \

,[117,117,117] \

,[120,120,120] \

,[122,122,122] \

,[125,125,125] \

,[13,13,13] \

,[127,127,127] \

,[130,130,130] \

,[133,133,133] \

,[135,135,135] \

,[138,138,138] \

,[140,140,140] \

,[143,143,143] \

,[145,145,145] \

,[148,148,148] \

,[150,150,150] \

,[15,15,15] \

,[153,153,153] \

,[156,156,156] \

,[158,158,158] \

,[161,161,161] \

,[163,163,163] \

,[166,166,166] \

,[168,168,168] \

,[171,171,171] \

,[173,173,173] \

,[176,176,176] \

,[18,18,18] \

,[179,179,179] \

,[181,181,181] \

,[184,184,184] \

,[186,186,186] \

,[189,189,189] \

,[191,191,191] \

,[194,194,194] \

,[196,196,196] \

,[199,199,199] \

,[201,201,201] \

,[20,20,20] \

,[204,204,204] \

,[207,207,207] \

,[209,209,209] \

,[212,212,212] \

,[214,214,214] \

,[217,217,217] \

,[219,219,219] \

,[222,222,222] \

,[224,224,224] \

,[227,227,227] \

,[23,23,23] \

,[229,229,229] \

,[232,232,232] \

,[235,235,235] \

,[237,237,237] \

,[240,240,240] \

,[242,242,242] \

,[245,245,245] \

,[247,247,247] \

,[250,250,250] \

,[252,252,252] \

,[0,128,0] \

,[0,255,0] \

,[0,255,0] \

,[0,238,0] \

,[0,205,0] \

,[0,139,0] \

,[173,255,47] \

,[240,255,240] \

,[240,255,240] \

,[224,238,224] \

,[193,205,193] \

,[131,139,131] \

,[255,105,180] \

,[255,110,180] \

,[238,106,167] \

,[205,96,144] \

,[139,58,98] \

,[205,92,92] \

,[255,106,106] \

,[238,99,99] \

,[205,85,85] \

,[139,58,58] \

,[75,0,130] \

,[255,255,240] \

,[255,255,240] \

,[238,238,224] \

,[205,205,193] \

,[139,139,131] \

,[240,230,140] \

,[255,246,143] \

,[238,230,133] \

,[205,198,115] \

,[139,134,78] \

,[230,230,250] \

,[255,240,245] \

,[255,240,245] \

,[238,224,229] \

,[205,193,197] \

,[139,131,134] \

,[124,252,0] \

,[255,250,205] \

,[255,250,205] \

,[238,233,191] \

,[205,201,165] \

,[139,137,112] \

,[173,216,230] \

,[191,239,255] \

,[178,223,238] \

,[154,192,205] \

,[104,131,139] \

,[240,128,128] \

,[224,255,255] \

,[224,255,255] \

,[209,238,238] \

,[180,205,205] \

,[122,139,139] \

,[238,221,130] \

,[255,236,139] \

,[238,220,130] \

,[205,190,112] \

,[139,129,76] \

,[250,250,210] \

,[211,211,211] \

,[144,238,144] \

,[255,182,193] \

,[255,174,185] \

,[238,162,173] \

,[205,140,149] \

,[139,95,101] \

,[255,160,122] \

,[255,160,122] \

,[238,149,114] \

,[205,129,98] \

,[139,87,66] \

,[32,178,170] \

,[135,206,250] \

,[176,226,255] \

,[164,211,238] \

,[141,182,205] \

,[96,123,139] \

,[132,112,255] \

,[119,136,153] \

,[176,196,222] \

,[202,225,255] \

,[188,210,238] \

,[162,181,205] \

,[110,123,139] \

,[255,255,224] \

,[255,255,224] \

,[238,238,209] \

,[205,205,180] \

,[139,139,122] \

,[0,255,0] \

,[50,205,50] \

,[250,240,230] \

,[255,0,255] \

,[255,0,255] \

,[238,0,238] \

,[205,0,205] \

,[139,0,139] \

,[128,0,0] \

,[176,48,96] \

,[255,52,179] \

,[238,48,167] \

,[205,41,144] \

,[139,28,98] \

,[102,205,170] \

,[0,0,205] \

,[186,85,211] \

,[224,102,255] \

,[209,95,238] \

,[180,82,205] \

,[122,55,139] \

,[147,112,219] \

,[171,130,255] \

,[159,121,238] \

,[137,104,205] \

,[93,71,139] \

,[60,179,113] \

,[123,104,238] \

,[0,250,154] \

,[72,209,204] \

,[199,21,133] \

,[25,25,112] \

,[245,255,250] \

,[255,228,225] \

,[255,228,225] \

,[238,213,210] \

,[205,183,181] \

,[139,125,123] \

,[255,228,181] \

,[255,222,173] \

,[255,222,173] \

,[238,207,161] \

,[205,179,139] \

,[139,121,94] \

,[0,0,128] \

,[0,0,128] \

,[253,245,230] \

,[128,128,0] \

,[107,142,35] \

,[192,255,62] \

,[179,238,58] \

,[154,205,50] \

,[105,139,34] \

,[255,165,0] \

,[255,165,0] \

,[238,154,0] \

,[205,133,0] \

,[139,90,0] \

,[255,69,0] \

,[255,69,0] \

,[238,64,0] \

,[205,55,0] \

,[139,37,0] \

,[218,112,214] \

,[255,131,250] \

,[238,122,233] \

,[205,105,201] \

,[139,71,137] \

,[238,232,170] \

,[152,251,152] \

,[154,255,154] \

,[144,238,144] \

,[124,205,124] \

,[84,139,84] \

,[175,238,238] \

,[187,255,255] \

,[174,238,238] \

,[150,205,205] \

,[102,139,139] \

,[219,112,147] \

,[255,130,171] \

,[238,121,159] \

,[205,104,137] \

,[139,71,93] \

,[255,239,213] \

,[255,218,185] \

,[255,218,185] \

,[238,203,173] \

,[205,175,149] \

,[139,119,101] \

,[205,133,63] \

,[255,192,203] \

,[255,181,197] \

,[238,169,184] \

,[205,145,158] \

,[139,99,108] \

,[221,160,221] \

,[255,187,255] \

,[238,174,238] \

,[205,150,205] \

,[139,102,139] \

,[176,224,230] \

,[128,0,128] \

,[160,32,240] \

,[155,48,255] \

,[145,44,238] \

,[125,38,205] \

,[85,26,139] \

,[102,51,153] \

,[255,0,0] \

,[255,0,0] \

,[238,0,0] \

,[205,0,0] \

,[139,0,0] \

,[188,143,143] \

,[255,193,193] \

,[238,180,180] \

,[205,155,155] \

,[139,105,105] \

,[65,105,225] \

,[72,118,255] \

,[67,110,238] \

,[58,95,205] \

,[39,64,139] \

,[139,69,19] \

,[250,128,114] \

,[255,140,105] \

,[238,130,98] \

,[205,112,84] \

,[139,76,57] \

,[244,164,96] \

,[46,139,87] \

,[84,255,159] \

,[78,238,148] \

,[67,205,128] \

,[46,139,87] \

,[255,245,238] \

,[255,245,238] \

,[238,229,222] \

,[205,197,191] \

,[139,134,130] \

,[160,82,45] \

,[255,130,71] \

,[238,121,66] \

,[205,104,57] \

,[139,71,38] \

,[192,192,192] \

,[135,206,235] \

,[135,206,255] \

,[126,192,238] \

,[108,166,205] \

,[74,112,139] \

,[106,90,205] \

,[131,111,255] \

,[122,103,238] \

,[105,89,205] \

,[71,60,139] \

,[112,128,144] \

,[198,226,255] \

,[185,211,238] \

,[159,182,205] \

,[108,123,139] \

,[255,250,250] \

,[255,250,250] \

,[238,233,233] \

,[205,201,201] \

,[139,137,137] \

,[0,255,127] \

,[0,255,127] \

,[0,238,118] \

,[0,205,102] \

,[0,139,69] \

,[70,130,180] \

,[99,184,255] \

,[92,172,238] \

,[79,148,205] \

,[54,100,139] \

,[210,180,140] \

,[255,165,79] \

,[238,154,73] \

,[205,133,63] \

,[139,90,43] \

,[0,128,128] \

,[216,191,216] \

,[255,225,255] \

,[238,210,238] \

,[205,181,205] \

,[139,123,139] \

,[255,99,71] \

,[255,99,71] \

,[238,92,66] \

,[205,79,57] \

,[139,54,38] \

,[64,224,208] \

,[0,245,255] \

,[0,229,238] \

,[0,197,205] \

,[0,134,139] \

,[238,130,238] \

,[208,32,144] \

,[255,62,150] \

,[238,58,140] \

,[205,50,120] \

,[139,34,82] \

,[128,128,128] \

,[0,128,0] \

,[128,0,0] \

,[128,0,128] \

,[245,222,179] \

,[255,231,186] \

,[238,216,174] \

,[205,186,150] \

,[139,126,102] \

,[255,255,255] \

,[245,245,245] \

,[190,190,190] \

,[0,255,0] \

,[176,48,96] \

,[160,32,240] \

,[255,255,0] \

,[255,255,0] \

,[238,238,0] \

,[205,205,0] \

,[139,139,0] \

,[154,205,50] \

])
### End of paste ###


RGB= np.delete(A, np.s_[3:5], axis=1)

pt = [154, 215,50]  # <-- the point to find
print (A[spatial.KDTree(A).query(pt)[1]]) # <-- the nearest point 

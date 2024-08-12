import numpy as np;
ma_1=np.array ([ [1,2,3,],[4,5,6,],[7,8,9] ])
ma_2=np.array ([ [9,8,7],[6,5,4],[3,2,1] ])
m_sum=ma_1+ma_2
m_diff=ma_1-ma_2
m_pro=ma_1*ma_2
m_div=ma_1/ma_2
m_multiply=np.dot(ma_1,ma_2)
ma_1_transpose=np.transpose(ma_1)
diagonal_sum=np.trace(ma_1)
print("matrix 1:\n",ma_1)
print("matrix 2:\n",ma_2)
print("sum of matrixs:\n",m_sum)
print("diffrence of matrixs:\n",m_diff)
print("product of thne matrixs:\n",m_pro)
print("division of the mattrixs:\n",m_div)
print("matrix multiplication:\n",m_multiply)
print("Transpose of matrix 1:\n",ma_1_transpose)
print("sum of diagonal elements of  matrix1:\n",diagonal_sum)

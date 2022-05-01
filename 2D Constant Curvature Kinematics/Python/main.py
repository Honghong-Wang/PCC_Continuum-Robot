import numpy as np
import matplotlib.pyplot as plt
from functions import trans_mat_cc
from functions import coupletransformations


# from configuration space (kappa, length) to task space (x,y)

# parameters
kappa1 = 1.7035; # 1/m
l1 = 0.1000; # metre
kappa2 = 1.0000; # 1/m
l2 = 0.1000; # metre
kappa3 = 2.0000; # 1/m
l3 = 0.1000; # metre

if kappa1 > 16 or kappa1 < -4:
    print("Please enter the First Curvature values between -4 and 16")
    kappa1 = 0;

elif kappa2 > 16 or kappa2 < -4:
    print("Please enter the Second Curvature values between -4 and 16")
    kappa2 = 0;

elif kappa3 > 16 or kappa3 < -4:
    print("Please enter the Third Curvature values between -4 and 16")
    kappa3 = 0;
    
else:
    print("Curvature Values for Each Segment are Appropriate")
    
    
# section 1
T1_cc = trans_mat_cc(kappa1,l1)
T1_tip = np.reshape(T1_cc[len(T1_cc)-1,:],(4,4),order='F');

# section 2
T2 = trans_mat_cc(kappa2, l2);
T2_cc = coupletransformations(T2,T1_tip);
T2_tip = np.reshape(T2_cc[len(T2_cc)-1,:],(4,4),order='F');

# section 3
T3 = trans_mat_cc(kappa3, l3);
T3_cc = coupletransformations(T3,T2_tip);

# Plot the trunk with three sections and point the section seperation
plt.scatter(T1_cc[0,12],T1_cc[0,13],linewidths=5,color = 'black',label="Section Seperation")
plt.plot(T1_cc[:,12],T1_cc[:,13],'b',linewidth=3,label="First Section")
plt.scatter(T1_cc[-1,12],T1_cc[-1,13],linewidths=5,color = 'black')
plt.plot(T2_cc[:,12],T2_cc[:,13],'r',linewidth=3,label="Second Section")
plt.scatter(T2_cc[-1,12],T2_cc[-1,13],linewidths=5,color = 'black')
plt.plot(T3_cc[:,12],T3_cc[:,13],'g',linewidth=3,label="Third Section")
plt.scatter(T3_cc[-1,12],T3_cc[-1,13],linewidths=5,color = 'black')
plt.legend(loc="best")
plt.title("2D Continuum Robot")
plt.xlabel("X - Position")
plt.ylabel("Y - Position")
plt.show()
# auroral oval
This python package conatins two auroral oval models, developed by  Starkov (1994a) and and Zhang & Paxton (2008). 

The models take Kp geomagnetic index and magnetic local time (mlt) as input and produce the poleward and equatorward boundaries of the auroral oval. 

The Feldstein-Starkov and Zhang-Paxtonoval models are given in the **FS_oval.py** and **ZP_oval.py** files. To get familiar with the models start from test scripts given seperately for each model. 

The Feldstein-Starkov model takes Kp index and MLT as input and produce either poleward or equtorward oval boundaries depending on the value of m.



![alt text](https://github.com/habtie-phys/auroraloval/blob/main/figures/FS_oval.png) 

The Zhang-Paxtonoval model takes Kp index, MLT and magnetic latitude (MLAT) as input and calculates energy flux of precipitating electrons. The auroral oval boundaries are then drawen at coordinates of (MLT, MLAT) where the energy flux is equal to a pre-defined value. The default pre-defined energy flux value is 0.25 mW/m^2

![alt text](https://github.com/habtie-phys/auroraloval/blob/main/figures/ZP_oval.png)

# Refernces 
Sigernes, F., Dyrland, M., Brekke, P., Chernouss, S., Lorentzen, D. A., Oksavik, K., & Deehr, C. S. (2011). Two methods to forecast auroral displays. J. Space Weather Space Clim., 1 (1). doi: https://doi.org/10.1051/swsc/2011003

Zhang, Y., & Paxton, L. (2008). An empirical kp-dependent global auroral model based on timed/guvi fuv data.
 Journal of Atmospheric and Solar-Terrestrial Physics, 70 (8), 1231-1242. doi: https://doi.org/10.1016/j.jastp.2008.03.008



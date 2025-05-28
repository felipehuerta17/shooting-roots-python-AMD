import matplotlib.pyplot as plt
import pandas as pd
from numpy import array

from Config.SoilParameters import SoilParameters
from Config.select_uptake_type import *
from Core.ShootingSol import *

# SOIL PARAMETER SETTING
lambda_ = 0.1  # set by user
soil_index = 1  # set by user: see Config.SoilParameters.py
active_uptake = True  # set by user: see Config.uptake_R.py
uptake_type = select_uptake_type(1)  # set by user: se Config.select_uptake_type.py

soil_parameters = SoilParameters()
soil_parameters.get_soil_parameters(soil_index, active_uptake, uptake_type)
Z = soil_parameters.Z

df = pd.DataFrame([(soil_parameters.theta_r, 'cm3*cm-3'),
                   (soil_parameters.theta_S, 'cm3*cm-3'),
                   (soil_parameters.K_S, 'cm/d'),
                   (Z, 'cm'),
                   (soil_parameters.lambda_, 'cm-1')],
                  index=['theta_r', 'theta_S', 'K_S', 'Z', 'lambda'],
                  columns=('Parameters', 'Values'))
print(df)

# INTEGRATION PARAMETER SETTING
T = 3  # set by user
Nt = 80  # set by user
Nz = 150  # set by user
tol = 1e-6  # set by user
bc_type = 'Ex3'  # set by user: see Config.boundary_condition_setter.py

dt = T / Nt
dz = Z / Nz

shooting_solution = ShootingSol(dt, dz, array([0, T]), array([0, Z]), tol)

shooting_solution.shooting_method(soil_parameters, active_uptake, uptake_type, bc_type)

# plt.contourf(shooting_solution.z_sol, shooting_solution.t_sol, shooting_solution.f_sol)

fig1, ax2 = plt.subplots(layout = 'constrained')
CS = ax2.contourf(shooting_solution.t_sol, shooting_solution.z_sol, np.transpose(shooting_solution.f_sol), cmap=plt.cm.inferno)
# Make a colorbar for the ContourSet returned by the contourf call.
cbar = fig1.colorbar(CS)

# plt.contourf(shooting_solution.t_sol, shooting_solution.z_sol, np.transpose(shooting_solution.f_sol))

# plt.xlabel('t (h)')
# plt.ylabel('z (cm)')

ax2.set_xlabel('t (h)')
ax2.set_ylabel('z (cm)')

plt.show()

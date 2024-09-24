# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys
import math


# "constants"
R_E_KM = 6378.137
E_E=0.081819221456

# helper functions

## function description

#   pass

# initialize script arguments
o_lat_deg =float('nan') # description of argument 1
o_lon_deg =float('nan') # description of argument 2
o_hae_km = float('nan')
s_km = float('nan')
e_km = float('nan')
z_km = float('nan')

# parse script arguments
if len(sys.argv)==7:
   o_lat_deg = float(sys.argv[1])
   o_lon_deg = float(sys.argv[2])
   o_hae_km = float(sys.argv[3])
   s_km = float(sys.argv[4])
   e_km = float(sys.argv[5])
   z_km= float(sys.argv[6])
   ...
else:
   print(\
      'Usage: '\
        'python3 o_lat_deg o_lon_deg o_hae_km s_km e_km z_km...'\
     )
   exit()

# write script below this line
o_lat_rad=o_lat_deg*(math.pi/180)
o_lon_rad=o_lon_deg*(math.pi/180)

#defining cos and sin to make the matrices easier to write
c_theta=math.cos(o_lon_rad)
c_phi=math.cos(o_lat_rad)
s_theta=math.sin(o_lon_rad)
s_phi=math.sin(o_lat_rad)

r_sez=[s_km, e_km, z_km]

r_ecef=[c_theta*s_phi*s_km+c_theta*c_phi*z_km-s_theta*e_km,
        s_theta*s_phi*s_km+s_theta*c_phi*z_km+c_theta*e_km,
        -c_phi*s_km+s_phi*z_km]

ecef_x_km, ecef_y_km, ecef_z_km=r_ecef

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
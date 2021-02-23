################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise08  Fluid Mechanics
# This program calculate the Reynolds number based on the input values.
################################################################################

# Formula: Re = (Vd) / v, V: Velocity d: diameter v: kinematic viscosity of the fluid

velocity = float(input("Enter the velocity of water in the pipe: "))
diameter = float(input("Enter the pipe's diameter: "))
temp = float(input(f"Enter the temperature in \u00B0C as 5, 10, or 15: "))
kv : float

if temp == 5:
    kv = 1.49 * (10 ** -6)
elif temp == 10 :
    kv = 1.31 * (10 ** -6)
elif temp == 15 :
    kv = 1.15 * (10 ** -6)

re = (velocity * diameter) / kv
re_formatting = "{:.2e}".format(re)

print(f"The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp}\u00B0C is {re_formatting}.")
#1E ELECTRICAL CURRENT IN THREE PHASE AC CIRCUIT
import math
P = eval(input("Enter power (in Watts) : "))
pf = eval(input("Enter power factor (pf<1): "))
VL = eval(input("Enter Line Voltage (in Volts) : "))
CL = P/(math.sqrt(3)*VL*pf)
print("Line Current =", round(CL,2),"A")
import matplotlib.pyplot as plt
import numpy as np
rainfall = np.array([[100,120,85,90,110,95],
                     [80,75,60,95,85,90],
                     [150,140,135,160,155,170]])
def avg_rf_cities(rf):
    t_r_X = sum(rf)
    avg = t_r_X/3
    return avg

avg = avg_rf_cities(rainfall)
months = ["M1", "M2", "M3", "M4", "M5", "M6"]
print("AVERAGE RAINFALL ACROSS ALL CITIES FOR EACH MONTH")
print (months)
print(avg)

### (1)
omega = 1366  # solar constant (W.m-2)
sigma = 5.67*1E-8            # Stefan Boltzman constant (W.m-2.K-4)
alpha = 0.306             # albedo: fraction of solar radiations reflected by the Earth



### (2)
Te_uten_atmosfær = (omega*(1-alpha)/(4*sigma)) **(1/4)

# print("%.2f" %(Te_uten_atmosfær -273),'°C')

### 2
epsilon = 0.77        # emissivity / fraction of longwaves radiations absorbed by the atmosphere
Te_med_atmosfær = ( (1-alpha)*omega / (4*sigma*(1-epsilon/2)) )**(1/4)
# print("%.2f" %(Te_med_atmosfær),'°C')   

def T_med_atm(alpha,omega,epsilon):
    sigma = 5.67*1E-8            # Stefan Boltzman constant (W.m-2.K-4)
    T = ( (1-alpha)*omega / (4*sigma*(1-epsilon/2)) )**(1/4)
    return T

jorden = (T_med_atm(0.306,1367,0.77))
jorden2 = (T_med_atm(0.306,1367,0.7904))

print("temperaturøkningen er :",jorden2-jorden)
# print( 2*(1-(1-alpha)*omega/((737**4)*4*sigma)) )
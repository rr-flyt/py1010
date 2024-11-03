# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:17:29 2024

@author: RuneRestad
Arbeidskrav 1 på Py1010
"""
print ("Arbeidskrav 1 for PY1010-1 24H Grunnleggende programmering med Python")
# Kostnader for elbil vs bil med fossilt drivstoff
print()
# Antall kjørte km for 2025 er satt til 16 000 km
km_2025 = 16000

#Kostnader for EL BIL
Forsikring_EL = 5000
Trafikkforsikring_EL = 365*8.38 #kr pr år
# Pris pr Kw er kr 2.0,- El bil bruker 0.2 kw/km. (0.2*2) = 0.4kr/Km
Drivstofforbruk_EL = 0.4*km_2025 #kr pr år
Bomavgift_EL = 0.1*km_2025 # kr pr år

Total_kostnad_ELBil = Forsikring_EL + Trafikkforsikring_EL + Drivstofforbruk_EL + Bomavgift_EL

#Kostnader for EL BIL
Forsikring_F = 7500
Trafikkforsikring_F = 365*8.38 #kr pr år
Drivstofforbruk_F = 1.0*km_2025 #kr pr år
Bomavgift_F = 0.3*km_2025 # kr pr år

Total_kostnad_FBil = Forsikring_F + Trafikkforsikring_F + Drivstofforbruk_F + Bomavgift_F

print("Forutsetninger:")
print("Antatt km forventet for 2025: ", km_2025), print("og forventet KW gjennomsnittpris på 2kr/KW:") 
print()
print("Resultat:")
print("Total kostnad for EL-Bil:", Total_kostnad_ELBil)
print("Total kostnad for bil med fossilt drivstoff:", Total_kostnad_FBil)
print()


print(f"Det koster {Total_kostnad_FBil - Total_kostnad_ELBil} kr 
      
      mer å ha fossilt drivstoff pr år enn El-bil")

#Takk for meg.
print()
print("Rune Restad")
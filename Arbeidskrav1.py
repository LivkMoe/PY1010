#!/usr/bin/env python
# coding: utf-8

# # Arbeidskrav 1
# ## *Liv Kristine Moe*
# ### 2024 11 08

# In[7]:


#  Konstante variabler 

km = 10000
Trafikkforsikringsavgift = 8.38 * 365

#  Utgifter Elbil per år 

Elforsikring = 5000
Eldrivstoff = 2.00 * km
Elbomavgift = 0.1 * km

Elbilutgift = Trafikkforsikringsavgift + Elforsikring + Eldrivstoff + Elbomavgift

print (" Elbilutgift = " , Elbilutgift)

#  Utgifter Bensinbil per år

Bensinforsikring = 7500
Bensinbruk = 1.0 * km
Bensinbomavgift = 0.3 * km

Bensinbilutgift = Trafikkforsikringsavgift + Bensinforsikring + Bensinbruk + Bensinbomavgift

print (" Bensinbilutgift = " , Bensinbilutgift)

#  Kostnadsdifferanse per år

Kostnadsdifferanse = Elbilutgift - Bensinbilutgift

print ("Kostnadsdifferanse = " , Kostnadsdifferanse)


# In[ ]:





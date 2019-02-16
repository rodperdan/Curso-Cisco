#!/usr/bin/env python
# coding: utf-8

# In[5]:


numero=int(input("Elige un número entero "))


# In[6]:


if numero < 20:
    print("El "+str(numero)+" es menor de 20")
elif numero >= 20 and numero <=39:
    print("El "+str(numero)+" está entre 20 y 40")
elif numero >= 40 and numero <=60:
    print("El "+str(numero)+" está entre 40 y 60")
else:
    print("El "+str(numero)+" es mayor de 60")


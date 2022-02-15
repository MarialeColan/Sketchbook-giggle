#!/usr/bin/env python
# coding: utf-8

# # Python para economistas: Primera Clase

# **1. Values y variable names**

# En python es importante distinguir entre valores y nombres de variables.
# Los valores más básicos con los que se puede trabajar en python son integers (enteros), floats (fracciones) y strings (texto).

# In[1]:


print ("Mariale Colán") #string


# In[2]:


1 #integrer


# In[3]:


2. #float


# A estos valores usulamente queremos asignarle un nombre (variable name) para luego referirnos a el en siguientes operaciones. En el siguiente ejemplo nombramos el valor string \"Mariale Colán\" como \"nombre\". Luego usamos la función print para revelar o imprimir que es lo que contiene 'nombre'."

# In[4]:


firstName= "Mariale"
lastName= "Colán"
print (firstName, lastName)


# **2. Operaciones con strings**

# Podemos además llamar las variables que creamos y hacer operaciones con ellas. En el siguiente ejemplo juntamos strings.

# In[5]:


fullName= firstName + ' ' + lastName
print (fullName)


# **3. Numeros y operaciones con numeros**

# Así mismo podemos realizar operaciones con integers (números enteros), floats (números reales) y otros objetos. Esto se puede realizar sin la necesidad de asignarles un nombre de variable, en este caso la operacion crea un objeto temporal que es visualizado en el kernel.

# In[6]:


print(
    3,
    1+2,
    2-1,
    2*3,
    4/2,
    4**2,
    4%3,
    5//2,
    4.5, #float:
    True,
    False)


# escribir un número
# suma +
# resta -
# multiplicación *
# división /
# potencia **
# evaluar el residuo de dividir 4 entre 3 (4%3)
# cociente de la división //
# float aka número real: se separa por un ".". Ejemplo: 4.5 

# **4. Tipos de objetos**

# Python te permite examinar el tipo de elemento con la funcion type(). Los tipos más basicos son int, float, str y bool.
# *Bool* : variable que sólo puede tomar dos posibles valores: True (verdadero) o False (falso)

# In[7]:


type (3)


# In[8]:


type (3.)


# In[9]:


type ("3.")


# In[10]:


type (True)


# **5. Cambio de tipo de elementos**

# Es posible además cambiar de tipo los elementos que querramos. Por ejemplo cambiar float a int para ahorrar memoria ram.

# In[11]:


int(4.5)


# In[12]:


int(True)


# In[13]:


int(False)


# In[14]:


float(True)


# In[15]:


float(3)


# Cambiar de tipo un objeto en el caso de números es dinstinto a redondearlos. Para redondearlos matemáticamente usamos la **función round()**.

# Cuando ponemos int(4.51) no se redondea a --> 5, el número se trunca y el resultado es --> 4

# 4.5 se redondea a 4. 4.51 se redondea a 5.

# **6. Redondear Numeros y otras operaciones**

# También podemos aplicar distintas funciones básicas predetermidas en python para ejecutar operaciones en numeros.

# In[16]:


round(4.5),
round(4.51),
print(round(4.5), round(4.51))


# In[17]:


print(round(4.51), int(4.51))


# In[18]:


abs(-2) #valor absoluto


# In[19]:


divmod(9,4) #Coeficiente y residuo


# In[20]:


pow(2,3) #2^3


# **7. Pedir insumos al usuario**

# Podemos pedir a python que interactue con  el usuario. En este python pide al usuario que introduzca un numero.

# In[21]:


beautiful_number= input("Tell me a beautiful number")
print(beautiful_number)


# **9. Listas y strings**

# Las listas son colecciones de elementos *del mismo o distinto tipo* de manera ordenada, las listas por lo general se introducen entre brackets [obj1, obj2]. En este caso, los strings tambien son listas donde cada caracter en el string es un elemento de la lista.

# In[22]:


[1,2,3,4]


# In[23]:


nombre='INFOX'
list(nombre)


# In[24]:


[1]*5


# In[25]:


print("a"*5)


# **10. Indexando y cortando listas**

# Es posible además indexar y cortar una lista. Cuando hablamos de indexar una lista -de tamaño N- básicamente lo que hacemos es quedarnos con el elemento número i de la lista, donde i es el orden que va de 0 hasta N. 

# Cuando dice [:] es print todo. CUando los números son negativos, lee la palabra al revés.

# In[26]:


print('1.',fullName),


# In[27]:


print('2.',fullName[0])


# In[28]:


print('3.',fullName[1:7])


# In[29]:


print('4.',fullName[0:7])


# In[30]:


print('5.',fullName[:6])


# In[31]:


print('6.',fullName[0:7][-1])


# In[32]:


print('7.',fullName[:])


#  Además, podemos dividir un string en función de algun caracter en el string, en este caso dividiremos el string en cada espacio con la función split(). En la funcion introducimos el caracter que hara la división del string varios substrings.

# In[45]:


str0 = 'I am learning Python'

str1 = str0.split(' ')
str2 = str0.split(' ', maxsplit=1)
print(str1, str2)


# También es posible unir strings

# In[41]:


proteinalist = ['Carne', 'Pollo', 'Cerdo', 'Pescado']
proteinas = ', '.join(proteinalist)
print(proteinas)


# In[43]:


proteinas.upper() # Cambiar string a mayusculas


# In[44]:


proteinas.lower() # Cambiar string a mayusculas


# Formateando Strings

# In[49]:


numbers = '%s, %s' % ('one', 'two')
print(numbers)
numbers = '%i, %i' % (1, 2)
print(numbers)
numbers = '%f, %f' % (1, 2)
print(numbers)
print('{}'.format(2))
print('{1} {0}'.format(1,2))


# **11. Mas operaciones**

# In[48]:


import math
pi = math.pi
eps = math.e
sq4 = math.sqrt(4)
math.exp(2)
math.log(4)
print(math.log(4))


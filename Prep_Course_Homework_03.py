#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

x=5
print(x)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(8.5)


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:


type(x)

# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_nombre="Antonio Perez"


# 5) Crear una variable que contenga un número complejo

# In[3]:

m=4+3j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

type(m)

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:

a=3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

b=True
c='True'



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

type(b)
print('la variable c es', type(c),'y la variable b es', type(b))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

t=4+4.2



# 11) Realizar una operación de suma de números complejos

# In[2]:

a=3+4j
b=2+2j
print(a+b)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

o=2.4
print(a+o)




# 13) Realizar una operación de multiplicación

# In[5]:

print(3*2)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

x=27/4
print(x)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

x=27//4
print(x)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

x=27%4
print(x)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

x=(4*(27//4))+27%4
print(x)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

x= 'señor '
y= 'juan'
print(x+y)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:


2=='2'


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

str(2)=='2'



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

# los datos decimales se expresa en ese caso como 3.8



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

x=3
x-=1
print(x)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:


# cada numero tiene un codigo binario,  al ejecutar el codigo desplaza 2 espacios.

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

# el primero es un número entero (int), y el segundo es una cadena de texto (str)

resultado = 2 + int('2')
print(resultado)


# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

resultado = 2 + int('2')
print(resultado)


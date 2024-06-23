a = 3
b = 3
c = 4

print(a is b)#muestra True
print(a is not b)#muestra False
print(a is not c)#muestra True

x = 1
y = x
z = y
print(z is 1)#muestra True
print(z is x)#muestra True

str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print(str1 is str2)#muestra True
print("Code" is str2)#muestra False

a = [10,20,30]
b = [10,20,30]

print(a is b)#muestra False (ya que las listas son objetos mutables en python)
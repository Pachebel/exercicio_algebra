from cmath import acos, cos
import numpy as np

#declarando os vetores
lista_v= []
lista_u= []

#definindo as dimensoes do vetor
dimension = int(input("Enter the dimension: "))


#definindo o valor do vetor u
for i in range(dimension): 
    input_u= float(input("Enter the value of u: "))
    lista_u.append(input_u)


#sim, aqui é a mesma coisa só que para o vetor v
for i in range(dimension): 
    input_v= float(input("Enter the value of v: "))
    lista_v.append(input_v)


#printando a lista pra ver se tá tudo certo
print ("lista u: ",lista_u,"\nlista v: ",lista_v)


#transformando as listas em arrays do numpy
list_u_np= np.array(lista_u)
list_v_np= np.array(lista_v)


#calculando o produto escalar
produto_escalar= np.multiply(list_u_np,list_v_np)

produto_escalar_somado = np.sum(produto_escalar)

print ("produto escalar: ",produto_escalar_somado)


# beleza, já temos o produto escalar, agora vamos calcular a norma


#aqui a gente eleva os numeros do array ao quadrado. Sim, a gente pega os números lá da primeira lista (list_u_np)
norma_u= np.square(list_u_np)
norma_v= np.square(list_v_np)


#aqui a gente soma esses numeros
norma_u= np.sum(norma_u)
norma_v= np.sum(norma_v)


#e aqui a gente calcula a raiz quadrada deles
norma_u= np.sqrt(norma_u)
norma_v= np.sqrt(norma_v)


print ("norma u: ",norma_u,"\nnorma v: ",norma_v)

# show, temos a norma :)



#Agora bora calcular o cosseno. Pra isso a gente pega aquela formula que o prof passou:

#cos(theta) = (u.v)/(||u||*||v||)


#aqui a gente calcula o cosseno
cos = produto_escalar_somado / (norma_u * norma_v)

print ("theta: ",cos)



#aqui a gente calcula os radianos
acos = acos(cos)

print (acos,"radianos")


#beleza, calculamos os radianos, agora vamos converter pra graus


#aqui a gente converte os radianos para graus
rad_to_degrees= acos * (180/3.14)

print (rad_to_degrees,"graus")



#pronto, facil né?
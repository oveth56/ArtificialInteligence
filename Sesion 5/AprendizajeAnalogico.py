#Universidad del valle
#Tema: Aprendizaje analogico.
#Autor: Moises Robleto.
#Importar las bibliotecas necesarias
from sklearn.neighbors import NearestNeighbors
import numpy as np

#Datos conocidos (entrenamiento)
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5,6]])

#Datos desconocidos (nuevas observaciones)
X_unknown = np.array([[1.5, 2.5], [3.5, 4.5]])

#Crear y ajustar el modelo de vecinos mas cercanos(Nearest Neighbors)
model = NearestNeighbors(n_neighbors=2)
model.fit(X_train)

#Encontrar los vecinos mas cercanos para las nuevas observaciones
distances, indices = model.kneighbors(X_unknown)

#Imprimir los vecinos mas cercanos encontrdos
for i in range(len(X_unknown)):
    print("Para la observacion", X_unknown[i], "los vecinos mas cercanos son:", X_train[indices[i]])
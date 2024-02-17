#Universidad del valle - Inteligencia Arficial
#Tema: Aprendizaje inductivo
#Autor: Moises Robleto
#Importar las bibliotecas necesarias
from sklearn.linear_model import LinearRegression

#Datos de entrenamiento: kilobytes (kb)
X_train = [[1024],[2048],[3072],[4096],[5120],[6144],[7168],[8192]]

# Etiquetas: Megabytes (MB)
y_train = [1, 2, 3, 4, 5, 6, 7, 8]

#Crear y entrenar el modelo de regresion lineal
model = LinearRegression()
model.fit(X_train, y_train)

#pedir el valor de kb
kb = int(input("Ingrese el valor de kb: "))

#Realizar predicciones
kb_to_convert = [[kb]]
predicted_mb = model.predict(kb_to_convert)

#Imprimir resultado
print(f"{kb} kb equivalen aproximadamente a {predicted_mb[0]} MB")

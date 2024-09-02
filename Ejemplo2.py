from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Cargar el dataset
iris = load_iris()
X = iris.data
y = iris.target
# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
print(X)
# Crear y entrenar el modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
# Realizar predicciones
y_pred = model.predict(X_test)
print(y_pred)
# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
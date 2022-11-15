from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import m2cgen as m2c

iris = datasets.load_iris()
print(iris.target_names)
print(iris.feature_names)

X, y = datasets.load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier(n_estimators=10, verbose=True)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("accuracy: ", metrics.accuracy_score(y_test, y_pred))

code = m2c.export_to_python(clf)

print(code, file=open("model.py", "w"))

print("Some examples to test:")

for i, (x, y) in enumerate(zip(X_test, y_test)):
    print(list(x), "->", y)
    if i >= 10:
        break

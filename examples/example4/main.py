from ulab import numpy as np
from neuralnetwork import DFF, amap, short, one_hot

epochs = 10
num_classes = 3
lr = 0.1

nn = DFF(layers=(4, 10, num_classes), func="tanh")

training_set = []

print("Loading data")
with open("iris.csv") as dataset:
    for i, line in enumerate(dataset):
        print(".", end="")
        if i == 30:
            break
        sepal_length, sepal_width, petal_length, petal_width, iris_class = [
            float(v) for v in line.split(",")
        ]
        x = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        y = np.array([one_hot(iris_class, num_classes)])
        # print(x, y)
        training_set.append([x, y])

print("\nTraining")
for _ in range(epochs):
    for a, s in training_set:
        nn.train(a, s, lrate=lr)
        print(".", end="")

print("\nValidation")
scores = []
for x, y in training_set:
    p = nn.predict(x)
    scr = np.sum(amap(p, round) == amap(y, round)) == num_classes
    # print(str(amap(p, round)), str(amap(y, round)))
    scores.append(scr)

score = sum(scores) / len(scores)
print("Accuracy is", score)

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras

from numpy.lib.stride_tricks import sliding_window_view
from sklearn.model_selection import train_test_split

df = pd.read_csv("out_combined.csv")

print(df.head())

xs = sliding_window_view(df["hall"].astype("float32").values, 5)
ys = np.array([int(np.any(y)) for y in sliding_window_view(df["label"].values, 5)])

X_train, X_test, y_train, y_test = train_test_split(xs, ys, test_size=0.2)

model = tf.keras.Sequential()
model.add(keras.layers.Dense(16, activation='relu', input_shape=(5,)))
model.add(keras.layers.Dense(32, activation='relu'))
model.add(keras.layers.Dense(1))

model.compile(optimizer="adam", loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=20, batch_size=64,
                    validation_data=(X_test, y_test))

model.save("model.tf")

# Convert the model to the TensorFlow Lite format without quantization
converter = tf.lite.TFLiteConverter.from_saved_model("model.tf")
model_no_quant_tflite = converter.convert()

# Save the model to disk
open("model.tflite", "wb").write(model_no_quant_tflite)

# Convert the model to the TensorFlow Lite format with quantization
def representative_dataset():
  for i in range(100):
    yield([X_train[i].reshape(1, 5)])
# Set the optimization flag.
converter.optimizations = [tf.lite.Optimize.DEFAULT]
# Enforce integer only quantization
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8
# Provide a representative dataset to ensure we quantize correctly.
converter.representative_dataset = representative_dataset
model_tflite = converter.convert()

# Save the model to disk
open("model_q.tflite", "wb").write(model_tflite)



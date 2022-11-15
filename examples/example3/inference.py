# https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/hello_world

import microlite
import io
import time

counter = 1

kXrange = 2.0 * 3.14159265359
steps = 1000
current_input = None

verbose = False
out_file = open("out.csv", "w")

def input_callback(microlite_interpreter):
    global current_input

    input_tensor = microlite_interpreter.getInputTensor(0)
    if verbose:
        print("input tensor:", input_tensor)

    position = counter * 1.0
    if verbose:
        print("position: %f" % position)

    x = position * kXrange / steps
    current_input = x
    if verbose:
        print("x: %f" % x)

    x_quantized = input_tensor.quantizeFloatToInt8(x)
    input_tensor.setValue(0, x_quantized)


def output_callback(microlite_interpreter):
    global current_input

    output_tensor = microlite_interpreter.getOutputTensor(0)

    if verbose:
        print("output:", output_tensor)

    y_quantized = output_tensor.getValue(0)
    y = output_tensor.quantizeInt8ToFloat(y_quantized)

    print("%f,%f" % (current_input, y)) # , file=out_file)


hello_world_model = bytearray(2488)

model_file = io.open("model.tflite", "rb")
model_file.readinto(hello_world_model)
model_file.close()

interp = microlite.interpreter(hello_world_model, 2048, input_callback, output_callback)

print("x,y")

for c in range(steps):
    start_time = time.time_ns()
    interp.invoke()
    if verbose:
        print("Inference time", (time.time_ns() - start_time) / 1e+9)
    counter += 1
    if verbose:
        break
    
if out_file:
    out_file.close()

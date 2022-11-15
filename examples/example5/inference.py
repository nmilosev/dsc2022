# Hall effect anomaly detection
import microlite
import io
import esp32
import time

current_input = None

def input_callback(microlite_interpreter):
    global current_input

    input_tensor = microlite_interpreter.getInputTensor(0)
    # print(input_tensor)
   
    xs = []
    while len(xs) < 5:
        xs.append(float(esp32.hall_sensor()))
        time.sleep(0.2)
   
    current_input = xs
    # print(current_input)

    x_quantized = [input_tensor.quantizeFloatToInt8(x) for x in xs]
    # print(x_quantized)
    for i in range(5):
        input_tensor.setValue(i, x_quantized[i])


def output_callback(microlite_interpreter):
    global current_input

    output_tensor = microlite_interpreter.getOutputTensor(0)

    y_quantized = output_tensor.getValue(0)
    
    y = output_tensor.quantizeInt8ToFloat(y_quantized)

    print(f"{current_input}, {y}")
    
    if y > 1:
        print("ANOMALY!!!")


model = bytearray(3064)

model_file = io.open("model_q.tflite", "rb")
model_file.readinto(model)
model_file.close()

interp = microlite.interpreter(model, 2048, input_callback, output_callback)

while True:
    interp.invoke()   
    
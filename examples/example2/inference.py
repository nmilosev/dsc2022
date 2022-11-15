from model import score
import time


def inference(sample):
    start_time = time.time_ns()
    result = score(sample)
    end_time = time.time_ns()
    print("Inference time:", (end_time - start_time) / 1e+9)
    print("Result:", result)
    return result

inference([4.8, 3.4, 1.9, 0.2]) # -> 0
inference([6.9, 3.1, 5.1, 2.3]) # -> 2
inference([6.3, 3.3, 4.7, 1.6]) # -> 1
inference([5.4, 3.4, 1.7, 0.2]) # -> 0
inference([7.2, 3.0, 5.8, 1.6]) # -> 2


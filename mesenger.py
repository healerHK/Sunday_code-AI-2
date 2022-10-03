import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import pprint
numOfPoint = 30
noise = np.random.normal(0, 1, 30).reshape(-1, 1)
for i in range(0, 30):
    print(20*noise[i, 0])

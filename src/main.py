#!/usr/bin/env python

# This is a simple script to demonstrate the use of the data processor module.
# It imports the `process_data` function from the `data_processor` module and applies it to a list of numbers.
# The result is printed to the console.


from data_processor import process_data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = np.random.randint(1, 20, size=100)
    result = process_data(data)
    #print(f"Processed Data: {result}")
    df=pd.DataFrame(result, columns=['Processed'])
    plt.plot(df['Processed'])
    plt.show()


if __name__ == "__main__":
    main()

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_file(filename1, filename2):
    filename1 = pd.read_csv(filename1, sep=' ', header=None, index_col=1,
                names=['lang', 'page', 'views', 'bytes'])
    filename2 = pd.read_csv(filename2, sep=' ', header=None, index_col=1,
                names=['lang', 'page', 'views', 'bytes'])
    return filename1, filename2

def plot(filename1, filename2):
    plt.figure(figsize=(10, 5))  # change the size to something sensible
    plt.subplot(1, 2, 1)  # subplots in 1 row, 2 columns, select the first
    plt.plot(filename1)  # build plot 1
    plt.title('Popularity Distribution')
    plt.xlabel('Rank')
    plt.ylabel('Views')
    # plt.subplot(1, 2, 2)  # ... and then select the second
    # plt.plot()  # build plot 2

    plt.savefig('wikipedia.png')  # save the figure to file
    plt.show()

def parse_first_data_set(filename1):
    filename1 = filename1.sort_values(by='views', ascending=False)
    filename1 = filename1['views'].to_numpy()
    return filename1

def main():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    filename1, filename2 = read_file(filename1, filename2)
    filename1 = parse_first_data_set(filename1)
    plot(filename1, filename2)


main()
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:52:53 2019

@author: Ho
"""

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.graph_objects as go

class Sorter:
    
    def generateArray(self, rangeNumbers, numberElements):
        return random.sample(range(rangeNumbers), numberElements)
    
    def selectionSort(self, array):
        fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
        fig.write_html('first_figure.html', auto_open=True)

        rects=plt.bar(indexArray, array, align='edge', width=0.5)
        plt.axis('off')
        plt.title('Selection Sort')
        
        
        length=len(array)
        for i in range(length):
            minimum_index=i
            for j in range(i+1, length):
                if array[j] < array[minimum_index]:
                    minimum_index = j
            array[i], array[minimum_index] =array[minimum_index], array[i]
            for rect, h in zip(rects, array):
                rect.set_height(h)
            plt.pause(0.003)

        plt.show()
        return array
    
    def insertionSort(self, array):
        for i in range(len(array)):
            for j in range(i, 0, -1 ):
                if array[j]<array[j-1]:
                    array[j-1], array[j] = array[j], array[j-1]
                    
        return array
    
    def init(self, indexes, array):
        graph = plt.bar(indexes,array) 
        return graph
        
    
if __name__ == '__main__':
    s = Sorter()

    array = s.generateArray(1000, 100)
    indexArray=list(range(len(array)))
    #print(indexArray)
    #print("No sort: ", array)
    start_time = time.time()
    s.selectionSort(array)
    elapsedTime=(time.time() - start_time)
    print("Selection sort: Time Execution: {} seconds ".format( elapsedTime))
#    start_time = time.time()
#    insertionSort=s.insertionSort(array)
#    elapsedTime=(time.time() - start_time)
#    print("Insertion sort: Time Execution: {} seconds ".format( elapsedTime))
#    print(insertionSort)
#    print(array)

    
    #ani = animation.FuncAnimation(plt.gcf(), s.selectionSort(array),  interval=1000, repeat= False)
    

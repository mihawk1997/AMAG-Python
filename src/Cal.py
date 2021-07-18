import numpy as np
import pandas as pd 
import math

df = pd.read_excel("C:/Users/suraj/Desktop/AMAG python challenge/data/Sample Input.xlsx") #input excel sheeet

#creating universal operation with different substrings
df['operation'] = df['operation'].str.lower()
df.loc[df['operation'].str.contains('add', case=False), 'operation'] = 'addition'
df.loc[df['operation'].str.contains('sub', case=False), 'operation'] = 'subtraction'
df.loc[df['operation'].str.contains('exp', case=False), 'operation'] = 'exponentiation'
df.loc[df['operation'].str.contains('div', case=False), 'operation'] = 'division' 


#method to calculate different operations
def get_calc(x,y,method):
    
    #Addition operation     
    if method.lower()=='addition':
         return x+y
        
    #subtraction operation    
    elif method.lower()=='subtraction':
         return x-y
        
    #division operation
    elif method.lower()=='division':
        if y == 0:
            return 'Division by 0 error'
        else:
            return x/y
        
    #multiplicaion operation
    elif method.lower()=='multiplication':
         return x*y
    
    #exponentiation operation
    elif method.lower()=='exponentiation':
        if x<0:
            return 'No significant solution'
        else:
            return x**y
    #check for invalid operation types
    else:
        method = 'Invalid'
        return 'Invalid input'

#send the values to the result column
df['result']=[get_calc(df.x[i],df.y[i],df.operation[i]) for i in range(len(df))]

#create an excel file to show results
df.to_excel ('C:/Users/suraj/Desktop/AMAG python challenge/result/result.xlsx', index = False, header=True)
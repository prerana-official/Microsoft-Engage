
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model 
from sklearn.model_selection import train_test_split 


class dataPreprocess:
 carsales = pd.read_csv('carsalesown.csv') #reading csv
 carsales=carsales.dropna()#dropping the rows having NaN values
 x=carsales.iloc[:,[0,2,3,4,5,6,7,8]]
 y=carsales.iloc[:,1]
 global  x_trainmain, x_testmain, y_trainmain, y_testmain
 x_trainmain, x_testmain, y_trainmain, y_testmain = train_test_split(x, y, test_size = 0.20)
 def linearreg(self,yearinput,arr):
     y_arr=np.array(yearinput)
     for i in range(1,8):
         x_train = x_trainmain.iloc[:,[0]] 
         y_train=x_trainmain.iloc[:,[i]] 
         x_test = x_testmain.iloc[:,[0]] 
         y_test = x_testmain.iloc[:,[i]] 
         regressor = LinearRegression() 
         model = regressor.fit(x_train, y_train)  
         y1= regressor.predict(arr)
         y_arr=np.append(y_arr,y1)          
     y_arr=y_arr.reshape(-1,8)
     self.df=pd.DataFrame(y_arr, columns=['Year','GDP per capita','Country GDP', 'Petrol prices', 'Diesel prices', 'Population', 'Inflation rate', 'Unemployment rate']) 
     regressor = LinearRegression() 
     model = regressor.fit(x_trainmain, y_trainmain)
     y_pred = regressor.predict(self.df)
     return self.df, y_pred

 def input(self,yearinput):
      arr=[yearinput]
      arr=pd.DataFrame(arr)
      finaldf, finalpred=self.linearreg(yearinput,arr)
      return finaldf, finalpred
      

 

     
 

import pandas as pd
import numpy as np

class GradientDescent:
    df:pd.DataFrame
    x:list
    y:list
    rows:int
    column:int

    def __init__(self,df,x1 ,x2,y):
        self.df = df
        self.x = df[[x1,x2]].to_numpy().tolist()
        self.y = df[[y]].to_numpy().tolist()
        self.rows,self.column = df.shape


    def CostFunc(self,o0, o1, o2,a):
        x=self.x
        y=self.y
        rows=self.rows

        for i in range(0,100):
            topj = 0
            for j in range(0, rows):
                topj = topj + (o0 * x[j][0] + o1 * x[j][1] + o2 - y[j][0]) ** 2
            c = topj / (2 * rows)
            print(f"{i}.cost :{c}")

            gradiento0 = 0
            gradiento1 = 0
            gradiento2 = 0

            for j in range(0, rows):
                gradiento0 = gradiento0 + (o0 * x[j][0] + o1 * x[j][1] + o2 - y[j][0]) * x[j][0]
                gradiento1 = gradiento1 + (o0 * x[j][0] + o1 * x[j][1] + o2 - y[j][0]) * x[j][1]
                gradiento2 = gradiento2 + (o0 * x[j][0] + o1 * x[j][1] + o2 - y[j][0])

            o0 = o0 - gradiento0 * a/ rows
            o1 = o1 - gradiento1 * a/ rows
            o2 = o2 - gradiento2 * a/ rows

        hprm=[o0,o1,o2]
        return hprm
    
def Prediction(area,bedrooms,grd):
        hParamaters =grd.CostFunc(10,100,10,np.exp(-17))

        for i in range(3):
             print(f"o{i} :{hParamaters[i]}",end=" ")
        print()


        return hParamaters[0]*area + hParamaters[1]*bedrooms + hParamaters[2]

df: pd.DataFrame = pd.read_csv("C:\\Users\\user\\Desktop\\Gradient\\House Price Prediction Dataset.csv")
grd=GradientDescent(df,'Area','Bedrooms','Price')
print("price:   "+str(Prediction(1360,5,grd)))


        

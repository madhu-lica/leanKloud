import  pandas as pd
import sys

df=pd.read_csv(sys.argv[1])
math=df['Maths'].max()
bio=df['Biology'].max()
eng=df['English'].max()
phy=df['Physics'].max()
chem=df['Chemistry'].max()
hin=df['Hindi'].max()
df1=pd.read_csv('marks.csv',index_col="Maths")
m=df1.loc[math,"Name"]
print("\nTopper in Maths is",m)
df2=pd.read_csv('marks.csv',index_col="Biology")
b=df2.loc[bio,"Name"]
print("\nTopper in biology is",b)
df3=pd.read_csv('marks.csv',index_col="English")
e=df3.loc[eng,"Name"]
print("\nTopper in English is",e)
df4=pd.read_csv('marks.csv',index_col="Physics")
p=df4.loc[phy,"Name"]
x2=p.array
print("\nTopper in Physics is",x2[0],",",x2[1])
df5=pd.read_csv('marks.csv',index_col="Chemistry")
c=df5.loc[chem,"Name"]
x1=c.array
print("\nTopper in Chemistry is",x1[0],",",x1[1])
df6=pd.read_csv('marks.csv',index_col="Hindi")
h=df6.loc[hin,"Name"]
print("\nTopper in Hindi is",h)
avg_scores=[]
count=df['Name'].count()


for i in range(count):
    deets=df.loc[i]
    arr=deets.array
    avg=sum(arr[1:7])/6
    avg_scores.append(avg)

avg_scores.sort()
#print(avg_scores)
#print(avg_scores[-1])
toppers={}
for i in range(count):
    deets=df.loc[i]
    arr=deets.array
    avg=sum(arr[1:7])/6
    if(avg==avg_scores[-1]):
        toppers[1]=arr[0]
    if(avg==avg_scores[-2]):
        toppers[2]=arr[0]
    if(avg==avg_scores[-3]):
        toppers[3]=arr[0]
print("\nBest students in the class are (",end="")
for  j in range(1,4):
    print(toppers[j],end=",")
print(")")

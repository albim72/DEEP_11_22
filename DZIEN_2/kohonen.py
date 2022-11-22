import pandas as pd
import numpy as np


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names=['sepal length','sepal width','petal length','petal width','class']
df = pd.read_csv(url,names=names)

#normalizacja
list_sl = []
list_sw = []
list_pl = []
list_pw = []

for sl in df['sepal length']:
    sl = (sl-min(df['sepal length']))/(max(df['sepal length'])-min(df['sepal length']))
    list_sl.append(sl)

for sw in df['sepal width']:
    sw = (sw-min(df['sepal width']))/(max(df['sepal width'])-min(df['sepal width']))
    list_sw.append(sw)

for pl in df['petal length']:
    pl = (pl - min(df['petal length'])) / (max(df['petal length']) - min(df['petal length']))
    list_pl.append(pl)

for pw in df['petal width']:
    pw = (pw - min(df['petal width'])) / (max(df['petal width']) - min(df['petal width']))
    list_pw.append(pw)

X = np.array(list(zip(list_sl,list_sw,list_pl,list_pw)))

#print(X)
nc = 3 #liczba klas (podgatunki irysów)
W=[] #lista wektorów w
M = len(X) #liczba wektorów x
N = len(X[0]) #wymiarowość wektora x

#funkcja zwaracająca losowe wartości wektorów x (czyli wag)
def get_weights():
    y = np.random.random()*(2.0/np.sqrt(M))
    return 0.5 - (1/np.sqrt(M)) + y

for i in range(nc):
    W.append(list())
    for j in range(N):
        W[i].append(get_weights()*0.5)

#funkcja obliczająca oodległość Euklidesową pomiędzy wektorami x i w

def distance(w,x):
    r=0
    for i in range(len(w)):
        r = r + (w[i]-x[i])**2
    r = np.sqrt(r)
    return r

#funkcja szukająca wektory x najbliższe wektorom w
def find_closest(W,x):
    wm = W[0]
    r = distance(wm,x)
    i = 0
    i_n = i
    for w in W:
        if distance(w,x) < r:
            r = distance(w,x)
            wm = w
            i_n = i
        i += 1
    return (wm,i_n)


print(W)

#inicjacja wspłczynników lambda oraz delta lambda
la = 0.3
dla  = 0.05
while la >=0:
    for k in range(10):
        for x in X:
            wm = find_closest(W,x)[0]
            for i in range(len(wm)):
                wm[i] = wm[i] + la*(x[i]-wm[i])
    la = la - dla

#trenowanie sieci oraz wyniki

data = list()
for i in range(len(W)):
    data.append(list())
dfList = df['class']
# print(dfList.to_list)

ds = list()
i=0
for x in X:
    i_n = find_closest(W,x)[1]
    data[i_n].append(x)
    ds.append([i_n,dfList[i]])
    i+=1

print(ds)

import pandas as pd
from sklearn import preprocessing
lb = preprocessing.LabelBinarizer()



id,status = [1,2,3,4,5],['Y','N','Y','N','Y']

data = [[i,j] for i,j in zip(id,status)]

df = pd.DataFrame(data,columns=['id','status'])
lb.fit_transform(df['status'])
print(lb.transform(df['status']))
print(lb.classes_)

from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np


data = pd.read_csv('Data.csv')
#print(data)
X = data.iloc[:,:-1]
Y = data.iloc[:,3]
#print(X)
#print(Y)
'''
#Handling missing data!
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean', verbose=0)
imputer = imputer.fit(X.iloc[:,1:3])
X.iloc[:,1:3] = imputer.transform(X.iloc[:,1:3])

#Encoding categorical data!
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X.iloc[:,0] =labelencoder_X.fit_transform(X.iloc[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y= labelencoder_Y.fit_transform(Y)
''' 

#Splitting the dataset into the Training set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state = 0)

'''
#Feature scaling 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''












'''
list1 = {'col1': [np.nan, np.nan, 3], 'col2': [
    4, np.nan, 6], 'col3': [10, 5, 9]}
df1 = pd.DataFrame(data=list1)
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(df1)

a = imp_mean.transform(df1)
print(type(df1))
'''

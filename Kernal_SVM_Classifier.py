# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Importing the dataset
    data = pd.read_csv('pulsar_stars.csv')
    x_train = data.iloc[1:,:-1].values
    y_train = data.iloc[1:,-1].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size = 0.2, random_state = 0)
    
    #Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.transform(x_test)
    
    # Training the SVM model on the Training set
    from sklearn.svm import SVC
    classifier = SVC(kernel = 'rbf', random_state = 0)
    classifier.fit(x_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(x_test)
    
    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
   
    # Writing Predictions in a file:
    df = pd.DataFrame(y_pred)
    df.to_csv('Y_Pred_K_SVM.csv',index=False)
        
if __name__ == "__main__":
    main()
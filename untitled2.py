import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

dataset = pd.read_csv("xclara.csv")
x = dataset.iloc[:,[0,1]].values


from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans = KMeans(n_clusters=i , init='k-means++',random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title("elbow method ")
plt.xlabel("v1")
plt.ylabel('v2')
plt.show()   


kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y_means = kmeans.fit_predict(x)

# Visualize
plt.scatter(x[y_means==0,0],x[y_means==0,1],s=100,c='blue',label='C1')
plt.scatter(x[y_means==1,0],x[y_means==1,1],s=100,c='red',label='C2')
plt.scatter(x[y_means==2,0],x[y_means==2,1],s=100,c='black',label='C3')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='yellow',label='centroids')

plt.title("Cluster formation ")
plt.xlabel("v1")
plt.ylabel("v2")
plt.show()

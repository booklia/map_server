from random import randint, sample
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge



def mlEngine(x1, y1, category):
    path = category+'.csv'
    print(path)
    data = pd.read_csv(path, sep=';')
    data = data.sample(frac=1)
    print(data.info())
    X = data[['id', 'category']]
    y = data[['id', 'rec']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)
    return model.predict(pd.DataFrame({'id': [x1], 'category': [y1]})).tolist()

user_data1 = {'statues': 5, 'nature': 4, 'churches': 4, 'sites': 3, 'theatres': 2, 'museums': 2, 'galleries': 1,
         'shopping': 1, 'national_cuisine': 1, 'fastfood': 1, 'cafe': 1, 'bars': 1}

points1 = ['museums', 'statues', 'statues', 'statues', 'statues']

id_bias = {'statues': 0, 'nature': 10, 'churches': 20, 'sites': 30, 'theatres': 40, 'museums': 50, 'galleries': 60,
         'shopping': 70, 'national_cuisine': 80, 'fastfood': 90, 'cafe': 100, 'bars': 110}

def getIds(user_data, points):
    category_count = {}
    resList = []
    for i in set(points):
        count = 0
        for j in points:
            if j == i:
                count += 1
        category_count[i] = count
    # print(category_count)
    for i in range(len(category_count)):

        elem = (category_count.popitem())
        userCategory = elem[0]
        pointsNumber = elem[1]
        userRating = user_data.get(userCategory)
        # print(userRating)
        # print(userCategory)
        # print(pointsNumber)
        resDict = {}
        for i in range(1, 10):
            a = mlEngine(i, userRating, userCategory)
            resDict[round(a[0][0]) + id_bias.get(userCategory)] = (a[0][1])
        # print(resDict)
        topPoints = list((sorted(resDict.items(), key=lambda x: x[1]))[::-1][:pointsNumber])
        for j in topPoints:
            resList.append(j[0])
    #print(resList)
    return resList

#print(getIds(user_data1,points1))

inputData1 = {'type': 'long',
             'categories': {'statues': 5, 'nature': 4, 'churches': 4, 'sites': 3, 'theatres': 2, 'museums': 2,
                            'galleries': 1, 'shopping': 1, 'national_cuisine': 1, 'fastfood': 1, 'cafe': 1, 'bars': 1
                            }}

#print(typeCategories)
def responseMl(inputData):
    typeData = inputData.get('type')
    typeCategories = inputData.get('categories')
    points = randint(3, 6)
    topCategories = list(sorted(typeCategories.items(), key=lambda x: x[1]))[::-1]
    arr = sample([i[0] for i in topCategories], points, counts=[i[1] for i in topCategories])
    #print('Вызов:')
    return getIds(typeCategories, arr)

print(responseMl(inputData1))

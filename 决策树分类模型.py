#这个监督式学习算法通常被用于分类问题。令人惊奇的是，它同时适用于分类变量和连续因变量。在这个算法中，我们将总体分成两个或更多的同类群。这是根据最重要的属性或者自变量来分成尽可能不同的组别。想要知道更多，可以阅读：简化决策树。

#在上图中你可以看到，根据多种属性，人群被分成了不同的四个小组，来判断 “他们会不会去玩”。为了把总体分成不同组别，需要用到许多技术，比如说 Gini、Information Gain、Chi-square、entropy。

#理解决策树工作机制的最好方式是玩Jezzball，一个微软的经典游戏(见下图)。这个游戏的最终目的，是在一个可以移动墙壁的房间里，通过造墙来分割出没有小球的、尽量大的空间。


#因此，每一次你用墙壁来分隔房间时，都是在尝试着在同一间房里创建两个不同的总体。相似地，决策树也在把总体尽量分割到不同的组里去。


#Python代码

#Import Library#Import other necessary libraries like pandas, numpy...

from sklearn importtree#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset

#Create tree objectmodel=tree.DecisionTreeClassifier(criterion='gini')#for classification, here you can change the algorithm as gini or entropy (information gain) by default it is gini

# model = tree.DecisionTreeRegressor() forregression# Train the model using the training sets andcheck score

model.fit(X,y)

model.score(X,y)#Predict

predicted=model.predict(x_test)

R code

library(rpart)

x

# grow tree

fit

#Predict Output

predicted= predict(fit,x_test)
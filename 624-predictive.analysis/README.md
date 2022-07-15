# Intro

The first half part of the course is focus on time series

  1. trend, seasonal, cyclic
  2. time series decomposition(better visualize trend and seasonal)
  3. seasonal diagnose plot
  4. time series smoothing(moving average)
  5. time series modeling(ARIMA, ETS)


the second part of the course is focus on varies regression models and its performance, I am going to break them into three parts, the params are the parameters which need to be tuned to get optimal model.

**Linear**
libraries: elasticnet, caret, lars, MASS, pls, stats

  1. Ordinary Linear Regression(params: intercept)
  2. Partial Least Square(params: ncomp)
  3. Penalized Regression

**Non Linear** 
libraries: nnet, earth, caret, kernlab
  
  1. Neural Network(params: size->number of hidden units, decay->learning rate)
  2. Support Vector Machine(param: sigma, C->cost)
  3. Multivariate Adapted Regression Splines(params: degree, nprune)
  4. K-Nearest Neighbors(param: k->number of neighbor used)

**Tree Structure**
libraries: caret, Cubist, gbm, ipred, party, randomForest, rpart, RWeKa

  1. Recursive Partition And Regression Tree(params: maxdepth)
  2. Random Forest(params: mtry)
  3. Gradient Boost Machine(params: interaction.depth->tree depth, n.trees, shrinkage->learning rate)
  4. Cubist(params:committees->boost, neighbors)

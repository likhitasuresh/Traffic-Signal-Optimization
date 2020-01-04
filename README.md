## **Traffic-Signal-Optimization**

Python project that implemented Machine Learning algorithms to optimize the functionalities of the current traffic signal system.
The project is aimed at building an efficient system that will help in optimizing the existing traffic signal system.It will use a traffic density as the main input parameter and automatically adjust the traffic signal timer accordingly in a more efficient way.

# **Objective**
To remove all hardware required to control traffic signals in order to provide efficient traffic signal optimization according to the day and the time.

# **Dataset**
* PeMS – Caltrans Performance Measurement System
* Freeway – 50W
* Length – 0.75mi
* 50-w/59th Street to 50-W/Stockton/35th Blvd
* Dark Sky API

# **Independent variables**
1. TIME OF THE DAY
2. DAY OF THE WEEK
3. WEATHER CONDITIONS
4. TEMPERATURE

# **Machine Learning Technique used - Random Forest Regression**
* Additive model viz., summation of multiple decision trees 
* Sampling is done with replacement ~ Bagging (bootstrap aggregating)

# **Picking the right algorithm**
Decision Tree Regression|Random Forest Regression
--------------------|------------------------
Single Tree|*Ensemble* learning
Very flexible model – overfitting occurs and hence bias is very high|Trees are formed on:
                                                                     * Random Sampling on training data points when building trees
                                                                     * Random subsets of features while splitting nodes
                                                                    |Avoids *overfitting*
                                                                    |Robust for Outliers

 



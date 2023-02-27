# Prediction of ML Operator Performance

This repository contains the code and documentation for the semester project in the course of design and analysis of information systems for the 9th semester in NTUA. The goal of this project is to develop a machine learning model that can accurately predict the performance of different operators in big data analytics runtimes.

[Project Paper](/Paper_Prediction_of_ML_Operator_Performance.pdf)

## Introduction

Machine Learning operators executed in big data analytics runtimes (e.g., Apache Spark) are often complex code that requires a significant amount of time to complete over data of large volume. In this project, we collected multiple measurements of how the execution of different operators progresses over time and used learning algorithms to create models that can predict their performance without even executing them.

## Project Steps

We completed the following steps in the project:

1. **Installation and setup of Apache Spark**: Using Okeanos-based resources, we installed and set up Apache Spark as our open-source, distributed analytics engine for executing different operators.

2. **Operator Selection**: We selected three operators from Apache Spark's MLLib library: k-means, random forest regression, and Word2Vec. These operators are diverse but belong to the same family.

3. **Data Generation and Loading**: Using an artificial data generator per operator, we created sample input data for the operators. The input data was of different sizes and structures and data points of different dimensions.

4. **Measurement of Performance and Modeling**: We executed multiple combinations of data to operator and monitored, for each combination, the total running time and main memory cluster usage. This data was then used to train a regression model to create accurate prediction models with minimal error in unseen data inputs.

## How to Run Experiments

To run experiments using the code, follow these steps:

1. Run `repeaterScript.sh` and provide the input parameters, which are the operator and the number of experiments you want to run.

2. Depending on your input, either random_forest_training.py, kmeans_training.py, or w2v_training.py will run. These scripts call data generators to create artificially generated data for model training of the corresponding operator.

3. After the model training is finished, the memory usage and total training time is gathered. The results are then saved in CSV files.

By following these steps, you can run experiments with different operators and input parameters and collect performance metrics for each run. This data can be used to train prediction models for each operator and evaluate their accuracy.

## Contributors
- Apostolis Garos: https://github.com/ApostolisGaros
- Nikos Vlachakis: https://github.com/NikosVlachakis
- Georgios Angelis: https://github.com/ag-george



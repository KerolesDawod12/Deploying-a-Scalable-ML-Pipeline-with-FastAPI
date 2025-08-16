# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
**Model Type:** RandomForestClassifier (scikit-learn)
**Version:** 1.0
**Framework:** Python 3.13, scikit-learn, FastAPI
**Author:** KerolesDawod12
**Date:** August 2025

## Intended Use
This model is intended to predict whether a person earns more than $50K/year based on U.S. Census data. It is designed for educational purposes and demonstration of deploying a machine learning pipeline with FastAPI. It should not be used for real-world financial or employment decisions.

## Training Data
The model was trained on the UCI Adult Census Income dataset (census.csv), which contains demographic and employment information for individuals in the United States. The dataset includes features such as age, workclass, education, marital status, occupation, relationship, race, sex, capital gain/loss, hours per week, and native country.

## Evaluation Data
The evaluation data is a 20% split from the original census.csv dataset, held out from training. The same preprocessing steps were applied to both training and evaluation data.

## Metrics
**Metrics Used:**
- Precision
- Recall
- F1 Score

**Model Performance on Test Data:**
- Precision: ~0.74
- Recall: ~0.64
- F1 Score: ~0.69

Performance was also evaluated on slices of categorical features (see slice_output.txt for details).

## Ethical Considerations
- The model may reflect biases present in the original census data, including gender, race, and socioeconomic biases.
- Predictions should not be used for real hiring, lending, or policy decisions.
- Users should be aware of the limitations and potential for unfair outcomes, especially for underrepresented groups.

## Caveats and Recommendations
- The model is for educational/demo use only.
- Performance may degrade on data distributions different from the training data.
- Further fairness and bias analysis is recommended before any real-world use.
- Model performance is limited by the quality and representativeness of the original dataset.

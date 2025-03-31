#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    # Load Titanic dataset
    return sns.load_dataset('titanic')

def clean_data(df):
    # Drop columns with too many missing values
    df.drop(columns=['deck', 'embark_town'], inplace=True)
    
    # Fill missing values
    df['age'].fillna(df['age'].median(), inplace=True)
    df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
    df['fare'].fillna(df['fare'].median(), inplace=True)
    df['alive'] = df['alive'].map({'yes': 1, 'no': 0})
    return df

def eda(df):
    # Basic statistics
    print(df.describe())
    
    -02a
    # Countplot of survival
    plt.figure(figsize=(6,4))
    sns.countplot(x='survived', data=df, palette='coolwarm')
    plt.title('Survival Count')
    plt.show()
    
    # Distribution of age
    plt.figure(figsize=(8,4))
    sns.histplot(df['age'], bins=30, kde=True)
    plt.title('Age Distribution')
    plt.show()
    
    # Survival rate by class
    plt.figure(figsize=(6,4))
    sns.barplot(x='pclass', y='survived', data=df, palette='viridis')
    plt.title('Survival Rate by Passenger Class')
    plt.show()
    
    # Correlation heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Feature Correlation Heatmap')
    plt.show()

def main():
    df = load_data()
    df = clean_data(df)
    eda(df)

if __name__ == "__main__":
    main()


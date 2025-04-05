import numpy as np
import pandas as pd
import kagglehub

def calcularEngajamento(df):
    views = df['views']
    likes = df['likes']
    dislikes = df['dislikes']
    comments = df['comments']
    return

path = kagglehub.dataset_download("datasnaek/youtube-new")

df = pd.read_csv(f"{path}/USvideos.csv", low_memory=False)

df.dropna(inplace=True)

df['approval'] = ((df['likes'] - df['dislikes']) / df['views']) + (df['comment_count'] / df['views'])

df.to_csv(f"{path}/USvideos.csv")

print(df.head())

import csv
import pandas as pd

df = pd.read_csv("Digital_behaviour.csv")

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)


print(df[["Instagram_Minutes", "Study_Minutes"]].describe())

print(df["Instagram_Minutes"])

col = ["Instagram_Minutes", "Study_Minutes"]
print(df[col])

print(df["Instagram_Minutes"].sum())

print(df["Study_Minutes"].mean())

print(df["Instagram_Minutes"].max())

df = df[df["Instagram_Minutes"] > 100]

print(df)

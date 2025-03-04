import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data.csv')

print("Primele 5 rânduri din setul de date:")
print(df.head())

print("\nValori lipsă per coloană:")
print(df.isnull().sum())

print("\nStatistici descriptive:")
print(df.describe())

print("\nCorelația între variabilele numerice:")
print(df[['Sales', 'Advertising']].corr())



plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], kde=True, bins=20)
plt.title('Distribuția vânzărilor')
plt.xlabel('Vânzări')
plt.ylabel('Frecvență')
plt.show()



plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Advertising'], y=df['Sales'])
plt.title('Corelația dintre Publicitate și Vânzări')
plt.xlabel('Publicitate')
plt.ylabel('Vânzări')
plt.show()



plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Region'], y=df['Sales'])
plt.title('Vânzările pe Regiuni')
plt.xlabel('Regiune')
plt.ylabel('Vânzări')
plt.show()



plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], kde=True, bins=20)
plt.title('Distribuția vânzărilor')
plt.xlabel('Vânzări')
plt.ylabel('Frecvență')
plt.savefig('sales_distribution.png')
print("\nGraficul distribuției vânzărilor a fost salvat ca 'sales_distribution.png'.")

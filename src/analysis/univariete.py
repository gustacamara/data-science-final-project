import seaborn as sns
import matplotlib.pyplot as plt
from src.data.loader import load_phenotypes
df = load_phenotypes()

print(df.head(10))
df.describe()
df.info()

print(df.select_dtypes(include='number').agg(["skew", "kurt"]))
# DTHHRDY = means how the person died

sns.histplot(df["SEX"], bins=50, kde=True)
plt.show()
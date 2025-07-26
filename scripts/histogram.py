# Skript vezme geoparsované tweety a vytvoří histogram počtu nalezených entit na tweet
import pandas as pd
import matplotlib.pyplot as plt

# Načtení dat
df = pd.read_csv("Zde vložit cestu ke zdrojovým datům")

# Výpočet počtu entit
df["num_entities"] = df["Entity_Names"].apply(lambda x: len(str(x).split(",")) if pd.notna(x) and x.strip() else 0)

# Definice hranic histogramu
bins = range(0, df["num_entities"].max() + 2)

# Vykreslení histogramu
plt.figure(figsize=(8, 5))
plt.hist(df["num_entities"], bins=bins, edgecolor="black", alpha=0.7, align='left')

# Estetika
plt.xlabel("Počet entit na tweet")
plt.ylabel("Počet tweetů")
plt.title("Rozložení počtu detekovaných lokalit na tweet")
plt.xticks(range(0, df["num_entities"].max() + 1))
plt.xlim(-0.5, df["num_entities"].max() + 0.5)  # Přesné ohraničení grafu, začátek přímo na ose Y
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

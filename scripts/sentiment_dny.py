# Skript pro každý den v týdnu generuje a ukládá graf průměrného sentimentu v průběhu dne zvlášť pro muže a ženy
import pandas as pd
import matplotlib.pyplot as plt

# Cesta k datovému souboru a výstupu
input_file_path = '/Users/bronapecner/Downloads/bp_prakticka/data_tweety/csv_tweety/Praha_tweety.csv'
output_folder = '/Users/bronapecner/Downloads/bp_prakticka/EDA/výstupy/sentiment/'

# Načtení CSV souboru s oddělovačem středník
df = pd.read_csv(input_file_path, sep=';')

# Převod sloupce 'Created' na datetime
df['Created'] = pd.to_datetime(df['Created'], errors='coerce')

# Ověření, zda sloupec 'Sentiment points' existuje a je numerický
if 'Sentiment points' not in df.columns:
    raise ValueError("Sloupec 'Sentiment points' v souboru neexistuje.")

df['Sentiment points'] = pd.to_numeric(df['Sentiment points'], errors='coerce')

# Vytvoření sloupce 'Hour' pro analýzu podle hodin
df['Hour'] = df['Created'].dt.hour

# Přidání názvu dne v týdnu
days_of_week = {
    0: 'Pondělí', 1: 'Úterý', 2: 'Středa', 3: 'Čtvrtek',
    4: 'Pátek', 5: 'Sobota', 6: 'Neděle'
}
df['DayOfWeek'] = df['Created'].dt.dayofweek.map(days_of_week)

# Mapování genderových hodnot na české názvy
if 'Gender' in df.columns:
    gender_mapping = {'m': 'Muži', 'f': 'Ženy', 'u': 'Neurčeno'}
    df['Gender'] = df['Gender'].map(gender_mapping)
else:
    raise ValueError("Sloupec 'Gender' v souboru neexistuje.")

# Vyfiltrování pouze mužů a žen (bez 'Neurčeno')
df = df[df['Gender'].isin(['Muži', 'Ženy'])]

# Iterace přes všechny dny v týdnu a generování grafu pro každý den
for day_num, day_name in days_of_week.items():
    df_day = df[df['DayOfWeek'] == day_name]

    if df_day.empty:
        print(f"Pro {day_name} nejsou dostupná žádná data, graf nebude vytvořen.")
        continue  # Přeskočíme dny bez dat

    # Seskupení dat podle hodin a pohlaví, výpočet průměrného sentimentu
    avg_sentiment_by_hour_gender = df_day.groupby(['Hour', 'Gender'])['Sentiment points'].mean().unstack()

    # Vytvoření cesty k výstupnímu souboru
    output_file_path = f"{output_folder}Průměrný sentiment v průběhu dne podle pohlaví ({day_name}).pdf"

    # Vykreslení grafu
    plt.figure(figsize=(14, 8))
    plt.plot(avg_sentiment_by_hour_gender.index, avg_sentiment_by_hour_gender['Muži'], label='Muži', color='blue', linestyle='-')
    plt.plot(avg_sentiment_by_hour_gender.index, avg_sentiment_by_hour_gender['Ženy'], label='Ženy', color='red', linestyle='-')

    # Úprava vizuálu grafu
    plt.xlabel('Hodina dne')
    plt.ylabel('Průměrný sentiment')
    plt.xticks(ticks=range(24))  # Nastavení osy X na celé hodiny
    plt.legend(title='Pohlaví')
    plt.grid(True)

    # Uložení grafu do PDF
    plt.savefig(output_file_path, format='pdf')

    # Zobrazení grafu
    plt.show()

    print(f"Graf byl úspěšně uložen jako {output_file_path}")
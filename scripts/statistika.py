# Skript analyzuje pokrytí zastávek ze slovníku v tweetech, měří jejich četnost a identifikuje nejčastěji zmiňované lokality

import pandas as pd

# Načtení datasetu tweetů
tweets_file_path = " Cesta "  # Změň na správnou cestu k souboru
df = pd.read_csv(tweets_file_path)

# Načtení slovníku zastávek
stops_file_path = " Cesta "  # Změň na správnou cestu k souboru
stops_df = pd.read_csv(stops_file_path)

# Počet zastávek ve slovníku
num_stops_in_dict = stops_df.shape[0]

# Nahrazení prázdných hodnot ve sloupci Entity_Names prázdným stringem
df["Entity_Names"] = df["Entity_Names"].fillna("")

# Odstranění duplicitních zastávek v rámci jednoho tweetu
df["Unique_Entities"] = df["Entity_Names"].apply(lambda x: ", ".join(set(x.split(", "))) if x else "")

# Správné počítání unikátních zastávek (ne unikátních buněk)
all_stops = [stop for entities in df["Unique_Entities"] if entities for stop in entities.split(", ")]
unique_entities_set = set(all_stops)  # Množina unikátních názvů zastávek
num_unique_entities = len(unique_entities_set)  # Počet unikátních zastávek

# Počet tweetů s nalezenou lokalitou
num_tweets_with_entities = df[df["Unique_Entities"] != ""].shape[0]

# Spočítání % zastávek ze slovníku, které se objevily v tweetech
stops_in_tweets = unique_entities_set.intersection(set(stops_df.iloc[:, 0]))  # Porovnání s prvním sloupcem slovníku
num_stops_found = len(stops_in_tweets)
percent_stops_found = (num_stops_found / num_stops_in_dict) * 100 if num_stops_in_dict > 0 else 0

# Počítání četnosti zastávek v tweetech
stop_counts = {}
for stop in all_stops:
    stop_counts[stop] = stop_counts.get(stop, 0) + 1

# Seřazení a výběr TOP 10 nejčastějších zastávek
top_10_stops = sorted(stop_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Výpis výsledků
print(f"Počet zastávek ve slovníku: {num_stops_in_dict}")
print(f"Počet unikátních zastávek nalezených v tweetech: {num_unique_entities}")
print(f"Počet tweetů obsahujících alespoň jednu lokalitu: {num_tweets_with_entities}")
print(f"Procento zastávek ze slovníku nalezených v tweetech: {percent_stops_found:.2f}%\n")

print("TOP 10 nejčastěji zmíněných zastávek:")
for i, (stop, count) in enumerate(top_10_stops, 1):
    print(f"{i}. {stop}: {count} tweetů")

# Diagnostika: výpis unikátních zastávek
print(f"\nSeznam unikátních zastávek nalezených v tweetech ({num_unique_entities}):")
print(sorted(unique_entities_set))  # Seřazeno pro lepší přehled

Analýza tweetů a webové aktivity: Pohled na sentiment, lokality a digitální interakce
Vítejte v tomto repozitáři, který obsahuje soubor Python skriptů zaměřených na hlubší analýzu dat, konkrétně tweetů s geografickou informací a webových interakcí. Cílem projektu je získat cenné poznatky o chování uživatelů, jejich sentimentu a zmínkách o klíčových lokalitách, s možností detailní analýzy, včetně genderových rozdílů.

Tento projekt je postaven na Pythonu a využívá populární knihovny pro datovou analýzu a vizualizaci.
<img width="573" height="223" alt="Screenshot 2025-07-26 at 17 26 07" src="https://github.com/user-attachments/assets/44cf8ab8-4190-4cb3-90d2-91200fc1410a" />

(Poznámka: Názvy souborů v adresáři data/ jsou pouze ilustrativní. Přizpůsobte si je podle skutečných názvů vašich datových souborů a jejich umístění.)

Popis a použití skriptů
Tento repozitář obsahuje tři hlavní analytické skripty:

1. Rozložení detekovaných entit v tweetech (histogram.py)
Účel:
Tento skript analyzuje geoparsované tweety a vizualizuje rozložení počtu nalezených geografických entit (lokalit) v rámci každého tweetu. Poskytuje vhled do toho, kolik unikátních míst je průměrně zmiňováno v jedné zprávě.

Klíčové výstupy:

Histogram zobrazující četnost tweetů podle počtu obsažených entit.

2. Průměrný denní sentiment dle pohlaví (sentiment_dny.py)
Účel:
Tento skript provádí hloubkovou časovou analýzu sentimentu v tweetech. Pro každý den v týdnu generuje a ukládá samostatný graf, který zobrazuje průměrný sentiment v průběhu dne, rozdělený zvlášť pro mužské a ženské uživatele.

Klíčové výstupy:

Sada PDF grafů (jeden pro každý den v týdnu), zobrazující průměrný sentiment v závislosti na hodině dne a pohlaví.

3. Analýza pokrytí a frekvence zmíněných lokalit (statistika.py)
Účel:
Tento skript se zaměřuje na validaci a četnost zmínek o konkrétních lokalitách (např. zastávkách) v tweetech. Porovnává nalezené entity s předdefinovaným slovníkem a identifikuje nejčastěji zmiňované.

Klíčové výstupy:

Statistiky o počtu unikátních lokalit ve slovníku a v tweetech.

Procentuální pokrytí lokalit ze slovníku nalezených v tweetech.

TOP 10 nejčastěji zmíněných lokalit.

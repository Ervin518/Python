text = 'Któregoś dnia w zeszłym tygodniu dokładnie o 9:29 pochyliłam się nerwowo nad klawiaturą komputera gotowa do walki ze sztucznym tworem o nazwie Emma. Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza. Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze. Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki).'
count_emma = text.split().count("Emma")
upper_text = text.upper()
words_list = text.split()
import re
sentences = re.split(r'[.!?]+', text)
sentence_count = len([s for s in sentences if s.strip()])

print("Liczba słów 'Emma':", count_emma)
print("Tekst wielkimi literami:", upper_text)
print("Lista wyrazów:", words_list)
print("Liczba zdań:", sentence_count)
- `nano plik.txt` - tworzenie pliku w nano
- `mv plik.txt plik2.txt` - zmiana nazwy pliku
- `mv katalog katalog01` - zmiana nazwy katalogu
- `rm -i plik.txt` - usuwanie pliku
- `rm -r katalog` - usuwanie katalogu

---

- `touch plik.txt` - tworzenie pustego pliku tekstowego
- `nano plik.sh` - tworzenie pliku shellowego
- `chmod +x plik.sh` - nadanie użytkownikowi praw do wykonywania pliku
- `./plik.sh` - wykonanie pliku
- `echo "jakiś tekst" >> plik.txt` - dodanie z poziomu pliku shellowego polecenia, które po wykonaniu pliku doda do pliku `plik.txt` frazę "jakiś tekst"
- `echo 'echo "jakis tekst" >> p.txt' >> p2.sh` - dodanie z poziomu terminala polecenia, które umieszcza w pliku `p2.sh` polecenie "jakieś..."

---

- `cat p01.txt p02.txt > p03.txt` - scalanie
- `sort p01.txt` - sortowanie

---

- Kompresowanie pliku do formatu zip:
  - `zip plik.zip plik.txt`
- Kompresowanie kilku plików tekstowych:
  - `zip pliki.zip plik01.txt plik02.txt`
- Rozpakowywanie paczki zip:
  - `unzip pliki.zip`
- Kompresja pliku poleceniem tar:
  - `tar -cf plik.tar plik.txt [plik02.txt, plik03.txt]`
- Rozpakowanie paczki tar:
  - `tar -xf plik.tar`
- Zmiana nazwy paczki zip:
  - `mv plik.zip plik02.zip`

---

- `grep "fraza" plik.txt` - wyszukiwanie frazy w pliku
- `sed -i 's/slowo/slowo2/' plik.txt` - zastępowanie słów w pliku
- `cat plik.txt` - wyświetlenie zawartości pliku
- `echo "text" >> plik.txt` - dodawanie słowa do pliku bez edytora
- `sed -i '/fraza/d' plik.txt` - usuwanie wiersza na podstawie frazy z pliku

---

- `sed -i 's/fraza/fraza2/' plik.txt` - zastąpienie
- `grep "fraza" plik.txt` - wyszukanie
- `sed -i 's/slowo//' plik.txt` - usunięcie pojedynczego
  słowa bez usuwania całego wiersza
- `sed -i '2 s/slowo//' plik.txt` - usunięcie słowa z konkretnego wiersza
- `sed -i '2 s/slowo//1' plik.txt` - usunięcie konkretnego wystąpienia słowa z określonego wiersza
- `sed -i '2 s/slowo//1g' plik.txt` - usunięcie wszystkich wystąpień słowa z określonego wiersza od 1szego do końca wiersza
- `cat plik.txt` - wyświetlenie zawartości pliku tekstowego
  bez korzystania z `nano`

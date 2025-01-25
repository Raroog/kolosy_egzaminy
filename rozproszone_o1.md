Oto poszczególne zadania z „rozproszonych systemów komputerowych” wraz z krótkim omówieniem rozwiązań. Starałem się możliwie wiernie odczytać rysunki i treść poleceń z załączonych obrazków.

---

## Zadanie 1 (diagram z procesami \(p_1, p_2, p_3, p_4\) i komunikatami grupowymi)

**Treść w uproszczeniu:**  
- Proces \(p_4\) wysyła komunikat (zdarzenie \(a\)) do \(p_1\) i \(p_3\); odbiory to odpowiednio \(x\) (w \(p_1\)) i \(y\) (w \(p_3\)).  
- Potem proces \(p_2\) wysyła komunikat (zdarzenie \(b\)) również do \(p_1\) i \(p_3\); odbiory to \(u\) (w \(p_1\)) i \(v\) (w \(p_3\)).  
- Wiadomo, że lokalny znacznik czasu \(C(a)\) jest mniejszy niż \(C(b)\) (czyli \(C(a)<C(b)\)).  
- Pytanie brzmi, czy z \(C(a)<C(b)\) wynika (implikuje) kolejność odbiorów, np. \(C(x)<C(u)\) i \(C(x)<C(v)\), itp. oraz czy jest to FIFO.

**Rozwiązanie i komentarz:**

1. Ponieważ komunikaty pochodzą **z różnych nadawców** (\(p_4\) oraz \(p_2\)), protokół FIFO z definicji nie wymusza tu żadnej kolejności między komunikatami **z różnych** procesów. FIFO zwykle gwarantuje kolejność tylko **per nadawca** (tzn. jeśli jeden nadawca wysyła dwa komunikaty w kolejności \(m_1\) potem \(m_2\), to każdy odbiorca otrzyma je w tej samej kolejności).  
   - Tutaj mamy **dwu różnych nadawców**, więc nie ma pewności, że komunikat \(a\) (z \(p_4\)) zostanie dostarczony w lokalnym czasie przed komunikatem \(b\) (z \(p_2\)) u każdego odbiorcy.  
   - Z diagramu widać zresztą, że odbiór \(x\) (w \(p_1\)) może się zdarzyć nawet „później” niż \(b\) w skali globalnej.

2. Implikuje to, że ani  
   \[
     C(a) < C(b)\;\; \text{nie gwarantuje} \;\;C(x) < C(u)\,\wedge\,C(x) < C(v),
   \]  
   ani analogicznie  
   \[
     C(a) < C(b)\;\; \text{nie gwarantuje} \;\;C(y) < C(u)\,\wedge\,C(y) < C(v).
   \]  
   W praktyce odpowiedź brzmi więc: oba stwierdzenia są **NIE** (nie wynikają wprost z \(C(a)<C(b)\)).

3. **Czy jest to komunikacja kolejowa (FIFO)?**  
   Również **NIE** w sensie globalnym między różnymi nadawcami. Gdyby był to jeden nadawca wysyłający dwa komunikaty, wtedy możnaby się zastanawiać nad zachowaniem FIFO. Ale przy różnych nadawcach — brak gwarancji.

---

## Zadanie 2 (metoda Cristiana)

**Treść:**  
Klient wysyła do serwera czasu zapytanie i po 2 ms łącznego czasu (RTT) otrzymuje odpowiedź z czasem \(T\). Serwer zużył 1 ms „w środku” (na przygotowanie odpowiedzi). Pytanie: o ile milisekund klient podnosi otrzymany czas \(T\), aby poprawnie zsynchronizować zegar?

**Rozwiązanie:**  
- Całkowity czas od wysłania zapytania do odebrania odpowiedzi to 2 ms.  
- Z tych 2 ms serwer przez 1 ms przygotowywał odpowiedź, więc na **same opóźnienia sieciowe (w obie strony)** zostaje 1 ms.  
- Przy metodzie Cristiana zakładamy symetryczny podział opóźnienia „w obie strony”, więc opóźnienie **jednokierunkowe** to \(\frac{1 \text{ ms}}{2} = 0{,}5 \text{ ms}\).  
- Klient zwiększa otrzymany czas \(T\) o połowę czasu sieci — czyli **o 0,5 ms**.

---

## Zadanie 1 z egzaminu (przelewy z kont \(a,b\) na konto \(c\))

Mamy dwa równolegle wykonywane programy:  
1. Przelew 120 zł z \(a\) na \(c\):
   ```pseudo
   if (a < 120) then ABORT
   else {
       a := a - 120;
       ra := c;
       ra := ra + 120;
       c := ra
   }
   ```
2. Przelew 30 zł z \(b\) na \(c\):
   ```pseudo
   if (b < 30) then ABORT
   else {
       b := b - 30;
       rb := c;
       rb := rb + 30;
       c := rb
   }
   ```
Początkowo \(a=\alpha\), \(b=\beta\), \(c=\gamma\). Zmienna `ra` czy `rb` to kopia \(c\) do obliczeń lokalnych.

**(A) Aktualizacja \(c\) nie jest chroniona sekcją krytyczną**  
Jeśli obie transakcje się **nie abortują** (tzn. \(\alpha \ge 120\) i \(\beta \ge 30\)), to w zależności od przeplotu instrukcji mogą wystąpić finalnie różne wartości \(c\):

1. **Jeśli T1 i T2 odczytają starą wartość \(\gamma\)** zanim którykolwiek zdąży ją zaktualizować, to:  
   - T1 ustawi \(c := \gamma + 120\)  
   - T2 ustawi \(c := \gamma + 30\) (bo T2 też pamiętało w `rb` jeszcze starą \(\gamma\)).  
   W efekcie końcowym może się zapisać \(\gamma + 30\) (jeśli T2 „nadpisze” w ostatnim kroku T1) **lub** \(\gamma + 120\) (jeżeli T1 wykona zapis w ostatnim kroku).  
2. **Może też być tak**, że jedna transakcja zdąży najpierw zaktualizować \(c\) na \(\gamma + 120\), a druga dopiero wtedy odczyta tę nową wartość. Wtedy finalnie dostaniemy \(\gamma + 150\).  
3. Gdyby jednak któraś transakcja się abortowała (np. \(\alpha<120\) lub \(\beta<30\)), wówczas w ogóle jej operacje nie są wykonywane i \(c\) może pozostać \(\gamma\) bądź zmienić się tylko o 30 lub o 120, zależnie od tego, która transakcja się powiodła.

Zatem przy braku sekcji krytycznej i przy obu transakcjach możliwych (bez abortu) mamy **trzy główne warianty**:  
\[
  c \in \{\gamma+30,\;\gamma+120,\;\gamma+150\}.
\]  
(Uwzględniając też ewentualne ABORT, może się pojawić \(\gamma\) jako wynik gdy jedna transakcja nie ruszy.)

**(B) Aktualizacja \(c\) jest chroniona do \(c:=...\)**  
Jeżeli obie transakcje wykonują swój zapis do \(c\) w sekcji krytycznej (jedna po drugiej), to nie może wystąpić nadpisanie wyniku innej transakcji. Wtedy (zakładając brak abortów) zawsze skończymy ze stanem  
\[
  c = \gamma + 120 + 30 = \gamma + 150,
\]  
niezależnie od kolejności (gdyż w obu kolejno odczytamy stan \(c\) zaktualizowany przez poprzednią transakcję).

---

## Zadanie 5 (sekwencyjna spójność)

**Treść skrócona:**  
- Komputer 1:  
  1. `pisz(a,1)`  
  2. `czyt(b,0)`  (odczytał wartość \(b=0\))  
- Komputer 2:  
  1. `pisz(b,1)`  
  2. `czyt(a,0)`  (odczytał wartość \(a=0\))  

Pytanie: czy da się ustawić te operacje w **jednym porządku sekwencyjnym**, który da te same wyniki odczytów (tj. \(b=0\) i \(a=0\)), spełniając jednocześnie porządek programowy każdej maszyny?

**Analiza:**  
- Żeby Komputer 1 zobaczył \(b=0\), jego odczyt `czyt(b,0)` musi nastąpić **przed** zapisem `pisz(b,1)` na Komputerze 2.  
- Żeby Komputer 2 zobaczył \(a=0\), jego odczyt `czyt(a,0)` musi nastąpić **przed** zapisem `pisz(a,1)` na Komputerze 1.  
- Tymczasem z porządku programowego wiemy, że Komputer 1 najpierw **pisze** \(a=1\), a dopiero potem czyta \(b\). A Komputer 2 najpierw **pisze** \(b=1\), a dopiero potem czyta \(a\).  

Próbując to wszystko ułożyć w jeden spójny ciąg, dostajemy wzajemnie sprzeczne zależności (koło w grafie przyczynowości). W efekcie **nie ma** pojedynczej kolejności sekwencyjnej, która pozwoliłaby odczytać oba zera i jednocześnie zachować porządek wewnątrz każdego wątku.  
Odpowiedź więc: **wykonanie nie jest sekwencyjnie spójne**.

---

### Podsumowanie skrótowe odpowiedzi

1. **Zad. 1 (grupowy komunikat \(p_4\to p_1,p_3\) i \(p_2\to p_1,p_3\))**  
   - \(\;C(a)<C(b)\) nie gwarantuje \(\;C(x)<C(u)\) itp., bo inny nadawca. Odpowiedzi: **NIE**, **NIE**.  
   - Komunikacja **nie** jest FIFO (różni nadawcy).

2. **Zad. 2 (Cristian)**  
   - Klient dodaje **0,5 ms** do czasu \(T\).

3. **Zad. 3 (przelewy 120 z \(a\) i 30 z \(b\) na \(c\))**  
   - Bez sekcji krytycznej: możliwe końcowe \(c \in \{\gamma,\;\gamma+30,\;\gamma+120,\;\gamma+150\}\) (zależnie od kolejności i ewentualnego abortu).  
   - Z sekcją krytyczną na zapis do \(c\): końcowe \(c = \gamma + 150\).

4. **Zad. 5 (pisz/czytaj na dwóch komputerach)**  
   - Nie da się uzyskać spójności sekwencyjnej z zaobserwowanymi odczytami (\(a=0, b=0\) przy wcześniej wykonanych pisaniach).  
   - Odpowiedź: **NIE**, nie jest sekwencyjnie spójne.


Mam nadzieję, że to klaruje, w jaki sposób rozwiązać powyższe przykłady i skąd biorą się odpowiedzi. W razie dalszych wątpliwości daj znać!


Zwykle przyjmuje się, że „awarią całego systemu” jest sytuacja, w której co najmniej jeden z komputerów przestaje działać. Skoro każdy komputer ma prawdopodobieństwo 0,1 awarii w ciągu roku, to:

- Prawdopodobieństwo, że **dany** komputer *nie* ulegnie awarii, wynosi \(1 - 0{,}1 = 0{,}9\).
- Aby żaden z 5 komputerów nie uległ awarii (a więc by cały system *nie* padł), potrzebujemy niezawodności wszystkich jednocześnie, co daje \((0{,}9)^5\).
- Zatem prawdopodobieństwo co najmniej jednej awarii (czyli awarii systemu w tym sensie) to
  \[
    1 \;-\; (0{,}9)^5 \;=\; 1 - 0{,}59049 \;\approx\; 0{,}40951.
  \]
Inaczej mówiąc, **ok. 40,95%** szans na to, że w ciągu roku system zawiedzie, jeśli wystarczy uszkodzenie jednego komputera spośród pięciu.

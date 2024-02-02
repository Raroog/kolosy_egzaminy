1. **Przeniesienie pliku do nowej lokalizacji**:
   - **Linux**: Używa się polecenia `mv [ścieżka/źródło] [ścieżka/destynacja]`. Na przykład, aby przenieść plik `dokument.txt` z bieżącego katalogu do katalogu `/dokumenty`, użyjesz `mv dokument.txt /dokumenty/`.
   - **Windows (CMD i PowerShell)**: Polecenie jest takie samo, `move [ścieżka/źródło] [ścieżka/destynacja]`. Na przykład, `move dokument.txt C:\dokumenty\`.

2. **Polecenie ping w powłoce CMD**:
   - W CMD, `ping` służy do testowania dostępności hosta w sieci (sprawdza, czy można się z nim połączyć). Używa się go przez wpisanie `ping [adres IP lub nazwa hosta]`. Na przykład, `ping google.com` sprawdzi połączenie z serwerami Google.

3. **Polecenie `net username localgroup Administrator /add *` w CMD z uprawnieniami administratora**:
   - To polecenie wydaje się być nieprawidłowo sformułowane. Prawdopodobnie miało na celu dodanie użytkownika do grupy Administratorów. Poprawna forma to `net localgroup Administrators [nazwa_użytkownika] /add`. Na przykład, `net localgroup Administrators Nasta /add` doda użytkownika `Nasta` do grupy Administratorów.

4. **Polecenie `cd` w powłoce CMD**:
   - Polecenie `cd` (Change Directory) służy do zmiany bieżącego katalogu. Na przykład, `cd C:\dokumenty` przeniesie Cię do katalogu `dokumenty` na dysku C.

5. **Stworzenie bazy informacji z pliku wsadowego bez nadpisywania danych**:
   - W systemach zarówno Linux, jak i Windows, aby zapisać dane do pliku bez ich nadpisywania, używa się operatora przekierowania `>>`. Na przykład, `echo "nowe dane" >> plik.txt` dopisze "nowe dane" na końcu `plik.txt` bez nadpisywania istniejącej zawartości.
  
6. **Poprawna nazwa wspólna polecenia w PowerShell**:
   - Polecenia w PowerShell nazywane są "cmdletami". Każdy cmdlet w PowerShell ma nazwę w formacie "Czasownik-Rzeczownik", np. `Get-Command`, `Set-Item`, `Remove-Item`.

7. **Operatory logiczne w PowerShell używane tylko z tekstem**:
   - W PowerShell operatorami logicznymi, które można używać wyłącznie z tekstami, są `-like`, `-notlike`, `-match`, i `-notmatch`. Służą one do porównywania ciągów tekstowych z użyciem wzorców i wyrażeń regularnych.

8. **Skasowanie wszystkich plików `.log` w bieżącym katalogu w PowerShell z uprawnieniami administratora**:
   - Polecenie, które to wykonuje, wygląda następująco: `Remove-Item *.log -Force`. Użycie `-Force` jest ważne, ponieważ pozwala na usunięcie plików tylko do odczytu. Pamiętaj, że to polecenie usunie wszystkie pliki `.log` w bieżącym katalogu bez ostrzeżenia, więc używaj go ostrożnie.

9. **Polecenie do wyświetlania zawartości katalogu w systemach Linux**:
   - W Linuxie, aby wyświetlić zawartość katalogu, używa się polecenia `ls`. Możesz użyć różnych opcji z tym poleceniem, na przykład `ls -l` dla szczegółowego wyświetlenia plików i katalogów.

10. **Znak zachęty dla konta administratora (root) w systemie Linux**:
   - W systemie Linux konto administratora, czyli root, jest zazwyczaj oznaczone znakiem zachęty `#`. Na przykład, gdy widzisz w terminalu `root@hostname#`, wskazuje to, że jesteś zalogowany jako użytkownik root.
  
11. **Kropka na początku nazwy zasobu w systemie Linux**:
   - W systemach typu Unix, w tym Linux, kropka na początku nazwy pliku lub katalogu oznacza, że jest to element ukryty. Tego rodzaju zasoby nie są wyświetlane domyślnie przez standardowe polecenia, takie jak `ls`, chyba że zostanie użyta odpowiednia opcja (np. `ls -a`).

12. **Polecenie w CMD do uzyskania informacji o konfiguracji sieci**:
   - Aby uzyskać informacje o konfiguracji sieci i danych interfejsów w CMD, używa się polecenia `ipconfig` lub `ipconfig /all` dla bardziej szczegółowych informacji.

13. **Kopiowanie plików w CMD z zmianą rozszerzenia**:
   - Polecenie, które umożliwi skopiowanie plików z określonym wzorcem nazewnictwa i zmianą rozszerzenia, może wyglądać następująco:
     ```
     for %f in (*_grade_????).bak do copy "%f" "%~nf.abck"
     ```
     To polecenie kopiuje wszystkie pliki pasujące do wzorca `*_grade_????`.bak (gdzie `????` to czterocyfrowy indeks) i zmienia ich rozszerzenie na `.abck`, zachowując pierwotną nazwę pliku (bez rozszerzenia .bak).

14. **Rozszerzenie pliku `.bat` w CMD**:
   - Plik z rozszerzeniem `.bat` jest plikiem wsadowym (batch) w systemach Windows. Pliki te zawierają serię poleceń, które są wykonywane przez interpreter CMD.

15. **Wskażenie nieprawidłowego skryptu i wskazówki do wykrycia**:
   - Aby wskazać nieprawidłowy skrypt, potrzebowałbym zobaczyć przykładowe skrypty do analizy. Generalnie, błędy w skryptach można wykryć przez sprawdzenie składni, logicznej konsekwencji poleceń, oraz upewnienie się, że wszystkie wymagane zmienne i ścieżki są poprawnie zdefiniowane. Również ważne jest sprawdzenie, czy polecenia są kompatybilne z używanym środowiskiem oraz czy nie naruszają żadnych zabezpieczeń systemowych.

16. **Rozszerzenia pliku wsadowego**:
   - W systemie Windows typowe rozszerzenia plików wsadowych to `.bat` i `.cmd`. Inne rozszerzenia, takie jak `.exe`, `.ps1` (PowerShell), czy `.sh` (skrypty shell w Unix/Linux), nie są rozszerzeniami plików wsadowych CMD.

17. **Znak łączenia poleceń w pliku wsadowym, aby wykonały się sekwencyjnie**:
   - Aby w pliku wsadowym kolejne polecenia wykonywały się tylko w przypadku powodzenia poprzedniego, używa się operatora `&&`. Na przykład: `polecenie1 && polecenie2` spowoduje wykonanie `polecenie2` tylko wtedy, gdy `polecenie1` zakończy się sukcesem.

18. **Uzupełnienie polecenia w pliku wsadowym**:
   - W pliku wsadowym, aby uzupełnić linię `find /n ..................... %1 | more` tak, aby był funkcjonalny, należy dodać tekst, który będzie szukany. Na przykład:
     ```
     find /n "%szukaj%" %1 | more
     ```
     To umożliwi wyszukiwanie tekstu wprowadzonego przez użytkownika w określonym pliku przekazanym jako pierwszy argument skryptu.

19. **Składnia polecenia w PowerShell**:
   - Składnia wzorcowa każdego polecenia w PowerShell składa się zwykle z dwóch członów: Czasownik-Rzeczownik. Przykłady: `Get-Item`, `Set-Content`, `Remove-Module`. Każdy cmdlet w PowerShell jest zbudowany zgodnie z tą konwencją.

20. **Polecenie `Get-Process | where-object {$_.PM -gt 90MB}` w PowerShell**:
   - To polecenie zwraca listę procesów, których używana pamięć prywatna (PM) jest większa niż 90 megabajtów. `Get-Process` pobiera informacje o procesach, a `where-object {$_.PM -gt 90MB}` filtruje te procesy, pokazując tylko te, które spełniają określone kryterium (użycie pamięci większe niż 90MB).

21. **Odchudzanie zainstalowanej wersji systemu Windows za pomocą PowerShell**:
   - W PowerShell, można użyć narzędzia Windows Feature (opcjonalne składniki systemu Windows) do odchudzenia systemu. Polecenie do zarządzania tymi funkcjami to `Get-WindowsFeature` oraz `Remove-WindowsFeature`. Na przykład, aby usunąć konkretną funkcję, użyłbyś `Remove-WindowsFeature NazwaFunkcji`. Uważaj, aby dokładnie znać funkcje, które usuwasz, aby nie naruszyć stabilności systemu.

22. **Sprawdzenie aktualnie zalogowanych użytkowników w systemie Linux**:
   - W systemie Linux, aby sprawdzić aktualnie zalogowanych użytkowników, używa się polecenia `who`. Jest to proste polecenie, które wyświetla listę wszystkich aktualnie zalogowanych użytkowników.

23. **Filtrowanie informacji w systemie Linux**:
   - W Linuxie, aby przefiltrować wyświetlaną informację pod kątem poszukiwanego ciągu znaków, używa się polecenia `grep`. Na przykład, `grep 'ciąg_znaków' plik.txt` wyświetli tylko te linie z `plik.txt`, które zawierają 'ciąg_znaków'.

24. **Założenie nowego pliku o nazwie `wyniki.txt` w systemie Linux**:
   - Aby utworzyć pusty plik o nazwie `wyniki.txt` w systemie Linux, możesz użyć polecenia `touch wyniki.txt`. Polecenie `touch` tworzy nowy, pusty plik, jeśli jeszcze nie istnieje.

25. **Wprowadzanie zmiennej w różnych środowiskach**:
   - **Linux (Bash)**: Zmienną definiuje się przez `nazwa_zmiennej=wartość`, na przykład `mojaZmienna=123`.
   - **Windows (CMD)**: W CMD zmienna definiowana jest przez `set nazwa_zmiennej=wartość`, np. `set mojaZmienna=123`.
   - **Windows (PowerShell)**: W PowerShell zmienna definiowana jest przez `$nazwa_zmiennej = wartość`, np. `$mojaZmienna = 123`.

26. **Poprawna składnia polecenia dla interpretera CMD**:
   - W CMD, polecenie zwykle składa się z nazwy polecenia i opcjonalnych argumentów. Na przykład, `dir /b` wyświetli tylko nazwy plików i katalogów w bieżącym katalogu.

27. **Znak łączenia poleceń, aby dane wynikowe z pierwszego posłużyły jako wejście do drugiego**:
   - W systemie Windows (CMD i PowerShell) oraz w systemie Linux (Bash), używa się potoku `|`. Ten znak przekazuje wynik jednego polecenia jako wejście do kolejnego. Na przykład, `polecenie1 | polecenie2`.

28. **Rozszerzenie, które nie identyfikuje pliku charakterystycznego dla PowerShell**:
   - Typowe rozszerzenia dla plików PowerShell to `.ps1` dla skryptów, `.psm1` dla modułów, i `.psd1` dla danych modułu. Rozszerzenia takie jak `.bat` (pliki wsadowe CMD), `.sh` (skrypty shell w Unix/Linux) nie są charakterystyczne dla PowerShell.

29. **Przełącznik w PowerShell obejmujący zakresem bieżący katalog i podkatalogi**:
   - W PowerShell, aby polecenie obejmowało zakresem nie tylko bieżący katalog, ale również jego podkatalogi, często używa się przełącznika `-Recurse`. Jest on stosowany w różnych cmdletach, na przykład w `Get-ChildItem -Recurse`, aby uzyskać elementy z bieżącego katalogu i wszystkich jego podkatalogów.

30. **Polecenie zmiany katalogu w systemie Linux**:
   - W systemie Linux, aby zmienić katalog, używa się polecenia `cd` (Change Directory). Na przykład, `cd /ścieżka/do/katalogu` przeniesie Cię do określonego katalogu.

31. **Polecenie zmiany hasła w systemie Linux jako użytkownik "newoneuser"**:
   - Jeśli jesteś zalogowany jako "newoneuser" i próbujesz zmienić hasło dla innego użytkownika "totokoko", musisz mieć uprawnienia administratora. Brakującym słowem w poleceniu jest `sudo`, co daje poleceniu uprawnienia superużytkownika. Poprawne polecenie to `sudo passwd totokoko`. System poprosi o hasło dla "newoneuser", a następnie pozwoli na zmianę hasła dla "totokoko".

32. **Polecenie systemu Linux nie służące do odczytu i przeglądania zawartości plików**:
   - Aby odpowiedzieć na to pytanie, potrzebowałbym listę poleceń do przeanalizowania. Polecenia takie jak `cat`, `less`, `more`, `tail`, `head` służą do odczytu i przeglądania zawartości plików. Polecenia niesłużące do tego celu mogą obejmować np. `rm` (usuwanie plików), `mkdir` (tworzenie katalogów) itp.

33. **Polecenie `net user (nazwa) (hasło) /add` w systemie Windows**:
   - Polecenie `net user [nazwa_użytkownika] [hasło] /add` w CMD służy do tworzenia nowego konta użytkownika z określoną nazwą użytkownika i hasłem.

34. **Skrypt zawierający błąd**:
   - Aby zidentyfikować błąd w skrypcie, potrzebowałbym zobaczyć przykładowe skrypty. Błędy mogą wynikać z nieprawidłowej składni, niewłaściwego użycia poleceń, błędów logicznych lub niewłaściwego użycia zmiennych.

35. **Polecenie `dir` z przełącznikiem do wyświetlenia tylko katalogów**:
   - W CMD, aby użyć polecenia `dir` do wyświetlenia tylko katalogów, używasz przełącznika `/AD`. Polecenie `dir /AD` wyświetli wszystkie katalogi w bieżącym katalogu.

36. **Polecenie `Ls *ps1 -Recurse | select -ExpandProperty DirectoryName` w PowerShell**:
   - To polecenie w PowerShell wyświetla nazwy katalogów dla wszystkich plików z rozszerzeniem `.ps1` w bieżącym katalogu i wszystkich jego podkatalogach. `Ls *ps1 -Recurse` znajduje pliki `.ps1`, a `select -ExpandProperty DirectoryName` wyodrębnia nazwy ich katalogów.

37. **Uruchamianie skryptów w PowerShell i odpowiednie ustawienie parametru**:
   - Domyślnie, PowerShell ma ograniczenia dotyczące uruchamiania skryptów. Aby umożliwić uruchamianie skryptów, musisz użyć polecenia `Set-ExecutionPolicy`, np. `Set-ExecutionPolicy RemoteSigned`. To pozwoli na uruchamianie lokalnych skryptów oraz tych pobranych z zaufanych źródeł. Pamiętaj, że zmiana polityki wykonania może narażać system na ryzyko, dlatego należy to robić z rozwagą.

38. **Katalog z dostępnymi urządzeniami w systemie plików Linux**:
   - W systemie Linux, katalog, w którym odnajdziesz dostępne urządzenia to `/dev`. Ten katalog zawiera specjalne pliki, które reprezentują urządzenia.

39. **Użycie polecenia nslookup z plikiem zawierającym adresy w systemie Linux**:
   - Aby użyć polecenia `nslookup` z plikiem zawierającym adresy serwerów, możesz przekierować zawartość tego pliku do polecenia `nslookup`. Na przykład, jeśli adresy są zapisane w pliku `serwery.txt`, polecenie będzie wyglądać następująco: `nslookup < serwery.txt`.

40. **Poznanie opisu każdej komendy w CMD**:
   - W CMD, aby uzyskać opis każdej komendy, używa się polecenia `help` seguido pelo nome do comando. Na przykład, `help dir` wyświetli opis polecenia `dir`.

41. **Wyświetlanie zawartości plików z podziałem na strony w CMD**:
   - W CMD, aby wyświetlić zawartość pliku z podziałem na strony, można użyć potoku `|` (pipe) wraz ze słowem `more`. Na przykład, `type plik.txt | more` spowoduje wyświetlenie zawartości `plik.txt` z podziałem na strony.

42. **Błędny zapis przypisania zmiennej w PowerShell**:
   - W PowerShell, poprawny zapis przypisania zmiennej to `$nazwa_zmiennej = wartość`. Błędne zapisy mogą obejmować pominięcie znaku dolara `$`, użycie niepoprawnych znaków w nazwie zmiennej, lub niewłaściwe użycie operatora przypisania. Na przykład, `nazwa_zmiennej = wartość` (bez `$`) lub `$nazwa zmiennej = wartość` (z białą przestrzenią) będą błędne.

43. **Czasownik Resolve w PowerShell**:
   - W PowerShell, czasownik `Resolve` jest używany w różnych cmdletach do rozwiązywania ścieżek, nazw lub innych identyfikatorów do ich pełnych form. Na przykład, `Resolve-Path` przekształca ścieżki względne na absolutne.

44. **Polecenie do zamknięcia systemu Linux o określonej godzinie**:
   - W systemie Linux, aby zaplanować zamknięcie systemu na określoną godzinę, używa się polecenia `shutdown`. Na przykład, `shutdown -h 22:00` zamknie system o godzinie 22:00. Opcja `-h` oznacza wyłączenie (halt).

45. **Brakujący przełącznik w poleceniu usuwania w Linux**:
   - Jeśli chcesz usunąć katalogi bez konieczności potwierdzania każdego z nich, użyj polecenia `rm` z przełącznikiem `-r` (rekursywne usuwanie) oraz `-f` (force, wymuszanie). Na przykład, `rm -rf /ścieżka/do/katalogu` usunie katalog i jego zawartość bez pytania o potwierdzenie.

46. **Kod liczbowy dla chmod w Linux do ustawienia konkretnych uprawnień**:
   - Aby ustawić uprawnienia `-rwx--x--x` dla pliku lub katalogu w Linux, użyjesz chmod z kodem liczbowym `711`. To dlatego, że `rwx` (czytanie, zapis, wykonanie) dla właściciela to `7`, a `--x` (tylko wykonanie) dla grupy i innych to `1`.

48. **Utworzenie ścieżki katalogowej jednym poleceniem w Linux z użyciem mkdir**:
   - Aby utworzyć ścieżkę katalogową jednym poleceniem w systemie Linux, używasz `mkdir` z przełącznikiem `-p`. Pozwala on na utworzenie wielu katalogów naraz, w tym katalogów nadrzędnych, które jeszcze nie istnieją. Na przykład, `mkdir -p /ścieżka/do/nowego/katalogu` utworzy całą ścieżkę katalogów, jeśli jeszcze nie istnieje.

# Hangman projekt

## Kort beskrivelse

Mit projekt er spillet Hangman.
Hvor jeg henter data fra 2 forskellige steder og bruger det data som de ord man skal gætte på.
Jeg har tilføjet hints til spillet så jeg har lidt mere kød på.
Man kan logge ind og oprette en bruger.
Så kan man også se grafer på brugerens spille informationer.

## Teknologier brugt

I dette projekt har jeg brugt følgende teknologier:

- Pandas
- Numpy
- os
- random
- cv2
- matplotlib
- tkinter
- PIL
- os
- sys
- requests

## Installations guide

Følgende skal installeres før projektet startes:

```python
pip install pandas
pip install numpy
pip install os
pip install random
pip install cv2
pip install matplotlib
pip install tkinter
pip install PIL
pip install os
pip install sys
pip install requests
```

## Bruger guide

For at køre projektet skal man køre følgende linje i roden af projektet

```python
python go.py
```

## Status på implementering

I dette projekt har jeg taget data jeg fandt på nettet,

- Rick and Morty API (https://rickandmortyapi.com/)
- Movies CSV (https://www.mavenanalytics.io/data-playground?page=2&pageSize=20).

Det data hentede jeg ned og ændrede så det passer til mit Hangman spil. Jeg fjernede unødvendige kolonner, ændrede navnet på de resterne kolonner og tilføjede data om sætningens/ordets opbygning.

I spillet kan også Log in og Sign up og bliver notificeret hvis man har forkert info.
Da man laver en bruger med Sign up, bliver alle informationer om brugeren gemt og der bliver lavet en csv fil til brugerens spil historik.
Brugernavnet og adgangskoden bliver gemt i en csv fil(DataFiles/UsersData.csv) samt en path til en ny csv, hvor jeg gemmer alt info om brugerens forrige spil.(DataFiles/Users/userName.csv)
Da man trykker på Exit og da man vinder eller taber, bliver information om det spil gemt i brugerens csv fil.

Efter man har logget ind eller lavet en bruger, ser du enten en side hvor du kan vælge enten at se statistik og at spille hangman, ellers hvis du ikke har nok data for at se grafer på statistik, kan du se en side hvor du skal vælge en kategori.
Da du vælger en kategori, bliver der hentet et tilfældig ord fra den kategori og det bliver sammenlignet brugerens spil historik, så man ikke får det samme ord to gange.

Da selve spillet starter, kan man se en hangman tegning som ændres ved hvert forkert gæt og det gættede bogstav bliver skrevet nedenfor linjerne og hver gang man gætter korrekt, kan man se linjerne som repræsenterer gætte ordet får bogstaver i stedet for.
Alt om spillet bliver skrevet ind i brugerens csv fil, her var der så meningen at man skulle kunne forsætte sit forrige spil, men det nåede jeg ikke.

Man kan også vinde og tabe spillet og da det sker, kommer mand ind på game over siden, hvor der er en spil igen knap samt hvad gætte ordet var og information som fortæller om du har vundet eller tabt.

Da man kommer til statistik siden, kan man vælge at se en linje graf eller et søjlediagram. Da jeg startede på det fattede jeg at det data jeg har er ikke det bedste til at lave grafer fra så jeg måtte improvisere lidt. Her er der også en spil igen knap.

Jeg har nået næsten alt jeg ønskede mig, de eneste jeg ikke nåede, var at lave funktionaliteten om så at man kan spille videre næste gang man åbner programmet og at jeg nåede ikke at lave mit UI helt perfekt.

## Udfordringer

I dette projekt har der været mange udfordringer, til at starte med var der tkinter, som jeg ikke var så god til, men efter en video og gode noter, kunne jeg få mit spil til at se ret godt ud.

Jeg havde det også lidt svært med at finde ud af hvordan man henter fra et API i python, men efter at kigge over noter og Google, fandt jeg ud af det og mit Rick and Mory data ser helt korrekt ud.

Så var der en udfordring med at lav en spil igen knap, jeg blev ved med at få en fejl om en cirkulær import og det tog ret lang tid at finde ud af men det virker nu og det er jeg stolt af.

Jeg er ret stolt af at jeg nåede at tegne hele hangman og gemme filen for hvert skridt og at senere kunne jeg vise dem hver gang man gætter forkert.

Så var jeg meget glad for hvordan funktionaliteten på da man gætter på et bogstav eller et ord virkede, begge for korrekt og forkert gæt.

Jeg var også meget stolt af at jeg nåede at gøre hint knappens funktionaliteten(man får kun 3 hints, så de første 3 gange du trykker på den ser du et nyt hint, men efter det bliver knappen grå og virker ikke længere).

Men det som jeg er mest stolt af er at da jeg henter en tilfældig række fra mit data(Rick and Morty character or Movies) så kigger jeg igennem brugerens csv fil og returnerer et ord brugeren ikke har fået før.

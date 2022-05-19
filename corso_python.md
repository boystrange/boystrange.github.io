---
layout: page
title: Introduzione a Python
---

Lo scopo di questo corso è quello di fornire le prime basi di
programmazione in Python, un linguaggio di programmazione noto per
la rapidità di scrittura dei programmi che integra diversi paradigmi
di programmazione (imperativo, object-oriented e funzionale). Il
corso si concentrerà soprattutto sul paradigma imperativo, secondo
il quale un programma è una sequenza di comandi atti a modificare lo
stato del calcolatore, e sul paradigma funzionale, secondo il quale
un programma è sequenza di trasformazioni sui dati.

Il sito <https://www.python.org> contiene numerose risorse sul
linguaggio Python. Di particolare importanza è la sezione dedicata
alla documentazione che contiene, tra le altre cose:

* [Un tutorial](https://docs.python.org/3/tutorial/index.html)
* [La documentazione della libreria standard](https://docs.python.org/3/library/index.html)
* [Il manuale di riferimento del linguaggio](https://docs.python.org/3/reference/index.html)

**Nota**. Attualmente esistono due versioni popolari del linguaggio,
la 2 e la 3. Il corso è impostato facendo riferimento alla versione
3, che è destinata a soppiantare la versione 2. Le due versioni del
linguaggio differiscono per numerosi aspetti, ma i concetti
descritti si applicano a entrambe le versioni ed i programmi
presentati saranno in gran parte eseguibili senza modifiche anche
con la versione 2, che è quella disponibile sulla macchine del
laboratorio.

## Indice degli argomenti
{:.no_toc}

* TOC
{:toc}
{:.no-style}

## 1. Nozioni di base

### 1.1 Script

Un programma Python è contenuto in uno **script**, ovvero un file di testo con estensione `.py` che contiene il codice del programma, sotto forma di definizioni (di funzioni, di classi, ecc.) e di comandi da eseguire. Un semplice esempio di script Python è il seguente, che stampa un saluto sul terminale quando eseguito:

```python
print("Ciao!")
```

Assumendo di aver creato un file `saluto.py` con il codice qui sopra, si può eseguire lo script dalla linea di comando inserendo

```bash
$ python3 saluto.py
Ciao!
```

In alternativa, è possibile usare Python come una calcolatrice attraverso il comando `python3` senza argomenti:

```text
$ python3
Python 3.7.3 (default, Mar 27 2019, 09:23:15)
[Clang 10.0.1 (clang-1001.0.46.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Il testo effettivo può variare in base alla versione di Python, del sistema operativo e dell'architettura su cui si esegue il comando. I simboli `>>>` rappresentano il **prompt** di comandi di Python e indicano che Python è pronto a ricevere espressioni (da valutare) e comandi (da eseguire). Per esempio, scrivendo

```python
>>> 1 + 2
3
>>>
```

chiediamo a Python di valutare l'espressione `1 + 2`, Python ne stampa il valore e ripropone il prompt in attesa di ulteriori espressioni o comandi. Si può usare `CTRL-D` per uscire da Python e ritornare alla linea di comando.

### 1.2 Tipi di dato primitivi

Python fornisce un insieme di tipi di dato primitivi per rappresentare informazioni di varia natura. I principali sono:

* `int` per rappresentare numeri interi a precisione arbitraria;
* `float` per rappresentare numeri in virgola mobile;
* `bool` per rappresentare valori di verità.

Numeri interi e in virgola mobile si scrivono nella solita notazione decimale. I numeri in virgola mobile sono riconoscibili per via del punto decimale `.` oppure dell'esponente `e`:

```python
>>> 1
1
>>> 15
15
>>> 0.5
0.5
>>> 2e3
2000.0
```

Il nome di un tipo numerico può essere usato anche per effettuare conversioni, eventualmente con troncamento:

```python
>>> float(2)
2.0
>>> int(0.5)
0
```

In Python i valori di verità si indicano con `True` e `False`. Ogni numero diverso da 0 può essere interpretato come `True`, mentre 0 è interpretato come `False`. Le seguenti conversioni esplicite illustrano questa convenzione:

```python
>>> bool(0.5)
True
>>> bool(2)
True
>>> bool(0)
False
```

### 1.3 Espressioni

Le espressioni si scrivono nella normale forma **infissa** in cui gli operatori binari si trovano in mezzo ai loro operandi. La sintassi degli operatori è per la maggior parte quella adottata in molti altri linguaggi di programmazione, con alcune eccezioni. Qui vediamo esempi di utilizzo degli operatori di somma, sottrazione e moltiplicazione:

```python
>>> 2 + 3
5
>>> 2 - 3
-1
>>> 2 * (3 + 4)
14
```

Gli operatori relazionali hanno la stessa sintassi di C e Java. In particolare, l'operatore di uguaglianza è `==` e la disuguaglianza è `!=`. Per esempio:

```python
>>> 3 < 2               # minore stretto
False
>>> 3 >= 2              # maggiore o uguale
True
>>> 3 == 2              # uguale a
False
>>> 3 != 2              # diverso da
True
```

 I **connettivi logici** sono scritti in lettere e non in forma simbolica. Avremo quindi

```python
>>> True and False      # and = congiunzione logica
False
>>> True or False       # or = disgiunzione logica
True
>>> not True            # not = negazione logica
False
```

Altri operatori meno convenzionali sono l'elevamento a potenza `**` e la divisione intera `//`, mentre `/` produce sempre (in Python 3) un valore in virgola mobile:

```python
>>> 2 ** 32
4294967296
>>> 3 / 2
1.5
>>> 3 // 2
1
>>> 4 / 2
2.0
```

### 1.4 Funzioni

Una **funzione** è un blocco di codice che esegue un calcolo a partire da zero o più argomenti (che rappresentano l'input della funzione) e produce un risultato (l'output della funzione). Per esempio, la funzione

```python
def absolute(x):
    if x >= 0: return x
    else: return -x
```

calcola il valore assoluto dell'argomento `x`. La definizione inizia con la parola chiave `def` seguita dal nome della funzione (`absolute`) e dall'elenco degli argomenti, in questo caso il solo argomento `x`. Il **corpo** della funzione è il codice che segue i due punti `:` **indentato** di 4 spazi rispetto al resto del programma. L'indentazione è fondamentale perché permette a Python di capire fin dove si estende il corpo della funzione. Il costrutto `if-else` è analogo a quello del linguaggio C. Il comando `return` causa la terminazione della funzione con la produzione del risultato indicato subito dopo la parola chiave `return`.

Per applicare la funzione ai suoi argomenti se ne scrive il nome seguito dalla lista di argomenti tra parentesi. Per esempio:

```python
>>> absolute(3)
3
>>> absolute(-3)
3
```

Un **predicato** è una funzione che restituisce `True` o `False` a seconda che i suoi argomenti soddisfino o meno il predicato. Per esempio, la funzione `divides` definita come

```python
def divides(i, n): return n % i == 0
```

rappresenta il predicato che stabilisce se `i` divide `n`. Dunque, avremo

```python
>>> divides(2, 4)
True
>>> divides(2, 3)
False
```

### 1.5 Moduli

La libreria di Python è organizzata in **moduli** che contengono definizioni raggruppate per tema/struttura dati. Prima di utilizzare le definizioni contenute in un modulo, il modulo deve essere **importato** con una clausola `import`, solitamente situata all'inizio dello script. Per esempio, il seguente script definisce una funzione per calcolare l'area di un cerchio noto il raggio, facendo uso della costante $\pi$ definita nel modulo `math`:

```python
import math

def area(r):
    return math.pi * r ** 2
```

Per riferirsi a una costante/funzione definita in un modulo diverso da quello corrente è necessario specificarne il **percorso** completo composto da nome del modulo `math`, un punto `.` ed il nome della costante/funzione. Dunque, `math.pi` fa riferimento alla definizione di `pi` nel modulo `math`.

A volte è più comodo importare solo specifiche definizioni da un modulo, senza doverne indicare il percorso completo. In tal caso si usa una variante della clausola `import`, come illustrato qui sotto:

```python
from math import pi

def area(r):
    return pi * r ** 2
```

In questi casi occorre evitare che ci sia conflitto tra le definizioni importate e quelle definite all'interno del modulo corrente.

### 1.6 Esercizi

Definire funzioni per:

1. calcolare la somma dei numeri naturali da 1 a $n$ usando la formula diretta $\frac{n(n+1)}2$ (attenzione: il risultato deve essere un numero intero);
2. calcolare lato $l$, apotema $a$, perimetro $P$ e area $A$ di un poligono regolare con $n$ lati e raggio $r$, ricordando che $l = 2r\sin\frac\pi{n}$ e $a = r\cos\frac\pi{n}$ (suggerimento: il [modulo `math`](https://docs.python.org/3/library/math.html) contiene, tra altre, funzioni Python corrispondenti alle funzioni trigonometriche $\sin$ e $\cos$).

[Soluzioni]({% link assets/downloads/CorsoPython/soluzioni_base.py %})

## 2. Programmazione imperativa

Per **programmazione imperativa** si intende un paradigma di programmazione in cui il programma elenca una sequenza di comandi da eseguire in ordine. Ogni comando *modifica* lo stato dal calcolatore, per esempio alterando il contenuto della memoria, leggendo o scrivendo dati da o su disco, stabilendo connessioni con server remoti, ecc.

### 2.1 Variabili

Come tutti i linguaggi di programmazione imperativa, Python fa uso di **variabili** come contenitori per l'immagazzinamento temporaneo di dati. Il seguente programma

```python
>>> x = 2 ** 32
```

assegna alla variabile `x` il valore $2^{32}$. Da ora in avanti si può scrivere `x` per leggere e usare il valore della variabile. Ad esempio, avremo

```python
>>> x
4294967296
>>> x // 2 == 2 ** 31
True
```

Il **valore** assegnato alla variabile `x` può essere modificato da un successivo **comando di assegnamento**. Per esempio, scrivendo

```python
>>> x = x + 1
```

incrementiamo di uno il valore della variabile `x`. Non bisogna confondere l'operatore `=` usato qui - che rappresenta il comando di **assegnamento** - con l'operatore `==` usato in precedenza - che rappresenta l'operatore di **uguaglianza**. In altri termini, l'**espressione** `e == f` significa "confronta il valore dell'espressione `e` ed il valore dell'espressione `f`, se sono uguali il risultato è `True`, altrimenti `False`". Al contrario, il **comando** `x = f` significa "modifica la variabile `x` con il valore di `f`".

Come in Java e C, i comandi di assegnamento che leggono e modificano la stessa variabile possono essere scritti in forma compatta. Per esempio, l'assegnamento `x = x + 1` può essere scritto anche come `x += 1` senza dover ripetere il nome della variabile nella parte a destra del simbolo `=`.

### 2.2 Scope delle variabili

Una variabile definita al di fuori di ogni funzione è detta **globale** ed è visibile e modificabile ovunque nello script successivamente alla sua prima inizializzazione. Una variabile definita all'interno di una funzione è detta **locale** ed è visibile e modificabile solo all'interno della funzione. Per esempio, dato lo script

```python
a = 1            # definisce una variabile globale a
def test():
    a = 2        # definisce una variabile locale a
    print("funzione test applicata")
```

avremo

```python
>>> a
1
>>> test()
funzione test applicata
>>> a
1
```

Se si vuole modificare una variabile globale all'interno di una funzione, è necessario dichiararla esplicitamente globale prima del primo utilizzo. Per esempio, dato il codice

```python
a = 1            # definisce una variabile globale a
def test():
    global a
    a = 2        # modifica la variabile globale a
    print("funzione test applicata")
```

avremo

```python
>>> a
1
>>> test()
funzione test applicata
>>> a
2
```

### 2.3 Il comando iterativo `while`

Il comando iterativo `while` serve a indicare l'esecuzione ripetuta di un blocco di codice, fintantiché l'espressione specificata di seguito a `while` ha valore `True`. Seguono alcuni esempi di funzioni che fanno uso del comando iterativo `while`. La seguente funzione calcola il fattoriale di un numero intero $n$, ovvero $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$:

```python
def factorial(n):
    assert n >= 0   # se n < 0 la funzione non termina
    r = 1
    while n > 0:    # fintantoché n > 0
        r = r * n   # moltiplica il risultato parziale per n
        n = n - 1   # decrementa n
    return r
```

* Il comando `assert` specifica una **precondizione**, ovvero una proprietà che l'argomento `n` deve soddisfare affinché la funzione possa completare il calcolo correttamente. In questo caso, indichiamo che la funzione è in grado di calcolare il fattoriale di `n` per ogni `n` non negativo.
* Il comando `while` identifica un blocco di codice da eseguire fintantoché la condizione specificata `n > 0` risulta essere vera. Python usa l'indentazione del codice per capire l'estensione del corpo del ciclo `while`.

Seguono alcuni esempi di applicazione della funzione:

```python
>>> factorial(0)
1
>>> factorial(10)
3628800
>>> factorial(50)
30414093201713378043612608166064768844377641568960512000000000000
```

L'ultimo esempio in particolare ci permette di apprezzare il fatto che in Python i numeri interi sono a precisione arbitraria.

La seguente funzione definisce il predicato "essere un numero primo":

```python
def prime(n):
    assert n >= 0
    d = 2                           # cerca divisori da 2...
    while d <= n // 2:              # ... fino a n / 2 incluso
        if n % d == 0:              # se trovo divisore...
            return False            # ... n non è primo
        d += 1                      # passa al successivo
    return n > 1                    # nessun divisore trovato, n primo
```

* L'operatore `%` calcola il resto della divisione intera.
* Si può usare il comando `return` per interrompere l'esecuzione della funzione in qualunque momento, laddove il risultato finale è disponibile.
* La parte `else` del comando `if` è opzionale. Di nuovo, l'indentazione consente a Python di capire cosa fa parte dell'`if`, cosa del corpo del `while` e cosa del corpo della funzione.
* Il comando `d += 1` è l'abbreviazione di `d = d + 1`.

Seguono alcuni esempi di applicazione della funzione:

```python
>>> prime(2)
True
>>> prime(101)
True
>>> prime(100)
False
```

La seguente funzione calcola il **massimo comun divisore** di due numeri interi usando (una versione del) l'algoritmo di Euclide:

```python
def euclid(m, n):
    assert m > 0 and n > 0
    while m != n:
        if m < n:
            m, n = n, m
        m -= n
    return m
```

* Il comando `m, n = n, m` effettua l'assegnamento simultaneo delle variabili `m` ed `n` con i vecchi valori di `n` ed `m`. In questo caso, l'assegnamento simultaneo è comodo per **scambiare** il contenuto delle variabili `m` ed `n` senza usare esplicitamente una variabile d'appoggio.
* Il comando `m -= n` è l'abbreviazione di `m = m - n`. Questa sintassi abbreviata si può applicare a tutti i comandi di assegnamento di questa forma per tutti gli operatori binari.

### 2.4 Esercizi

Definire funzioni per:

1. calcolare la somma dei numeri naturali da $1$ a $n$ con una iterazione;
2. stampare tutti i numeri primi da $2$ a $n$, facendo uso della funzione `prime` definita in precedenza;
3. trovare il primo numero primo maggiore o uguale a un numero $n$ dato;
4. contare il numero di 1 nella rappresentazione binaria di un numero naturale.

[Soluzioni]({% link assets/downloads/CorsoPython/soluzioni_imp.py %})

## 3. Sequenze

Python fornisce vari tipi di dato "sequenza" per rappresentare collezioni lineari di dati. Alcuni tipi sequenza sono **immutabili** ed altri **mutabili**. I primi si distinguono dai secondi perché non possono essere modificati una volta creati. Al limite, si può ottenere una nuova sequenza che rappresenta quella originaria in cui sono stati effettuati gli aggiornamenti opportuni. Di seguito sono elencati i principali tipi sequenza di Python:

* **stringhe**, ovvero sequenze immutabili di **caratteri**;
* **intervalli**, ovvero sequenze immutabili di numeri interi;
* **tuple**, ovvero sequenze immutabili di valori di tipo arbitrario, non necessariamente omogenee;
* **liste**, ovvero sequenze mutabili di valori di tipo arbitrario, solitamente omogenee.

### 3.1 Creazione di sequenze

Le stringhe sono racchiuse tra singoli o doppi apici, ad esempio:

```python
>>> "ciao"
'ciao'
>>> "po'"
"po'"
>>> '"Ciao", disse'
'"Ciao", disse'
```

Gli intervalli si creano con la funzione `range` applicata a uno, due o tre argomenti:

```python
>>> range(10)
range(0, 10)
>>> range(1, 10)
range(1, 10)
>>> range(1, 10, 2)
range(1, 10, 2)
```

* La versione a un solo argomento `n` rappresenta l'intervallo dei numeri interi compresi tra 0 (incluso) ed `n` (escluso). Dunque, `range(10)` rappresenta l'intervallo $[0..9]$;
* La versione a due argomenti `m` ed `n` rappresenta l'intervallo dei numeri interi compresi tra `m` (incluso) ed `n` (escluso). Dunque, `range(1, 10)` rappresenta l'intervallo $[1..9]$;
* La versione a tre argomenti `m`, `n` ed `s` rappresenta l'intervallo dei numeri interi compresi tra `m` (incluso) ed `n` (escluso) a passi di `s`. Dunque, `range(1, 10, 2)` rappresenta la sequenza $[1, 3, 5, 7, 9]$.

Le tuple di creano separando i loro elementi con virgole e solitamente (ma non necessariamente) racchiudendoli tra parentesi tonde. Ad esempio:

```python
>>> (1, 2)
(1, 2)
>>> (True, "Ciao", 5)
(True, 'Ciao', 5)
```

La tupla vuota si rappresenta con `()` e la tupla con un solo elemento `e` con `(e,)`.

Le liste si creano racchiudendo i loro elementi separati da virgole tra parentesi quadre. Ad esempio:

```python
>>> [1, 2]
[1, 2]
>>> [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
>>> ["Queste", "sono", "stringhe", "in", "una", "lista"]
['Queste', 'sono', 'stringhe', 'in', 'una', 'lista']
```

La lista vuota si rappresenta con `[]`. Vedremo in seguito modi più flessibili di creare liste con le cosiddette *list comprehension*.

Tutte le sequenze supportano alcune operazioni in comune, le più importanti sono:

* `len(s)`, che determina la lunghezza della sequenza `s`;
* `+`, che concatena due sequenze dello stesso tipo;
* `s[m]` che accede all'elemento in posizione `m` nella sequenza `s`, ricordando che il primo elemento si trova in posizione 0.
* `s[m:n]` che produce una **slice** (cioè una "fetta") della sequenza `s` dalla posizione `m` (inclusa) alla posizione `n` (esclusa). Sia `m` che `n` possono essere omessi, nel qual caso assumono il loro valore di default (rispettivamente, 0 e la lunghezza della sequenza). Dunque, `s[:n]` produce il prefisso di `s` fino alla posizione `n` (esclusa), `s[m:]` produce il suffisso di `s` a partire dalla posizione `m` (inclusa), e `s[:]` produce una copia di `s`.

Seguono alcuni esempi di queste operazioni:

```python
>>> len(range(10))
10
>>> len(range(1, 10))
9
>>> len(range(1, 10, 2))
5
>>> (1, 2) + (True,)
(1, 2, True)
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> (1, 2)[0]
1
>>> [1, 2, 3][1]
2
>>> range(10)[5:]
range(5, 10)
>>> "Queste", "sono", "stringhe", "in", "una", "lista"][1:4]
['sono', 'stringhe', 'in']
>>> 'sono'[1:3]
'on'
```

Le liste, in quanto **sequenze mutabili**, possono essere modificate, ad esempio aggiungendo/rimuovendo elementi ed anche sovrascrivendo un elemento già esistente. Ad esempio:

```python
>>> l = [1, 2, 3]       # crea una lista l con 3 elementi
>>> l.append(4)         # aggiunge in fondo alla lista l'elemento 4
>>> l                   # ora l ha un elemento in più
[1, 2, 3, 4]
>>> l[2] = 5            # sovrascrive l'elemento in posizione 2 con 5
>>> l
[1, 2, 5, 4]
```

Questo esempio ci consente di osservare un caso di invocazione di *metodo* (`append`). Un metodo è un blocco di codice analogo a una funzione tranne per il fatto che rappresenta un'operazione da indirizzare a un oggetto specifico, in questo caso la lista `l` alla quale si vuole aggiungere l'elemento 4. L'oggetto a cui il metodo è indirizzato nell'invocazione è specificato a *sinistra* del nome del metodo, prima del simbolo `.`, e a volte è detto **oggetto ricevente** (l'invocazione del metodo).

### 3.2 Il comando iterativo `for`

Tutte le sequenze sono **iterabili**, ovvero è possibile specificare (attraverso il comando `for`) un'azione da eseguire su ogni elemento della sequenza. Per esempio, il comando

```python
for i in range(10):
    print(i, '² = ', i ** 2, sep='')
```

itera su tutti gli elementi `i` dell'intervallo $[0..9]$ e, per ciascun elemento, esegue il comando `print` indentato. Il nome `i` con cui riferirsi a ogni singolo elemento dell'intervallo è a discrezione del programmatore. L'argomento `sep=''` indica al comando Python di **non** separare gli elementi da stampare con uno spazio, come accade normalmente. Il risultato è

```python
0² = 0
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
6² = 36
7² = 49
8² = 64
9² = 81
```

### 3.3 List comprehension

È possibile creare una lista usando una notazione detta **list comprehension** che richiama la notazione usata in matematica per indicare insiemi. Per esempio, useremo

```python
>>> [ i ** 2 for i in range(10) ]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

per creare la **lista** dei quadrati dei numeri naturali nell'intervallo $[0..9]$. La notazione utilizzata richiama
$$\{ i^2 \mid i\in[0..9] \}$$
usata per denotare l'insieme dei quadrati dei numeri naturali nell'intervallo $[0..9]$. La parte a sinistra di `for` nella list comprehension è un'espressione che produce i singoli elementi della lista. In generale, tale espressione fa uso di nomi (come `i`) che sono **generati** a destra della parola chiave `for`. Nell'esempio qui sopra il generatore è un intervallo, ma è possibile generare liste a partire da altre sequenze. Per esempio

```python
>>> [ ord(c) for c in "ciao" ]
[99, 105, 97, 111]
```

genera la lista dei codici (Unicode) corrispondenti ai caratteri della stringa `"ciao"`. La funzione di libreria `ord` determina il codice corrispondente a un singolo carattere.

È possibile inserire dei **filtri** che selezionano gli elementi di interesse nella lista generata. Per esempio

```python
>>> [ i for i in range(20) if i % 3 == 0 ]
[0, 3, 6, 9, 12, 15, 18]
```

genera la lista dei multipli di 3 compresi tra 0 e 19, mentre

```python
>>> [ i for i in range(50) if prime(i) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

calcola la lista dei numeri primi compresi tra 0 e 49. Infine, è possibile usare più generatori. Ad esempio

```python
>>> [ (m, n) for m in range(5) for n in range(5) if m < n ]
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

genera la lista delle coppie ordinate di numeri naturali compresi tra 0 e 4.

### 3.4 Esercizi

Usando opportunamente `for` e list comprehension ma non il comando `while`, definire funzioni per:

1. calcolare il fattoriale di un numero naturale `n`;
2. calcolare la lista dei divisori di un numero naturale `n`;
3. determinare se un numero `n` è primo senza usare iterazioni (suggerimento: usare la soluzione dell'esercizio precedente);
4. ottenere da una lista $l$ ed un numero $x$ una coppia di liste $l_1$ ed $l_2$ tali che $l_1$ contiene tutti gli elementi di $l$ minori o uguali ad $x$ ed $l_2$ contiene tutti gli elementi di $l$ maggiori di $x$;
5. determinare se una lista è ordinata in modo non decrescente.

[Soluzioni]({% link assets/downloads/CorsoPython/soluzioni_seq.py %})

## 4. Dizionari e file

Le collezioni che abbiamo considerato fino ad ora sono caratterizzate dal fatto di consentire un accesso *posizionale* ai loro elementi. Come abbiamo visto, data una sequenza `s` ed un numero intero `n` compreso tra 0 e la lunghezza della sequenza meno uno, l'espressione `s[n]` ci permette di leggere ed eventualmente modificare l'elemento che si trova in posizione `n`.

Dizionari e file sono altre collezioni fondamentali di elementi con caratteristiche diverse da quelle viste fino ad ora. Nei primi, l'accesso agli elementi non avviene attraverso la loro posizione, ma più genericamente per mezzo di una *chiave*. I secondi risiedono su disco, e dunque rappresentano collezioni *permanenti* che "sopravvivono" alla terminazione dello script e allo spegnimento del calcolatore.

### 4.1 Motivazione e uso dei dizionari

Per illustrare l'utilità dei dizionari, consideriamo il problema di tradurre i nomi dei giorni della settimana dall'inglese all'italiano, e viceversa. Usando le nozioni accumulate fino ad ora, una soluzione potrebbe essere la seguente

```python
def inglese_italiano(day):
    if day == "monday": return "lunedì"
    elif day == "tuesday": return "martedì"
    elif day == "wednesday": return "mercoledì"
    elif day == "thursday": return "giovedì"
    elif day == "friday": return "venerdì"
    elif day == "saturday": return "sabato"
    elif day == "sunday": return "domenica"
    else: assert False
```

in cui usiamo una cascata di `if-elif` per prendere in considerazione tutte le possibilità.

Questa soluzione ha alcuni difetti fondamentali: intanto, la funzione è poco efficiente, in quanto effettua una serie lineare di confronti tra stringhe per individuare il caso giusto; inoltre, la funzione non scala a situazioni in cui il numero di associazioni da stabilire è più elevato e/o non è determinabile a priori dal programmatore, ma è calcolato da altre informazioni (notare che `inglese_italiano` risolve solo una direzione particolare delle traduzioni, e che l'altra traduzione richiederebbe la scrittura di una funzione analoga).

I problemi evidenziati possono essere risolti facendo uso di un *dizionario* che associ i giorni della settimana in inglese ai loro corrispettivi in italiano. Il seguente codice crea un nuovo dizionario (con l'invocazione `dict()`) e lo popola con le associazioni richieste:

```python
ei = dict()                   # crea un nuovo dizionario vuoto
ei["monday"] = "lunedì"       # associa a "monday" la parola "lunedì"
ei["tuesday"] = "martedì"     # associa a "tuesday" la parola "martedì"
ei["wednesday"] = "mercoledì" # ... e così via
ei["thursday"] = "giovedì"
ei["friday"] = "venerdì"
ei["saturday"] = "sabato"
ei["sunday"] = "domenica"
```

Ora avremo, ad esempio:

```python
>>> ei['monday']              # legge il valore associato a "monday"
'lunedì'
>>> ei['sunday']              # legge il valore associato a "sunday"
'domenica'
>>> ei['boh']                 # nessun valore associato a "boh"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'boh'
```

Nell'ultimo caso otteniamo (giustamente) un errore in quanto il dizionario non contiene un valore associato alla chiave `'boh'`. Grazie al dizionario `ei`, possiamo implementare la funzione di traduzione dall'inglese all'italiano nel modo seguente:

```python
def english_italian(day):
    return ei[day]
```

È vero che l'inizializzazione del dizionario ci è costata - in termini di linee di codice - una fatica analoga a quella della prima funzione di traduzione, ma occorre considerare che l'accesso al dizionario con `ei[day]` è molto più efficiente di una sequenza lineare di confronti tra stringhe. Inoltre, aver creato un dizionario con le corrispondenze dall'inglese all'italiano ci fornisce un modo automatico di creare il dizionario con le corrispondenze invertite. A tal fine, osserviamo che il metodo

```python
>>> ei.items()
dict_items([('monday', 'lunedì'), ('tuesday', 'martedì'),
            ('wednesday', 'mercoledì'), ('thursday', 'giovedì'),
            ('friday', 'venerdì'), ('saturday', 'sabato'),
            ('sunday', 'domenica')])
```

produce una lista di coppie con le associazioni contenute nel dizionario. È facile allora creare il dizionario italiano-inglese così

```python
ie = dict([ (i, e) for (e, i) in ei.items() ])
```

invertendo le coppie prodotte da `ei.items()` e creando ed inizializzando un nuovo dizionario `ie` passando a `dict` la lista risultante dall'inversione. Ora abbiamo, ad esempio

```python
>>> ie["sabato"]
'saturday'
```

e la funzione di traduzione si riduce a

```python
def italian_english(giorno):
    return ie[giorno]
```

### 4.2 Apertura e lettura di file di testo

Un file di testo può essere considerato alla stregua di una collezione/sequenza di stringhe, una per ogni riga di testo nel file, che risiede su disco. Ad esempio, la seguente funzione conta il numero di righe, parole e caratteri presenti nel file di testo specificato come argomento, realizzando di fatto lo stesso comportamento del comando `wc` di Unix:

```python
def count(filename):
    lines, words, chars = 0, 0, 0   # inizializza i tre contatori a zero
    f = open(filename)              # apre il file
    for line in f:                  # per ogni riga
        lines += 1                  # incrementa il numero di righe
        chars += len(line)          # incrementa il numero di caratteri
        words += len(line.split())  # incrementa il numero di parole
    print(lines, words, chars, filename)    # stampa i contatori
```

La funzione `open` apre il file dal nome indicato e restituisce un **handle** - anche detto "descrittore" - `f` attraverso il quale è possibile leggere il contenuto del file. Il successivo comando `for` usa l'handle per iterare su tutte le righe del file: per ogni riga `line`, si incrementa il contatore `lines` di 1, il contatore `chars` della lunghezza della riga, ed il contatore `words` del numero di parole della riga. Per ottenere quest'ultimo valore, si invoca su `line` il metodo `split` che spezza la stringa in una lista di stringhe, ciascuna corrispondente ad una parola in `line`. Il metodo `split` considera "parola" una qualsiasi sequenza di caratteri delimitata da spazi. Ad esempio, avremo

```python
>>> "questa è una stringa con 7 parole".split()
['questa', 'è', 'una', 'stringa', 'con', '7', 'parole']
```

Un esempio leggermente più complesso è quello di una funzione che conta il numero di occorrenze di ogni parola che compare in un file di testo. In questo caso, è comodo usare un dizionario che ha parole come chiavi e numeri come valori. Il numero associato a una parola rappresenta il numero di occorrenze di quella parola nel file. La funzione che risolve il problema è

```python
def collect(filename):
    d = dict()
    f = open(filename)
    for line in f:
        for word in line.split():
            if word.isalpha():
                d[word] = d.get(word, 0) + 1
    return d
```

che crea un dizionario vuoto con l'invocazione `dict()` e itera su tutte le righe del documento. Ogni parola di ogni riga è esaminata e, se è composta da soli caratteri alfabetici, usata come chiave per incrementare il contatore corrispondente nel dizionario.

Note

* L'invocazione del metodo `word.isalpha()` restituisce `True` o `False` a seconda che `word` sia composta di soli caratteri alfabetici o meno.
* L'invocazione del metodo `d.get(word, 0)` legge nel dizionario `d` il valore associato alla chiave `word`. Se non c'è alcun valore associato a `word`, ovvero se è la prima volta che si incontra la parola `word`, allora il valore restituito dal metodo `get` è 0.

Per completare l'esercizio definiamo una funzione che visualizza sul terminale il contenuto del dizionario creato da `collect`, ordinato per numero decrescente di occorrenze:

```python
def show_results(d):
    l = [ (c, w) for (w, c) in d.items() ]
    l.sort(reverse=True)
    for (c, w) in l:
        print(w, "=", c)
```

Note

* Il generatore `for (w, c) in d.items()` lega direttamente ai due nomi `w` e `c` la parola ed il contatore di ciascuna coppia restituita da `d.items()`.
* La lista `l` differisce dalla lista `d.items()` in quanto le coppie hanno le componenti a posizioni invertite. Questo è utile per poter ordinare la lista in base al numero di occorrenze delle parole, e non in base all'ordine lessicografico delle parole stesse.
* Il metodo `l.sort(reverse=True)` ordina la lista `l`. L'argomento `reverse=True` indica a Python che siamo interessati all'ordine decrescente.

### 4.3 Esercizi

Il file [log.txt]({% link assets/downloads/CorsoPython/log.txt %})
contiene i dati di un Web server sugli accessi ad una pagina
HTML. Ogni riga del file indica un accesso alla pagina ed inizia con
l'indirizzo IP della macchina dalla quale l'accesso è avvenuto. Come
esercizio, scrivere un programma Python che estrae gli indirizzi IP
all'inizio di ogni riga del file, contarne le occorrenze e
presentare i dati sugli accessi sotto forma di istogramma (un
frammento di risultato è riportato qui sotto).

```text
79.226.254.210  ##################################################
93.88.113.130   #################################
79.20.227.208   ##############
82.73.192.154   ###########
97.88.254.194   #########
89.160.237.92   #########
212.185.189.67  #########
154.59.123.106  #########
129.217.131.41  #########
82.227.70.214   ########
147.91.173.31   ########
146.148.64.128  ########
```

Suggerimenti

* Per risolvere l'esercizio, adattare le funzioni `collect` e `show_results` mostrate in precedenza.
* Per allineare l'inizio di tutti gli istogrammi a prescindere dalla lunghezza dei singoli indirizzi IP è utile usare il [metodo `ljust`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) per le stringhe.
* Usare `'#' * n` per ottenere la stringa composta da `n` occorrenze del carattere `#`. In generale, se `s` è una stringa ed `n` è un numero, `s * n` è la stringa formata da `n` occorrenze di `s` concatenate in sequenza.

[Soluzione]({% link assets/downloads/CorsoPython/soluzioni_file.py %})

## 5. Programmazione funzionale

Nel paradigma di programmazione **funzionale** l'enfasi è posta sulla trasformazione di dati, possibilmente in passaggi successivi, per mezzo dell'applicazione di funzioni (o trasformazioni). Python è un linguaggio di programmazione **multi paradigma**, intendendo con ciò il fatto che integra al proprio intero diversi paradigmi di programmazione tra cui quello imperativo (già introdotto in una sezione precedente), quello funzionale e quello object-oriented.

Un aspetto tipico e caratterizzante del paradigma funzionale è che le funzioni sono valori di **prima classe**, intendendo con ciò che è possibile fare con le funzioni "tutto" quello che si può fare con i dati: è possibile memorizzare funzioni in strutture dati (ad esempio, in tuple e liste), è possibile definire funzioni che accettano come argomenti altre funzioni, ed è possibile definire funzioni che producono una funzione come risultato.

In questa sezione vediamo come queste caratteristiche delle funzioni Python consentano la scrittura di codice più compatto e senza uso di cicli o altri costrutti tipici del paradigma imperativo.

### 5.1 Funzioni di ordine superiore

Una funzione che ha tra i suoi argomenti un'altra funzione si dice **di ordine superiore**. Un esempio classico di funzione di ordine superiore è quella che calcola l'integrale definito di una funzione $f$ in un intervallo $[a,b]$. Ricordando che l'integrale di una funzione corrisponde (grosso modo) all'area del piano compresa tra la funzione e l'asse orizzontale, possiamo approssimare l'integrale definito di $f$ **campionando** la funzione a intervalli regolari e calcolando la somma delle aree delle figure geometriche risultanti dal campionamento. Nel caso più semplice, possiamo approssimare l'integrale di $f$ calcolando la somma delle aree di $n$ rettangoli, nel modo sequente:

$$\int_a^b f(x)dx \approx h\sum_{i=0}^{n-1} f(a + ih)$$

dove $h = (b - a) / n$ è l'altezza (*height*) degli $n$ rettangoli. È inteso che tale approssimazione è tanto migliore quanto più grande è il numero $n$ di rettangoli che consideriamo.

In Python scriveremo allora la seguente funzione di ordine superiore

```python
def rectangles(f, a, b, n):
    assert n > 0
    h = (b - a) / n         # h = altezza dei rettangoli
    s = 0                   # somma parziale delle basi dei rettangoli
    for i in range(n):
        s += f(a + i * h)   # base del rettangolo i-esimo
    return s * h            # area = somma basi * altezza
```

in cui il primo argomento `f` è a sua volta una funzione Python che
rappresenta la funzione della quale vogliamo approssimare
l'integrale. Per esempio, possiamo calcolare

```python
>>> rectangles(math.exp, 0, 1, 10)
1.6337993999663625
>>> rectangles(math.exp, 0, 1, 100)
1.7097047383081216
>>> rectangles(math.exp, 0, 1, 1000)
1.7174228307349666
```

in cui `math.exp` è la funzione Python che rappresenta
l'esponenziale $e^x$ e notiamo che il risultato migliora
all'aumentare di $n$, avvicinandosi sempre più al valore di $e - 1$.

### 5.2 Funzioni anonime

Nell'esempio precedente, la funzione `math.exp` della quale vogliamo
calcolare l'integrale è già definita nella libreria standard di
Python, pertanto è sufficiente indicarne il nome. In alternativa,
possiamo definire noi stessi la funzione di cui calcolare
l'integrale approssimato:

```python
>>> def g(x): return x ** 2
...
>>> rectangles(g, 0, 1, 10)
0.2850000000000001
>>> rectangles(g, 0, 1, 100)
0.32835000000000003
>>> rectangles(g, 0, 1, 1000)
0.33283349999999995
```

Qui abbiamo definito la funzione Python `g` che rappresenta la
funzione $g(x) = x^2$ e di nuovo notiamo che l'integrale definito
converge verso la soluzione esatta ($\frac13$).

Laddove occorre una funzione Python semplice, ma che non è già
definita nello script o nella libreria standard, è possibile
definirla "al volo" attraverso una cosiddetta **lambda**. Per
esempio, lo stesso integrale di `g` visto qui sopra può essere
calcolato come

```python
>>> rectangles(lambda x: x ** 2, 0, 1, 10)
0.2850000000000001
```

dove `lambda x: x ** 2` rappresenta una funzione anonima a un
singolo argomento `x` che calcola `x ** 2`. Argomenti e corpo della
funzione anonima sono separati da `:`.

Una `lambda` è una funzione a tutti gli effetti e può essere
applicata ai suoi argomenti con la notazione convenzionale, in cui
gli argomenti sono forniti tra parentesi di seguito alla funzione:

```python
>>> (lambda x: x ** 2)(2)
4
>>> (lambda x, y: x + y)(2, 3)
5
```

### 5.3 Riduzione di liste con `reduce`

Un'operazione frequente consiste nel **ridurre** una sequenza "combinandone" tutti gli elementi secondo un'operazione specifica. Per esempio, data la lista

$$[a_1, a_2, \dots, a_n]$$

potremmo voler calcolare la somma $\sum_{i=1}^n a_i$ oppure il prodotto $\prod_{i=1}^n a_i$ di tutti i suoi elementi. Queste operazioni corrispondono a combinare gli elementi della lista secondo operazioni specifiche (ad esempio, somma e prodotto): si sommano il primo ed il secondo elemento, il risultato si somma con il terzo, e così via fino a "ridurre" l'intera lista ad un singolo valore. L'associatività di somma e prodotto garantisce che il risultato della riduzione è ben definito, ovvero che esso non dipende dal particolare ordine in cui gli elementi della lista sono combinati.

Non è difficile definire funzioni Python che realizzano queste riduzioni:

```python
def add_all(l):
    r = 0           # risultato parziale
    for x in l:     # per ogni x in l...
        r += x      # ...somma x al risultato parziale
    return r

def mul_all(l):
    r = 1           # risultato parziale
    for x in l:     # per ogni x in l...
        r *= x      # ...moltiplica x al risultato parziale
    return r
```

Tuttavia, è evidente che `add_all` e `mul_all` condividono la stessa struttura e differiscono solo per l'operazione (`+` o `*`) che consente loro di combinare gli elementi della lista `l`. Sarebbe auspicabile poter definire una volta per tutte la funzione che riduce una sequenza rendendola parametrica nel tipo di combinazione da effettuare, un po' come la funzione di integrazione era parametrica nella funzione da integrare. In Python questa funzione di riduzione si chiama `reduce` ed è fornita nel modulo `functools` della libreria standard. Per esempio, possiamo sommare e moltiplicare tutti gli elementi di una lista così

```python
>>> from functools import reduce
>>> reduce(lambda x, y: x + y, [1, 2, 3, 4])
10
>>> reduce(lambda x, y: x * y, [1, 2, 3, 4])
24
```

dove la funzione che combina gli elementi è specificata con una `lambda`.

Note

* Se la lista da combinare può essere vuota, la funzione `reduce`
  non è in grado di produrre un risultato sensato in generale. In
  questi casi è possibile fornire a `reduce` un terzo argomento con
  il valore da produrre nel caso un cui la lista sia vuota. Questo
  caso era previsto nella definizione di `add_all` e `mul_all` qui
  sopra, e produceva l'elemento neutro (rispettivamente, 0 o 1) di
  somma e prodotto.
* Alcune semplici funzioni, come quelle che sommano o moltiplicano i
  loro argomenti, sono frequenti e dunque predefinite nella libreria
  standard. Ad esempio, il modulo `operator` definisce funzioni
  corrispondenti agli operatori del linguaggio Python. Le funzioni
  `operator.add` e `operator.mul` sono equivalenti a `lambda x, y:
  x + y` e `lambda x, y: x * y` rispettivamente.

### 5.4 Esercizi

Senza usare iterazioni (con `while` e `for`), ma usando invece list comprehension, funzioni di ordine superiore e `reduce`, definire funzioni per:

1. calcolare il fattoriale di un numero $n$;
2. calcolare il **coefficiente binomiale generalizzato** di $\alpha$ e $k$, ovvero

$$\left(\alpha\atop k\right) = \frac{1}{k!}\prod_{h=0}^{k-1}(\alpha - h)$$

3. calcolare l'integrale definito di una funzione $f$ nell'intervallo $[a,b]$ con il metodo dei rettangoli;
4. calcolare la **somma** ed il **prodotto scalare** di due vettori, rappresentati come liste di numeri. Suggerimento: osservare il risultato di `list(zip([1,2,3], [4,5,6]))` e usare la funzione `zip`;
5. calcolare la **trasposta** di una matrice rappresentata come lista di liste di numeri (ogni lista interna è una riga della matrice);
6. moltiplicare due matrici;
7. calcolare l'integrale definito di una funzione $f$ nell'intervallo $[a,b]$ con il metodo dei **trapezi** (suggerimento: usare `zip`);
8. determinare se una lista è ordinata in modo non decrescente (**attenzione**: questo esercizio differisce da quello della sezione 3.4 in quanto qui non è ammesso l'uso di iterazioni).

[Soluzioni]({% link assets/downloads/CorsoPython/soluzioni_fun.py %})

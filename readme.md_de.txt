

### **README.md**

```markdown
# A-B Wordlist Combiner

 
**Version:** 0.1a (1.7.2023)  
**Python Version:** 3.10.10 x64/amd64  

---

## Projektbeschreibung

Der **A-B Wordlist Combiner** erstellt aus zwei vorhandenen Wortlisten eine neue Wortliste, die alle möglichen Kombinationen der einzelnen Wörter enthält.  

Dies ist besonders nützlich für Brute-Force-Tests, Passwort-Generierung oder für kreative Textkombinationen.

---

## Funktionsweise

1. **Wortlisten**:  
   - Die Eingabedateien sollten einfache Textdateien sein (`.txt`) ohne Satzzeichen oder Leerzeilen.  
   - Jede Zeile enthält ein einzelnes Wort.  

   **Beispiel:**
```

Text1
Text2
Text3

````

2. **Kombinationsmethoden**:  
- **Straight:** Wörter werden in der Reihenfolge der Datei kombiniert.  
- **Shuffled:** Wörter werden vor der Kombination zufällig gemischt.  

3. **Trennzeichen für Kombinationen**:  
- Standardmäßig `-`  
- Optional: Leerzeichen oder ein benutzerdefiniertes Zeichen  

4. **Ausgabe**:  
- Alle Kombinationen werden in einer Datei `combinations.txt` im Arbeitsverzeichnis gespeichert.  

---

## Nutzung

1. **Starten des Programms**:
```bash
python AB_Wordlist_Combiner.py
````

2. **Eingabeaufforderungen**:

   * Auswahl der Kombinationsmethode:

     ```
     1 = Straight
     2 = Shuffled
     ```
   * Pfad zu Wortliste A (`Name_A.txt`)

     * Leer lassen, um Standarddatei `colors.txt` zu verwenden
   * Pfad zu Wortliste B (`Name_B.txt`)

     * Leer lassen, um Standarddatei `colors.txt` zu verwenden
   * Auswahl des Trennzeichens:

     ```
     1 = '-'
     2 = ' '
     3 = Benutzerdefiniert
     ```

3. **Start der Kombination**:

   * Nach Bestätigung mit Enter startet die Erstellung der neuen Wortliste.

---

## Hinweise

* Bei großen Wortlisten kann die Kombinationsdatei sehr groß werden.
* Für sehr große Listen kann die Berechnung einige Zeit dauern.
* Die Standard-Beispielwortliste `colors.txt` kann für Testzwecke genutzt werden.

---

## Dateien im Repository

* `AB_Wordlist_Combiner.py` – Hauptskript
* `colors.txt` – Beispiel-Wortliste
* `README.md` – Projektbeschreibung

---

## Lizenz

Dieses Projekt ist für private und nicht-kommerzielle Nutzung freigegeben.

```

---

### **requirements.txt**


# Keine externen Bibliotheken benötigt

```



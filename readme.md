
```markdown
# A-B Wordlist Combiner

**Version:** 0.1a (1.7.2023)  
**Python Version:** 3.10.10 x64/amd64  

---

## Project Description

The **A-B Wordlist Combiner** creates a new wordlist from two existing wordlists by generating all possible combinations of the individual words.  

This is especially useful for brute-force testing, password generation, or creative text combinations.

---

## How It Works

1. **Wordlists**:  
   - Input files should be plain text files (`.txt`) without punctuation or empty lines.  
   - Each line contains a single word.  

   **Example:**
```

Text1
Text2
Text3

````

2. **Combination Methods**:  
- **Straight:** Words are combined in the order they appear in the file.  
- **Shuffled:** Words are randomly shuffled before combining.  

3. **Separator for Combinations**:  
- Default: `-`  
- Optional: Space or a custom character  

4. **Output**:  
- All combinations are saved in a file called `combinations.txt` in the working directory.  

---

## Usage

1. **Run the program**:
```bash
python AB_Wordlist_Combiner.py
````

2. **Prompts**:

   * Choose combination method:

     ```
     1 = Straight
     2 = Shuffled
     ```
   * Path to Wordlist A (`Name_A.txt`)

     * Leave empty to use the default file `colors.txt`
   * Path to Wordlist B (`Name_B.txt`)

     * Leave empty to use the default file `colors.txt`
   * Choose the separator:

     ```
     1 = '-'
     2 = ' '
     3 = Custom
     ```

3. **Start Combining**:

   * Press Enter to start generating the new wordlist.

---

## Notes

* Large wordlists may produce a very large output file.
* Generating combinations for large lists can take some time.
* The default example wordlist `colors.txt` can be used for testing purposes.

---

## Repository Files

* `AB_Wordlist_Combiner.py` – Main script
* `colors.txt` – Example wordlist
* `README.md` – Project description

---

### **requirements.txt**


no external Bibliotheks used

```


---

## License

This project is free for private and non-commercial use.

```




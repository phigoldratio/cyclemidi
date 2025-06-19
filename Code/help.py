from utilities import VERSION
GENERAL_HELP_MESSAGE_FR = f"""
#Cyclemidi {VERSION} - Guide d'utilisation

Bienvenue dans Cyclemidi, un puissant outil de création de séquences MIDI complexes et dynamiques en temps réel. 
Ce programme fonctionne comme un contrôleur MIDI, compatible avec des logiciels tels que FL Studio et Ableton Live.

# I. Installation et configuration

1. **Connexion MIDI :**
   Connectez Cyclemidi à votre application musicale via Ethernet. 
   Assurez-vous que chaque piste MIDI dans votre application est assignée à un canal différent.
     
---

2. **Exécution du programme :**
   - Lancez `main.py`.
   - Patientez environ **10 secondes**.
   - Appuyez sur **ENTRÉE**. Vous devriez entendre un son d'initialisation.

# II. Types de données

Cyclemidi prend en charge plusieurs types de données, chacun avec des fonctionnalités spécifiques :
     
---

## 1. **Cycles**
   - Les cycles sont la structure de base de Cyclemidi.
   - Ils définissent une suite de valeurs répétées en boucle infinie.
   - Exemple : Un cycle `(1, 2, 3)` jouera les valeurs **1**, **2**, et **3** en boucle.
     
---

## 2. **Notes**
   - Les notes MIDI sont un type de données commun dans les cycles.
   - Elles sont écrites au format **<note><octave>** (par ex. `c4`, `eb5`, `d2`).
   - Exemple d'une mélodie simple : `(c4, e4, g4, f4)`.
     
---

## 3. **Nums (Nombres)**
   - Les nums sont des nombres entiers non reproductibles directement.
   - Utiles pour automatiser ou contrôler divers paramètres.
     
---

## 4. **Accords**
   - Les accords sont un ensemble de données jouées simultanément.
   - Ils sont écrits entre crochets : `[c4 e4 g4 c5]`.
   - Vous pouvez mélanger différents types de données dans un accord.
     
---

## 5. **Références**
   - Pour automatiser des cycles, utilisez le système de références.
   - Une référence pointe vers la valeur actuelle d'un cycle. 
   - Format : `@<nom_du_cycle>`.
     Exemple : `@foo` pour référencer la valeur actuelle du cycle nommé **foo**.
     
---

## 6. **Opérations**
   - Les opérations permettent de manipuler les données.
   - Syntaxe : `{{<paramètre_gauche> <opération> <paramètre_droit>}}`.
   - Exemple : `{{@foo + 2}}` ajoute 2 à la valeur actuelle de **foo**.

## 7. None
    - Le type none ne revoie rien, et ne joue rien lorsque jouée. Pour créer une valeur none, il suffit de taper `'none'`
    - Ainsi, ce cycle est valide :
    `(c4,e4,none,g4)`

**Limitation actuelle :** Vous ne pouvez pas encore imbriquer les opérations, accords ou références (par ex. : accord dans accord, opération dans opération, etc.). Cette fonctionnalité sera ajoutée dans une mise à jour future.

# III. Les différentes opérations dans Cyclemidi

## a. Addition et soustraction (+ et -)
Ces opérations permettent :  
1. **D'additionner ou soustraire deux nombres entre eux.**  
2. **D'additionner ou soustraire deux notes.**  
3. **D'additionner ou soustraire une note et un nombre (dans cet ordre).**

### Syntaxe :
`{{<num/note> + <num/note>}}`  
`{{<num/note> - <num/note>}}`

### Notes :
- Si deux **notes** sont additionnées, leurs hauteurs respectives sont combinées.  
  Bien que cela soit rarement utile, cela peut trouver des applications spécifiques.

---

## b. Map (&)
L'opération `map` renvoie une valeur ou non en fonction d'un verrou défini par le paramètre de droite.  
Si le verrou est **0** ou **none**, la valeur n'est pas renvoyée.  
Sinon, la valeur passe normalement.

### Syntaxe :
`{{<data> & <verrou>}}`

---

## c. Random (~)
L'opération `random` génère une valeur aléatoire :  
1. **Un nombre aléatoire** compris entre le paramètre de gauche et celui de droite.  
2. **Une note aléatoire** ayant une hauteur comprise entre deux notes définies.

### Syntaxe :
`{{<num/note> ~ <num/note>}}`

# IV. Commandes dans Cyclemidi

Les commandes sont ce qui constitue une action dans Cyclemidi. Elles ont toujours la forme suivante :  
`<commande> : <arg1> ; <arg2> ; ... | <option1> : <valeur1> ; <option2> : <valeur2>`

Un message apparaît à chaque exécution de commande, utile principalement pour le débogage.

## a. **cycle**
La commande `cycle` est la plus utilisée. Elle permet de créer de nouveaux cycles.  
Syntaxe : `cycle : <nom> ; <valeur>`  

### Paramètres :
- `speed : <num>`  
  Définit la durée de chaque élément dans le cycle. Par défaut, la valeur est **1**.
- `reboot : y/n`  
  Si réglé sur **y**, le cycle redémarre au début à chaque nouvelle mesure.

---

## b. **launch**
Cette commande associe un cycle à une piste MIDI.  
Syntaxe : `launch : <cycle> ; <piste>`  

### Notes :
- Il n'y a pas de paramètres supplémentaires.
- Un cycle peut être associé à plusieurs pistes simultanément.

---

## c. **stop**
La commande `stop` arrête un cycle.  
Syntaxe : `stop : <cycle> ; <piste>`

---

## d. **mv**
La commande `mv` déplace un cycle d'une piste à une autre sans l'arrêter.  
Syntaxe : `mv : <cycle> ; <piste_d'origine> ; <piste_d'arrivée>`

---

## e. **mod**
Cette commande modifie un cycle sans l'arrêter. Cela est utile si des références pointent vers ce cycle, car l'arrêter entraînerait des références nulles.  
Syntaxe : `mod : <nom> ; <valeur>`  

### Paramètres :
- `speed : <num>`  
  Définit la durée de chaque élément dans le cycle. Par défaut, la valeur est **1**.
- `loop : y/n`  
  Définit si le cycle se répète plusieurs fois. Par défaut, la valeur est **y**.
- `reboot : y/n`  
  Si réglé sur **y**, le cycle redémarre au début à chaque nouvelle mesure.

---

## f. **exit**
Taper `exit` ferme Cyclemidi.

"""
GENERAL_HELP_MESSAGE_EN = f"""
# Welcome to Cyclemidi {VERSION}!

# I. Setup and Configuration

1. **MIDI Connection:**
   - Connect Cyclemidi to your music application via Ethernet.
   - Ensure each MIDI track in your application is assigned to a different channel.

2. **Running the Program:**
   - Run `main.py`.
   - Wait for approximately **10 seconds**.
   - Press **ENTER**. You should hear the initialization sound.

# II. Data Types

Cyclemidi supports several types of data, each with specific features:
     
---

## 1. Cycles
- Cycles are the core concept of Cyclemidi. They define a sequence of values repeated in an infinite loop.
- Example: A cycle `(1, 2, 3)` will loop through the values **1**, **2**, and **3**.
     
---

## 2. Notes
- Notes are MIDI values written as `<note><octave>` (e.g., `c4`, `eb5`, `d2`).
- Example of a simple melody: `(c4, e4, g4, f4)`.
     
---

## 3. Nums (Numbers)
- Nums are integers that cannot be played directly.
- They are useful for automation and controlling parameters.
     
---

## 4. Chords
- Chords are collections of data played simultaneously.
- They are written in brackets, e.g., `[c4 e4 g4 c5]`.
- You can mix data types within a chord.
     
---

## 5. References
- References allow you to automate and access the current value of a cycle.
- Use the `@` symbol followed by the cycle's name to reference its value.
- Example: `@foo` refers to the current value of the cycle named **foo**.
     
---

## 6. Operations
- Operations allow you to manipulate data with two parameters.
- Syntax: `{{<left_parameter> <operation> <right_parameter>}}`.
- Example: `{{@foo + 2}}` adds 2 to the current value of **foo**.
- Voir le `III` pour plus de precisions sur les operations
       
---

## 7. None
- This type when played return nothing. You can type `'none'`. For example, this cycle works :
`(c4,e4,none,c5)`

---

**Current Limitation:**  
- Nested operations, chords within chords, or operations within chords are not yet supported. This will be addressed in a future update.
     
# III. Different Operations in Cyclemidi

## a. Addition and Subtraction (+ and -)
These operations allow:  
1. **Adding or subtracting two numbers.**  
2. **Adding or subtracting two notes.**  
3. **Adding or subtracting a note and a number (in this order).**

### Syntax:
`{{<num/note> + <num/note>}}`  
`{{<num/note> - <num/note>}}`

### Notes:
- When two **notes** are added, their respective pitches are combined.  
  This is not very practical but can occasionally be useful.

---

## b. Map (&)
The `map` operation returns a value conditionally, based on the lock defined by the right-hand parameter.  
If the lock is **0** or **none**, the value is not returned.  
Otherwise, the value passes through normally.

### Syntax:
`{{<data> & <lock>}}`

---

## c. Random (~)
The `random` operation generates a random value:  
1. **A random number** between the left and right parameters.  
2. **A random note** with a pitch between two defined notes.

### Syntax:
`{{<num/note> ~ <num/note>}}`     
     
---

# IV. Commands in Cyclemidi

Commands are the actions that compose operations in Cyclemidi. They always follow this format:  
`<command> : <arg1> ; <arg2> ; ... | <option1> : <value1> ; <option2> : <value2>`

A message appears each time a command is executed, primarily useful for debugging.

## a. **cycle**
The `cycle` command is the most frequently used. It creates new cycles.  
Syntax: `cycle : <name> ; <value>`  

### Parameters:
- `speed : <num>`  
  Defines the duration of each element in the cycle. The default value is **1**.
- `reboot : y/n`  
  When set to **y**, the cycle restarts from the beginning at each new measure.

---

## b. **launch**
This command associates a cycle with a MIDI track.  
Syntax: `launch : <cycle> ; <track>`  

### Notes:
- No additional parameters are required.
- A cycle can be associated with multiple tracks simultaneously.

---

## c. **stop**
The `stop` command stops a cycle.  
Syntax: `stop : <cycle> ; <track>`

---

## d. **mv**
The `mv` command moves a cycle from one track to another without stopping it.  
Syntax: `mv : <cycle> ; <source_track> ; <destination_track>`

---

## e. **mod**
This command modifies a cycle without stopping it. This is useful if references point to this cycle, as stopping it would cause null references.  
Syntax: `mod : <name> ; <value>`  

### Parameters:
- `speed : <num>`  
  Defines the duration of each element in the cycle. The default value is **1**.
- `loop : y/n`  
  Specifies whether the cycle repeats multiple times. Default is **y**.
- `reboot : y/n`  
  When set to **y**, the cycle restarts from the beginning at each new measure.

---

## f. **exit**
Typing `exit` closes Cyclemidi.
"""

HELP_MESSAGE_EN = {}
HELP_MESSAGE_FR = {}

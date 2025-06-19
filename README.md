# cyclemidi
A python tool for programming and sending midi sequence

# Launch
Run main.py to launch CycleMidi 

# Help
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

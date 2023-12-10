# Word-Graph-Generator-and-Analyzer
Word Graph Generator and Analyzer (Natural language processing and graph-based algorithms for analyzing and generating sequences of words)

The program is a text analysis tool that reads text files, processes words, builds a graph of word relationships, and provides various functionalities for analyzing and generating word sequences.

### Overview of Program Functionality:

1. **Reading and Processing Text Files:**
   - The program reads text files from the current directory.
   - It processes the text, removing punctuation, converting to lowercase, and extracting individual words.

2. **Graph Construction:**
   - It constructs a graph where vertices represent words, and edges represent the relationship between consecutive words in the text.

3. **Basic Statistics:**
   - Displays basic statistics about the processed text, such as the number of files, total words, unique words, and the 5 rarest words.

4. **Functionality Menu:**
   - Provides a menu-driven interface to perform different operations.

### Available Functionalities:

   - **Option A: Return K Most Likely Words:**
     - Takes user input for a word and an integer K.
     - Returns the K most likely words to follow the given word in the text.

   - **Option B: Generating a Sequence of N Most Likely Words:**
     - Takes user input for a word and an integer N.
     - Generates a sequence of N most likely words to follow the given word based on graph weights.

   - **Option C: Generating a Sequence of N Words:**
     - Takes user input for a word and an integer N.
     - Generates a sequence of N words by probabilistically selecting the next word.

   - **Option D: End Program:**
     - Exits the program.

### How to Use:

1. **Run the Program:**
   - Execute the program, and it will process text files in the current directory.

2. **View Basic Statistics:**
   - The program will display basic statistics about the processed text.

3. **Select Functionality:**
   - Choose a functionality (A, B, C, or D) from the menu.

4. **Follow Prompts:**
   - Follow the prompts to input a word or an integer as required by the selected functionality.

5. **View Results:**
   - The program will execute the chosen functionality and display the results.

6. **Repeat or Exit:**
   - Choose another functionality or select option D to exit the program.

### Example Usage:

   - To find the 3 most likely words to follow a specific word, choose option A and provide the word and K.
   - To generate a sequence of 5 words based on probability, choose option C and provide the starting word and N.

Remember that the program works with the text files in the current directory, so make sure to place your text files there or modify the program to read from a specific directory if needed. 
Additionally, input validation is implemented to handle errors, such as entering non-existent words or non-integer values.

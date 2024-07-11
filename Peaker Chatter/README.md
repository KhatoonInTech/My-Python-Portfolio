Overview**

This Python-based chatbot project simulates a conversation with characters from the TV series "*Peaky Blinders*". It utilizes a keyword-based matching system to generate responses based on user input. Additionally, it maintains a conversation history using CSV files.

**Key Features:**

 - **Peaky Blinders Themed Responses:** Provides responses aligned with the Peaky Blinders TV series, including character interactions, plot references, and user sentiment analysis.
 - **Conversation History:** Maintains a record of user interactions in CSV files for future reference.
 - **User-Friendly Interface**: Offers both console-based and GUI-based interactions.
 - **Error Handling**: Includes basic error handling for file operations.

**Tech Stack:**

 - [ ] **Programming Language**:
                   Python

 - [ ] **Libraries:**

 - **tkinter**: For GUI development (front end.py)
 - **csv**: For handling CSV files (database.py)
 - **os:** For file system operations (database.py)
 - **random:** For generating random responses (bot_responses.py)
 - **PIL, ImageTk:** For image display (front_end.py)
 - **winsound:** For sound effects (consol_based.py)
 - **turtle:** For visual effects (consol_based.py)
 - **colorsys**: For color generation (consol_based.py)
 - **tabulate:** For data formatting (consol_based.py)

**File Structure:**

 - **Peaker Chatter** : Main project directory.
 - **history:** Contains the database.py file for managing conversation
   history.
 - **responses:** Contains the bot_responses.py file with chatbot responses.
 - **front_end.py**: Contains the GUI implementation.
 - **consol_based.py**: Contains the console-based implementation.

**Usage:**

 - [ ] **GUI:**
 - Run front_end.py to start the graphical user interface.
 - Interact with the chatbot through the GUI.
 
 - [ ] **Console:**
 - Run consol_based.py to start the console-based chatbot.
 - Interact with the chatbot by typing input in the console.

**Dependencies**:
 - tkinter
 - csv
 - PIL/Pillow (optional)
 - tabulate (optional)
 - winsound (optional)

**How it Works:**

 - The chatbot loads pre-defined keywords and responses from the
   bot_responses.py file.

 - It compares user input with the keywords and generates responses
   accordingly.

 - The conversation history is stored in CSV files using the database.py
   module.

 - The GUI version provides a user-friendly interface with a graphical
   representation of the conversation.

**How to run this on your system**:

 - [ ] **Install dependencies:**

    **Bash**
    *pip install tkinter csv os random tabulate pillow winsound*

 - [ ] **Run the desired version:**

 - **For GUI:** python front_end.py

 - **For console:** python consol_based.py

**Additional Notes:**

 - The code includes basic error handling for file operations.

 - The chatbot's responses are based on the Peaky Blinders theme and
   include various scenarios like greetings, questions, agreements, and
   even handling abusive language.

 - The GUI version uses Tkinter for creating the user interface and
   displaying conversation history.

 - The console version provides a basic text-based interaction.

**For Contributions:**

*Contributions are welcome! Please feel free to fork the repository and submit pull requests.*


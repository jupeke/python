# How to run Python (Atom & Command Prompt)

## Method 1 (Command Prompt): You need to know some Command Line commands but otherwise this works well.

- Open an editor (like Atom) and write some code and save it as a .py file.
- Start Command Prompt and cd to the folder containing your python code.
- Check the path to the python.exe file and copy it (File Explorer)
- In Command Prompt type the following command:

[path to python.exe folder]\python.exe [python code file]

- A real life example (note quotes around names with spaces and the empty space after ".exe"):

C:\"Program Files (x86)"\Python37-32\python.exe helloWorld.py

## Method 2 (Atom): This works otherwise nicely directly in Atom but using input() for user input does not work.

- Install Package Script (File -> Settings -> Install -> type "script")
- Note: at school skip this step: Download and install Python ( https://www.python.org/downloads/ )
- Create a new file in Atom (right-click the folder name) with name hello.py
- Type code print("Hello World!") and save
- Select Script -> Run Script
- If nothing happens, Atom does not find the python.exe file. In this case, find the file on the computer, copy the path to the folder containing the file, open Script->Configure Script, paste the address and run. Hopefully it works now..

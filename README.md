# Asteroids

I programmed the original asteroids game with python.

## How to Install the Game 

1. To play the game, go to the main page of the asteroids repo and then:
- Click the green Code button in the upper right-hand corner.
- Select "Download ZIP" from the drop-down menu.
- Extract the file and save it on your computer desktop (or another location if preferred).

2. Open a command-line environment. (Windows users: PowerShell or Command Prompt. Mac users: Terminal or Console.) 

3. Confirm that you have python installed.
- Windows and Mac users should type the following in the command-line environment: python --version
  
  (The CLI is the screen that pops up when you open a command-line environment.)
  - If a version appears in the output, you have python (e.g., Python 3.13.14) and can proceed to the "Install pygame" step below. 
  - If a version does not appear in the output, you need to install python.

4. Install Python
  - Windows PowerShell & Command Prompt: winget install Python.Python.3
  - Mac Terminal:
    - Install Xcode Command Line Tools: xcode-select --install
    - Install Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    - Install python: brew install python
  - Mac Console:
    - Install Homebrew (if you don't have it): /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    - Install python: brew install python

5. Verify Installation
  - Windows & Mac: python --version
    - If a version appears in the output, you have python (e.g., Python 3.13.14) and can proceed to the "Navigate to the Directory" step below.
    - If not, you did not successfully install python and will need to try again.

6. Confirm that Pip is installed.
  - Windows PowerShell: pip --version
  - Windows Command Prompt: python -m pip --version
  - Mac Terminal: pip3 --version
  - Mac Console: python3 -m pip --version
  
   If a version appears in the output, you have pip (i.e., python's package manager) and can proceed to the "Confirm that Pygame is Installed" step below. 
   If not, you did not successfully install pip and will need to try again. 
   
7. Install Pip
  - Windows PowerShell:
    - python -m ensurepip --default-pip
    - python -m pip install --upgrade pip
  - Windows Command Prompt:
    - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    - python get-pip.py
  - Mac Terminal & Console:
    - python3 -m ensurepip --upgrade

8. Confirm that Pygame is Installed.
  - Windows PowerShell & Command Prompt: python -m ensurepip --upgrade
  - Mac Terminal & Console: python3 -m ensurepip --upgrade
    
9. Install pygame
   - Windows PowerShell & Command Prompt: pip install pygame
   - Mac Terminal: python3 -m pip install pygame
   - Mac Console: pip3 install pygame

10. Navigate to the Directory
    
If you saved the file on your desktop, you can use one of the following commands: 
- Windows PowerShell: cd ~\Desktop\asteroids-main
- Windows Command Prompt: cd /d %userprofile%\Desktop\asteroids-main
 - Mac Terminal & Console: cd ~/Desktop/asteroids-main
 
12. Launch the game: <python_version> main.py

For example: python3 main.py

## How to Play
- Use the space bar to fire.
- Use the W, A, S, and D keys to move.
    w: go down
    a: turn right
    s: go up
    d: turn left

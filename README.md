# Moveocado: Telepathically Play Tetris
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white)

Have you ever wished you can type and play games without using your clunky keyboard? Introducing Moveocado, a program that allows you to play the game Tetris, just by moving your hands around and using different gestures. 

## Controls
After running the program, simply open up a game of tetris (that uses the arrows as input), and use the following controls:  
**Moving Left**: Touch the tip of your index finger to the left side of the screen  
**Moving Right**: Touch the tip of your index finger to the right side of the screen  
**Rotate Block**: Make a thumbs up gesture  
**Fast Drop**: Make a thumbs down gesture

## System Requirements

Before getting started, ensure you have the following installed on your system:

- **Pip**: Package management system
- **Pyenv**: Python version management

## Getting Started
### 1. Clone the repository
```bash
git clone <repository-url> <your-repo-name>
cd <your-repo-name>
```
### 2. Set up the virtual environment
First, set the local Python version to 3.9.13.
```bash
pyenv local 3.9.13
```
To double check that the local version is 3.9.13, run:
```bash
pyenv local # should be 3.9.13
```
Create the virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
### 3. Run the program
Simply run `main.py` in an editor of your choice or run:
```bash
python main.py
```
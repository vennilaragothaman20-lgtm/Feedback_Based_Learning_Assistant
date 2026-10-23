Feedback Learning Assistant
1. About the Project
This is a simple Python project that improves future responses using feedback from the user.
2. How It Works
1. The user enters a request.
2. The assistant gives a response.
3. The user says whether the response was useful.
4. If the response was not useful, the user enters a better response.
5. The project saves the better response and reuses it when the same request is entered again.
3. Technologies Used
- Python
- JSON file for saving responses
4. Requirements
- Python installed on your computer
- Visual Studio Code (VS Code)
No extra Python packages are required.
5. How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run this command:
   python main.py
4. Enter a request when prompted.
5. Give feedback by typing yes or no.
6. If you type no, enter a better response.
6. Files Created
- main.py — contains the Python program.
- feedback.json — stores improved responses. This file is created automatically when you save an improvement.
7. Example
First run:
- Request: how to learn python
- Assistant response: Start with the basics and practice every day.
- Feedback: no
- Better response: Learn variables, loops, functions, and practice small programs daily.
Next time you enter the same request, the assistant shows the saved improved response.
8. Important Note
This is a beginner project. It does not train an AI model automatically. It saves user-provided improvements and reuses them for the same request.
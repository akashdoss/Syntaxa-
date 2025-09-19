Syntaxia 2.0 - Your Smart Coding Assistant
Syntaxia is a sleek, modern web application designed to be your intelligent coding partner. Powered by Google's Gemini API, it helps developers understand, debug, and improve their code with ease. Just paste your code snippet, and Syntaxia will provide detailed explanations or suggest fixes for potential bugs.

✨ Features
Intelligent Code Analysis: Leverages the advanced capabilities of the Gemini API for high-quality code insights.

Code Explanation: Get detailed, line-by-line explanations of complex code snippets to understand their functionality.

Bug Detection & Fixing: Automatically identify potential bugs, logical errors, or anti-patterns and receive corrected code suggestions.

Polished User Interface: A premium, dark-themed UI with a dynamic, animated background for an enjoyable user experience.

Syntax Highlighting: Code snippets in the output are beautifully highlighted for maximum readability.

One-Click Copy: Easily copy corrected code snippets to your clipboard with a convenient button.

Secure API Key Handling: Your API key is handled securely on the server-side and is never exposed to the client.

🛠️ Tech Stack
Backend: Flask (Python)

Frontend: HTML5, CSS3, JavaScript

AI Model: Google Gemini 1.5 Flash

UI Libraries:

Marked.js for Markdown rendering.

Highlight.js for syntax highlighting.

🚀 Getting Started
Follow these instructions to get a local copy of Syntaxia up and running on your machine.

Prerequisites
Python 3.7 or higher

A Google Gemini API Key. You can obtain one from Google AI Studio.

Installation & Setup
Clone the repository:

git clone [https://github.com/your-username/syntaxia.git](https://github.com/your-username/syntaxia.git)
cd syntaxia

Create a Python virtual environment (recommended):

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required dependencies:
Create a file named requirements.txt and add the following lines:

Flask
google-generativeai

Then, run the installation command:

pip install -r requirements.txt

Run the application:

python app.py

Access Syntaxia:
Open your web browser and navigate to http://127.0.0.1:8080.

kullanım
When you first open the application, you'll be greeted by the welcome screen. Click "Get Started".

You will be prompted to enter your Google Gemini API Key. Paste your key and click "Save & Continue". The app will validate your key.

Once the key is validated, you can paste your code into the text area.

Click "Explain Code" to get a detailed breakdown of what the code does.

Click "Find & Fix Bugs" to have the AI identify errors and provide a corrected version.

Use the Copy button on any code block in the output to copy it to your clipboard.

📂 Project Structure
.
├── app.py             # The Flask backend server
└── templates/
    └── index.html     # The single-page HTML file for the entire frontend

✍️ Author
This project was created and designed by Akash Doss.

LinkedIn: https://www.linkedin.com/in/akash-selvadoss-n-542765252/

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

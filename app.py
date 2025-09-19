from flask import Flask, render_template, request, session, jsonify
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/set_api_key", methods=["POST"])
def set_api_key():
    api_key = request.json.get("api_key")
    if not api_key:
        return jsonify({"success": False, "error": "API Key required"})

    try:
        genai.configure(api_key=api_key)
        # Use a lightweight model for a quick verification check.
        model = genai.GenerativeModel("gemini-1.5-flash")
        # Generate a simple content to validate the key.
        _ = model.generate_content("Hello")
        session["api_key"] = api_key
        return jsonify({"success": True})
    except Exception as e:
        # Provide a more user-friendly error message.
        return jsonify({"success": False, "error": f"API Key validation failed: {e}"})


@app.route("/analyze_code", methods=["POST"])
def analyze_code():
    if "api_key" not in session:
        return jsonify({"error": "API key not set. Please refresh and enter your key."}), 403

    user_code = request.json.get("code")
    task = request.json.get("task")

    if not user_code or not task:
        return jsonify({"error": "Missing code or task."}), 400

    genai.configure(api_key=session["api_key"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        # Create more descriptive prompts for better results.
        if task == "explain":
            prompt = f"You are an expert code explainer. Break down the following code, explaining its purpose, logic, and key components in a clear and concise way for a developer.\n\nCode:\n```\n{user_code}\n```"
        elif task == "fix":
            prompt = f"You are an expert code debugger. Analyze the following code for bugs, errors, or inefficiencies. Provide a corrected version of the code and a brief explanation of the fixes you made.\n\nCode:\n```\n{user_code}\n```"
        else:
            return jsonify({"error": "Invalid task specified."}), 400

        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": f"An error occurred while analyzing the code: {e}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

from flask import Flask, request, jsonify, render_template
import language_tool_python

# Initialize Flask app
app = Flask(__name__)

# Initialize LanguageTool for grammar correction
tool = language_tool_python.LanguageTool('en-US', remote_server='https://api.languagetoolplus.com/v2')


@app.route("/")
def index():
    """Serve the frontend HTML page"""
    return render_template("index.html")

@app.route("/api/correct-grammar", methods=["POST"])
def correct_grammar():
    """Receive text, correct grammar, return JSON"""
    try:
        data = request.get_json()
        text = data.get("text", "")
        corrected = tool.correct(text)
        return jsonify({"correctedText": corrected})
    except Exception as e:
        return jsonify({"correctedText": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

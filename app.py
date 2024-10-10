from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Function to compile/execute code based on the language
def execute_code(language, code):
    if language == "python":
        return execute_python(code)
    elif language == "javascript":
        return execute_javascript(code)
    else:
        return "Unsupported language", 400

# Execute Python code
def execute_python(code):
    try:
        # Run the Python code and capture the output
        result = subprocess.run(
            ['python', '-c', code], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

# Execute JavaScript code (requires Node.js installed in the container)
def execute_javascript(code):
    try:
        # Run the JavaScript code using Node.js and capture the output
        result = subprocess.run(
            ['node', '-e', code], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

# Create an endpoint that takes code and language via POST requests
@app.route('/compile', methods=['POST'])
def compile():
    data = request.get_json()

    if 'code' not in data or 'language' not in data:
        return jsonify({'error': 'Please provide both code and language'}), 400

    code = data['code']
    language = data['language']

    # Compile or execute the code
    output = execute_code(language, code)
    return jsonify({'output': output}), 200


if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        return f"<h2>Hello {name}, welcome! </h2>"
    
    # Show input form
    return """
        <h2>Enter your name</h2>
        <form method="POST">
            <input type="text" name="name" placeholder="Your name" required>
            <button type="submit">Submit</button>
        </form>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5000)
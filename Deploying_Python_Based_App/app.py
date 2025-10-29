from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html>
  <head>
    <title>Docker Flask App</title>
  </head>
  <body>
    <h2>Simple Frontend Running Inside Docker</h2>
    <form method="POST">
      <label>Enter your name:</label>
      <input type="text" name="username" required>
      <input type="submit" value="Submit">
    </form>
    {% if name %}
      <h3>Hello, {{ name }}!</h3>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(HTML_PAGE, name=name)

if __name__ == "__main__":
    # Bind to 0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=5000)


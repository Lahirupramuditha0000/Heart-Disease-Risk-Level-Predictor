from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # Endpoint created
def home():
    return "Home page"

@app.route('/page2')
def page2():
    return "Page 02"

@app.route('/page3')
def page3():
    return render_template("test.html")  # ✅ Return the rendered HTML

if __name__ == '__main__':
    app.run(debug=True)  # Run the app

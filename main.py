from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<name')
def profile(name): 
    return render_template("profile.html", ) # don't put html in the return statement


if __name__ == "__main__":
    app.run(debug=True) # tells it to start the server
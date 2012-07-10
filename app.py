import os
from flask import Flask, request, render_template

#------------------------
# app configuration
#------------------------

app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

#------------------------
# helper functions
#------------------------

def helper_function():
	pass

#------------------------
# controllers and routes
#------------------------

@app.route("/")
def index():
    return render_template("index.html")

#------------------------
# app launch
#------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

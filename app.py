# Importing Flask
from flask import Flask, render_template
from django.shortcuts import render

# Creating an instance of the Flask class
app = Flask(__name__)

# Creating a new endpoint with this instance as a function decorator
@app.route('/')
def hello_world():
    return render_template("index")

# Starting the Server
if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'super secret key'
@app.route('/')
def index():
    data="sarthak"
    return render_template('index.html',data=data)
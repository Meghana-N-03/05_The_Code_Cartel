from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')
 
# main driver function
if __name__ == '__main__':
    app.run(debug=True)
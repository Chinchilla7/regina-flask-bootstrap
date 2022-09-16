from flask import Flask, render_template

app = Flask(__name__)

#creating and styling homepage using bootstrap
@app.route('/')
def home_page():
    return render_template('homepage.html')

#creating and styling contact page using bootstrap

@app.route('/contactus')
def contact_page():
    return render_template('contactpage.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
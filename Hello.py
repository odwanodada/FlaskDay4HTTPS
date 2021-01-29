from flask import Flask,render_template,url_for,request
app = Flask(__name__)

@app.route('/Login',methods=['GET','POST'])
def hello():
    type_of_request = request.method
    return render_template('Hello.html', request_method = type_of_request)

@app.route('/contact/')
def contact_us():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
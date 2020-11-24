from flask import Flask, render_template , redirect,url_for,request
import csv
app = Flask(__name__)

@app.route('/')
def home1():
    return render_template('index.html')


@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data.get('email')
        subject=data.get('subject')
        message=data.get('message')
        file=database.write(f"\nYou have Email from {email} regarding {subject} and here is the message{message}\n------------------------------")
       
def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email=data.get('email')
        subject=data.get('subject')
        message=data.get('message')
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
       
        
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Oppps!!! Something went wrong try agin or get connect with social apps'
    else:
        return 'Form not submitted'
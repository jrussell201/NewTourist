from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/question',methods= ['GET','POST'])
def question():
    if request.method == "GET":
        return "Use the form"
    else:
        city = request.form['city']
        #print (city)
        date = request.form['date']
        #print (date)
        #print (model.concerts)
        concerts=model.concerts[city]
        # if(city == 'New York":
        
        #     return 
        # else:
        return render_template("concerts.html",concerts=concerts)
        #return ("debugging")
        
@app.route('/location')
def location():
    return render_template("location.html")

    
    
    
from flask import Flask, render_template, request
import pickle
import pandas as pd




app=Flask(__name__, template_folder='templates')
#load the model
model=pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result=''
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Hour=(float(request.form['Hour (0 - 23)']))
    
    Month=(float(request.form['Month (1 - 12)']))

    cab_type=request.form['cab_type']
    
    
    if cab_type=="uber":
        cab_type=1

    
    else:
        cab_type=0
    
    cab=float(cab_type)

    service=float(request.form['service_class'])

    tmprain=request.form['Weather']

    if tmprain=='rain': 
        tmprain=1
    else:
        tmprain=0
    rain=float(tmprain)

    day=float(request.form['day'])

    dist=float(request.form['Distance'])

    surge=float(request.form['Surge Multiplier'])

    tmppeak=request.form['Peak Time']

    if tmppeak=='Yes': 
        tmppeak=1
    else: 
        tmppeak=0
    
    peak=float(tmppeak)
    


    
    result=model.predict([[Hour, Month, cab, dist,  surge, rain, service, day,  peak]])
    return render_template('index.html', Price= f'The Total Cab Price is ${round(result[0],2)}')



if __name__=="__main__":
    app.run(debug=True)

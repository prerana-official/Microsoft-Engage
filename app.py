from pickle import TRUE
import flask
from flask import Flask,redirect, request,url_for,render_template


#


app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index1.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    year=int(request.args.get('year'))
    from prediction import dataPreprocess
    obj1=dataPreprocess()
    df,result=obj1.input(year)
    print(df)
    print(result)
    return render_template('outputpage.html',dataf=df, result=result,year=year)

if __name__=='__main__':
    app.run(debug=TRUE)

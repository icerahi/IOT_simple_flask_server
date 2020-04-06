from flask import Flask,render_template,request,redirect
from gpiozero import LED
from datetime import datetime


led=LED(18)
fan=LED(21)

app=Flask(__name__)


 
@app.route('/')
def index():
    
    return render_template('index.html',led=led,fan=fan)

@app.route('/light_on')
def light_on():
    led.on()
    return redirect("/")

@app.route('/light_off')
def light_off():
    led.off()
    
    return redirect("/")

@app.route('/fan_off')
def fan_off():
    fan.on()
    return redirect("/")
    
@app.route('/fan_on')
def fan_on():
    fan.off()
    return redirect("/")


if __name__=='__main__':
    app.run(debug=True,port=80,host='0.0.0.0')

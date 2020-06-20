from flask import Flask,render_template,request,redirect
from gpiozero import LED
import requests
from Adafruit_IO import MQTTClient
import os
from flask_cors import cross_origin
import urllib.request

led=LED(18)

app=Flask(__name__)
@app.route('/')
@cross_origin()
def index():
    
    return render_template('index.html',led=led)

@app.route('/light_on')
@cross_origin()
def light_on():
    led.off()
    return redirect("/")

@app.route('/light_off')
@cross_origin()
def light_off():
    led.on()
    
    return redirect("/")


"""ADAFRUIT_IO_KEY = 'aio_vIqm07WiwXqcPV0PYvT4I34MW7rO'
ADAFRUIT_IO_USERNAME = 'icerahi'

def connected(client):
    print("Connected, Listening changes....")
    client.subscribe("light")

def disconnected(client):
    print('Disconnected....')
    sys.exit(1)

def message(client, feed_id, status):
    if feed_id == 'light':
    
        if status == "on":
            print("Light On")
            requests.get('http://localhost/light_on')

         
        else:
            print("light Off")
            requests.get('http://localhost/light_off')
          

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect       =   connected
client.on_disconnect    =   disconnected
client.on_message       =   message
client.connect()


client.loop_background()

"""

if __name__=='__main__':
    app.run(debug=True,port=80,host='0.0.0.0')

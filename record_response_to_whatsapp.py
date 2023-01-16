from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from configure import twilio_auth_key, acct_id

app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():
    """Read a message aloud"""
    resp = VoiceResponse()
    resp.say("Hi Chris, record your message after the beep and then hang up")
    resp.record(timeout=10, transcribe=True)
    resp.hangup()
    return(str(resp))

if __name__ == "__main__":
    app.run(debug=True)

    


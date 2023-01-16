from twilio.rest import Client
from configure import twilio_auth_key, acct_id, phoneNumberOrGroup
import pywhatkit as pwk
from time import sleep

firstTime=True
lastcount=0

client = Client(acct_id, twilio_auth_key)

while True:

    transcriptions = client.transcriptions.list()

    if firstTime:
        lastcount=len(transcriptions)
        print("First time setup, number of old messages = " + str(lastcount))
        firstTime=False

    if firstTime==False:
        if lastcount < len(transcriptions):
            print("Message number has increased so transcribing and sending")
            print("Waiting 10 seconds to allow the recording to be processed")
            sleep(10)
            print("ready ... lets transcribe")
            _tid = transcriptions[0].sid
            transcript = client.transcriptions(_tid).fetch()
            message = str(transcript.transcription_text)
            print("Message was: " + message)
            try:
                pwk.sendwhatmsg_instantly(phoneNumberOrGroup,  message)
                print("Message sent")
            except:
                print("Error sending message")

            lastcount = len(transcriptions)
            print("Updated number of known messages to " + str(lastcount))






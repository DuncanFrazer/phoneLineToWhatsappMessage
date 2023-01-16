# phoneLineToWhatsappMessage

This app works with a Twilio account to allow a regular land line phone number to be called, a message recorded, and that message is sent as a whatsapp message
The original intention is for an elderly relative to be able to leave messages for family members so that the family can call back instead of receiving as-I-think-of-it calls throughout the day

Whatsapp messages are sent via pywhatkit - pywhatkit requires you to be signed in to whatsapp web in a browser on the machine that is running these python scripts with an account that can reach the contact number or group to be messaged

The python scripts require a few personal details that you'll need to add to configure.py, rename the sample_configure.py and add your details

The code is based on an write-up that I found from assemblyai ... although I've stuck with Twilio's transcription service and not invoked AssemblyAI's transcription method at this time
https://www.assemblyai.com/blog/how-to-build-a-burner-phone-with-voicemail-in-python

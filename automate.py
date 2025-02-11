import pywhatkit as kit
import time

# Selected interns' WhatsApp numbers (Format: "+CountryCodePhoneNumber")
selected_numbers = ["+919837408849","+917678673442"]  # Replace with actual numbers

# Message content
message_body = """🎉 Congratulations! 🎉

You have been selected for the next round of the Cropsky internship. 🚀

Join our WhatsApp group for further updates: https://chat.whatsapp.com/HB3vBPt4EsB30G76TjDV10

Best,  
Cropsky Team
"""

# Send message to each intern
for number in selected_numbers:
    kit.sendwhatmsg_instantly(number, message_body)  # Instantly sends the message
    print(f"✅ WhatsApp message sent to {number}")
    time.sleep(5)  # Prevents sending too fast

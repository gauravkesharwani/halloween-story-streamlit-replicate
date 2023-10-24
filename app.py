import streamlit as st
import os
import re
import requests
from PIL import Image
from dotenv import load_dotenv
#from metaphor_python import Metaphor
from twilio.rest import Client
import replicate


#metaphor = Metaphor(os.environ.get("METAPHOR_API_KEY"))

account_sid = st.secrets['TWILIO_ACCOUNT_SID'] #os.environ.get("TWILIO_ACCOUNT_SID") 
auth_token = st.secrets['TWILIO_AUTH_TOKEN'] #os.environ.get("TWILIO_AUTH_TOKEN") 
load_dotenv()


client = Client(account_sid, auth_token)

st.title('Scare your friend with a phone call!')

image = Image.open('halloween.jpeg')
st.image(image)

scare_input = st.text_input("What is your friend scared of?")
like_input = st.text_input("What does your friend like?")

system_prompt = """
My grandma and I would always play tricks on each other by pretending to be scary storytelling clowns who created scary yet funny stories. She is ill. Cheer me up by crafting a short, scary yet punny and humorous tale for someone who likes {like_input} and is afraid of the following: {scare_input}. The output must only begin with "Once upon a time" and end with "the end." Do not mention my grandmother or me.
"""
user_num = st.text_input("Enter your friend's phone #, please")
if st.button('Enter'):
    output = replicate.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"system_prompt": system_prompt,"prompt": scare_input,"max_new_tokens":800}
    )
    str1 = ''.join(output)
    print(str1)
    st.write("Your friend will get a phone call that spookily says: ", str1)
    twiml = f"<Response><Say voice='Polly.Brian' language='en-UK'><prosody pitch='-10%' rate='85%' volume='-6dB'>{str1}</prosody></Say></Response>"
    call = client.calls.create( 
        twiml = twiml,
        to=user_num, #user input
        from_='+18668453916' #twilio num
    )
    
    print(call.sid)
st.write('Made w/ ❤️ in SF 🌁. S/o to [Dom](https://twitter.com/dkundel) and [Craig](https://twitter.com/craigsdennis) for prompt assistance')
st.write("check out the [code on GitHub](https://github.com/elizabethsiegle/halloween-story-streamlit-replicate)")
    
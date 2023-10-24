### Happy Halloween! Make a scary phone call with AI (llama-2-70b-chat)
[Try out the web app here](https://ai-halloween-story-phone-call.streamlit.app/)

![Web app screenshot](image.png)

- [get your Twilio credentials here and a phone number here](https://twilio.com/try-twilio)
- [make a Replicate account here](https://replicate.com/)
- [make a Streamlit account here](https://streamlit.io/)
Clone the repo, install the dependencies by running `pip install -r requirements.txt`, and make a .env file with your credentials. To run the app locally, replace the lines containing `st.secret` with the commented out versions using `os.environ.get`...

If you deploy to Streamlit, you'll need to add your secret credentials to your deployed project.
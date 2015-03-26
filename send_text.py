from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "YOUR_ACCT_ID"
auth_token  = YOUR_AUTH_TOKEN"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body="dickface",
    to="+7777777777",    # Replace with your phone number
    from_="+9999999999") # Replace with your Twilio number
print message.sid
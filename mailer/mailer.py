import requests

class Mailer:
    def __init__(self):
      pass

    def send_message(self, name, email, subject, comment):

      message_text = "Name: " + name + "\n" + "Email: " + email + "\n" + \
                     "Message:\n\n" + comment
      return requests.post(
        "https://api.mailgun.net/v3/sandbox6cbe982fa9b64efe8110a44cad8f25a7.mailgun.org/messages",
        auth=("api", "key-d31ba89312af933035576be061244371"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox6cbe982fa9b64efe8110a44cad8f25a7.mailgun.org>",
              "to": "Collin Price <collinprice@college.harvard.edu>",
              "subject": subject,
              "text":  message_text})

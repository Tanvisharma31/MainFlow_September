import razorpay
from datetime import datetime
from .settings import KEY_ID,  KEY_SECRET

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

def order(username, email, fname, lname, amount_rs, currency='INR'):
    amount = int(amount_rs) * 100
    id = username + "@" + str(datetime.now()).split(".")[0].replace(":", "").replace("-", "").replace(" ", "")
    notes = {"email" : email, "name" : f"{fname} {lname}"}

    data = { "amount": amount, "currency": currency, "receipt": id, "notes" : notes }
    order = client.order.create(data=data)

    return order

def verify_payment_request(data):   
    client.utility.verify_payment_signature(data)

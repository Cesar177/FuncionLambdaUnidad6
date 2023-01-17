import json
import os
import mercadopago

def lambda_handler(event, context):

    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    bodyGet = json.loads(event["body"])
    
    # TODO implement
    payment_data = {
        "transaction_amount": float(bodyGet["transaction_amount"]),
        "token": bodyGet["token"],
        "installments": int(bodyGet["installments"]),
        "issuer_id": bodyGet["issuer_id"],
        "payment_method_id": bodyGet["payment_method_id"],
        "payer": {
            "email": bodyGet["payer"]["email"],
            "identification": {
                "type": bodyGet["payer"]["identification"]["type"],
                "number": bodyGet["payer"]["identification"]["number"]
            },
        },
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    
    return {
        "statusCode": 200,
        "body": json.dumps(payment)
    }
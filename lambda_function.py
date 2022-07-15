import json
import stocks

import random
random.randint(1, 100)



#= stocks.function(5)

#print(y)

def lambda_handler(event, context):
    """
    Everything begins here!
    """
    inputted_symbol = input("type ticker symbol here")

    # they get SQL first
    stocks_SQl = stocks.create_sql(inputted_symbol)

    # ok, they are using an API to get stocks
    stocks_dictionary = stocks.API(stocks_SQl)

    email_text = stocks.generate_email_text(stocks_dictionary)

    stocks.send_email(email_text)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

lambda_handler(None, None)


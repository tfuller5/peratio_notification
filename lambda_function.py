import json
import stocks

import random
random.randint(1, 100)

def lambda_handler(event, context):
    """
    Everything begins here!
    """
    inputted_symbol = input("type ticker symbol here")

    # they get SQL first
    stocks_SQl = stocks.create_sql(inputted_symbol)
    # print(stocks_SQl)

    # ok, they are using an API to get stocks
    stocks_dictionary = stocks.API(stocks_SQl)
    # print(stocks_dictionary)

    stock_info = stocks.generate_email_text(stocks_dictionary)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

lambda_handler(None, None)
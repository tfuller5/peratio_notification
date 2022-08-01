import json
import stocks

# program with 130 lines
# something is going wrong
# what do you do?


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

    #print(email_text)
    stocks.send_email(email_text)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

lambda_handler(None, None)


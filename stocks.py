# expecting
# AUTHORIZATION: account
# WHERE: link to the site
# WHAT: details of which stocks and what info we want
# python: other python stuff which needs to be done

# use functions
# setup git
# use aws

# functions?
# * function to create the sql
# * function which

# what is simplest thing we can do first?
# chris's email
# recipient email: school email
# create a function
# send an empty email

import http.client
import json


def API(sql):
    """
    This function connects to the sql database and retrieves the stocks data.


    :param sql:
    :return: a data dictionary
    """
    conn = http.client.HTTPSConnection("hotstoks-sql-finance.p.rapidapi.com")

    headers = {
        'content-type': "text/plain",
        'X-RapidAPI-Host': "hotstoks-sql-finance.p.rapidapi.com",
        'X-RapidAPI-Key': "f3e259d6damshb4ef9605aa104b4p1efaccjsne0bcdc9b3c67"
    }

    # python: get data from website
    conn.request("POST", "/query", sql, headers)
    res = conn.getresponse()

    # reading
    data = res.read()
    # decoding
    data = data.decode("utf-8")
    # convert to dictionary
    data = json.loads(data)

    return data


def create_sql(symbol):
    '''
    This function this function takes a stock ticker symbol, inserts it in SQL and returns the text.

    :param symbol: stock ticker (ex. AMZN, AAPL)
    :return: it returns the sql data
    '''

    print(f"""You have selected {symbol}""")

    sql_string = """
    SELECT name, price, pe_ratio
    FROM stocks
    WHERE symbol = '""" + symbol + """'
    ORDER BY price DESC
    """

    return sql_string


def generate_email_text(stock_data):
    """
    creates a user friendly string representing the content of an email given input a dictionary (not user friendly)

    :param stock_data:
    :return:
    """
    # strategy: use print to get more info
    #print(stock_data)
    results = stock_data["results"]
    firststock = results[0]
    peratio = firststock["pe_ratio"]
    price = firststock["price"]
    price = (float(price))

    name = firststock["name"]

    print(peratio)
    print(name)
    print(price)


import smtplib
from email.mime.text import MIMEText

def send_email(x):
    email_template = MIMEText("Hello")
    print(type(email_template))

    me = "tom80f@outlook.com"
    you = "w1826354@my.westminster.ac.uk"
    password = ""

    email_template["From"] = me
    email_template["To"] = you
    email_template["Subject"] = "hello there" + str(x * 1000)
    print("SENDING EMAIL")

    s = smtplib.SMTP('outlook.office365.com')
    s.ehlo()
    s.starttls()
    s.login(me, password)
    s.sendmail(me, [you], email_template.as_string())
    s.quit()

for x in range(100):
    test1 = send_email(x)


"""
print("start debugger")

inputted_symbol = input("type ticker symbol here")

print("before call")
# they get SQL first
stocks_SQl = create_sql(inputted_symbol)
#print(stocks_SQl)

# ok, they are using an API to get stocks
stocks_dictionary = API(stocks_SQl)
#print(stocks_dictionary)

stock_info = generate_email_text(stocks_dictionary)
"""


f"""
Hello investor, 
You have selected the x stock and you set an alert for when it will reach x pe ratio. 
The actual price of {5} stocs is y, pe ratio is h.
"""

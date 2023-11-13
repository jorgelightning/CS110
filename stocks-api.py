from flask import Flask
from flask import request
import requests

app = Flask(__name__)
app.debug = True

#given code to grab responses from stock API through symbol input
def getStock(symbol):
    baseURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=csv'
    keyPart = '&apikey=' + "FF08QG0OG9019Q4C" #Add API key
    symbolPart = '&symbol=' + symbol
    stockResponse = requests.get(baseURL+keyPart+symbolPart)
    return stockResponse.text  #Return only text part of response


#created a checkbox and input for text and assigned variables for 
#them to access later 
#I used triple " so I don't need to use html += so many times and easy to edit html code
@app.route('/')
def form_example():
    html = """
    <html>
    <title>D:</title>
    <body bgcolor="lightgrey">
    <form method="POST" action="results">
    <h2>Stock symbols: <input type="text" name="userInput" /></h2>
    <input type="checkbox" id="option1" name="option1" value="open">
    <label for="option1">Opening Price</label><br>
    <input type="checkbox" id="option2" name="option2" value="high">
    <label for="option2">High</label><br>
    <input type="checkbox" id="option3" name="option3" value="low">
    <label for="option3">Low</label><br>
    <input type="checkbox" id="option4" name="option4" value="price">
    <label for="option4">Current Price</label><br><br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    """ 
    return html
  

#using the variable assigned I would used to add symbol into getStock()
#the option# are used if true would show in the result page 
#error checking is used when the response is empty {}
@app.route('/results', methods=['POST'])
def form_input():
    userInput = request.form['userInput']
    option1 = str(request.form.getlist('option1'))
    option2 = str(request.form.getlist('option2'))
    option3 = str(request.form.getlist('option3'))
    option4 = str(request.form.getlist('option4'))
    userInput = userInput.upper()
    stockString = getStock(userInput)
    html = ''
    html += '<html>'    
    html += '<title>;)</title>'
    html += '<body bgcolor="lightgrey">'
    if stockString != '{}':
        stockList = stockString.split(',')
        html += '<h2> The value for ' + userInput + ' is as follows: </h2>'
        if option1 == '[\'open\']':
            html += '<p>Opening Price: ' + stockList[10] + '</p>'
        if option2 == '[\'high\']':
            html += '<p>High: ' + stockList[11] + '</p>'
        if option3 == '[\'low\']':
            html += '<p>Low: ' + stockList[12] + '</p>'
        if option4 == '[\'price\']':
            html += '<p>Current Price: ' + stockList[13] + '</p>'
    else:
        html += '<p> ERROR! PLEASE ENTER VALID SYMBOL! </p>'
    html += '<a href="/">Back</a>'
    html += '</body>'
    html += '</html>'
    return html

if __name__ == '__main__':
  app.run()

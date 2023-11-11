from flask import Flask
from flask import request
import requests

app = Flask(__name__)
app.debug = True


def getStock(symbol):
    baseURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=csv'
    keyPart = '&apikey=' + " " #Add API key
    symbolPart = '&symbol=' + symbol
    seriesType = '&series_type=' + 'high'
    stockResponse = requests.get(baseURL+keyPart+symbolPart+seriesType)
    return stockResponse.text  #Return only text part of response

stockString = getStock('ibm')
stockList = stockString.split(',')
    
@app.route('/')
def form_example():
    html = ''
    html += '<html>'
    html += '<title>D:</title>'
    html += '<body bgcolor="lightgrey">'
    html += '<form method="POST" action="results">'
    html += '<h2>Stock symbols: <input type="text" name="userInput" /></h2>'
    html += '<input type="checkbox" id="option1" name="option1" value="open">'
    html += '<label for="option1">Opening Price</label><br>'
    html += '<input type="checkbox" id="option2" name="option2" value="high">'
    html += '<label for="option2">High</label><br>'
    html += '<input type="checkbox" id="option3" name="option3" value="low">'
    html += '<label for="option3">Low</label><br>'
    html += '<input type="checkbox" id="option4" name="option4" value="price">'
    html += '<label for="option4">Current Price</label><br><br>'
    html += '<input type="submit" value="Submit">'
    html += '</form>'
    html += '</body>'
    html += '</html>'
    return html
  

  
@app.route('/results', methods=['POST'])
def form_input():
    userInput = request.form['userInput']
    option1 = str(request.form.getlist('option1'))
    option2 = str(request.form.getlist('option2'))
    option3 = str(request.form.getlist('option3'))
    option4 = str(request.form.getlist('option4'))
    userInput = userInput.upper()
    stock = getStock(userInput)
    html = ''
    html += '<html>'
    html += '<title>;)</title>'
    html += '<body bgcolor="lightgrey">'
    html += '<h2> The value for ' + userInput + ' is as follows: </h2>'
    if option1 == '[\'open\']':
        html += '<p>Opening Price: ' + stockList[10] + '</p>'
    if option2 == '[\'high\']':
        html += '<p>High: ' + stockList[11] + '</p>'
    if option3 == '[\'low\']':
        html += '<p>Low: ' + stockList[12] + '</p>'
    if option4 == '[\'price\']':
        html += '<p>Current Price: ' + stockList[13] + '</p>'
    html += '<a href="/">Back</a>'
    html += '</body>'
    html += '</html>'
    return html
  
  

if __name__ == '__main__':
  app.run()
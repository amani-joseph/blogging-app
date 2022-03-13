import urllib.request, json
from .models import Quote

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quote():
    get_quote_url = base_url.format()

    with urllib.request.urlopen(get_quote_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        quote_object = None
        if quote_details_response:
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')

            quote_object = Quote(author,quote)
            print(quote_object)
          
    return quote_object
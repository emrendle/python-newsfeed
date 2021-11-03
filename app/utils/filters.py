# expects to receive a datetime object the converts it to a string 
def format_date(date):
  return date.strftime('%m/%d/%y')

# removes all excess info from the url string leaving only the domain name
# .replace and .split behave the same as js
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word
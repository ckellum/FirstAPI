import requests
import send_email

api_key = "aabc15d1f45947e48b87a2091ff29be5"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-01-21&sortBy=publishedAt&apiKey" \
      "=aabc15d1f45947e48b87a2091ff29be5 "

# make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()

# access the article titles and description
message = ""
for article in content["articles"]:
    message = message + article["title"] + "\n" + article["description"] + 2*"\n"

message = message.encode("utf-8")
send_email.send_email(message)

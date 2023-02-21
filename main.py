import requests
import send_email

topic = input("what would you like to view?")
api_key = "aabc15d1f45947e48b87a2091ff29be5"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-21&" \
      "sortBy=publishedAt&" \
      "apiKey=aabc15d1f45947e48b87a2091ff29be5&" \
      "language=en"

# make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()

# access the article titles and description
message = "Subject:Here it is \n"
for article in content["articles"][0:20]:
    message = message + article["title"] + "\n" + \
              article["description"] + "\n" + \
              article["url"] + 2*"\n"

message = message.encode("utf-8")
send_email.send_email(message)

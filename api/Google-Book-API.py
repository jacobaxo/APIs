import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
query = input('what book would you like to look up ')

params = {"q": query, "maxResults": 3}
response = requests.get(endpoint, params=params).json()
for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume["title"]
    published = volume["publishedDate"]
    description = volume["description"]
    print(f"{title} ({published}) | {description}") 
text = "text.txt" # very orginal name
file = open(text, "w")
wr = file.write(f"{title} | {published} | {description}")
file.close()

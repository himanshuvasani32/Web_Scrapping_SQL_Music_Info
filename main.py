import requests
import selectorlib
import smtplib, ssl
import os

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """This function will extract the source from the given URL."""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    """This function will extract the value we want to extract from the source."""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    sender = "himanshuvasani33@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "innovistainfotech@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
    print("Email was sent!")


def store(extracted):
    """This function will add the new value to the data.txt file."""
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read(extracted):
    """This function will read the data.txt file."""
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_mail(message="Hey! there is new music event coming soon.")

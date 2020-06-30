from bs4 import BeautifulSoup


def html_parser(file):
    soup = BeautifulSoup(file, 'html.parser')
    strongs = soup.select('strong')
    mailtos = soup.select('a[href^=mailto]')

    emails = []

    div = soup.select('td')
    phone = soup.select('a[href^=tel]')
    phone_number = []
    for i in phone:
        x = i.string
        phone_number.append(x)

    for i in mailtos:
        if i.string != None:
            emails.append(i.string.encode('utf-8').strip())

    result = []
    names = []
    for i in strongs:
        for j in i:
            result.append(j.string)

    for i in result:
        if result.index(i) % 2 != 0:
            if i.string != None:
                if i != '\n':
                    names.append(i.string.encode('utf-8').strip())
    data = {
        "name": result[1],
        "email": emails[1].decode(),
        "phone": phone_number[0],
        "beds": result[5],
        "baths": result[6],
        "address": result[3]
    }
    return data


if __name__ == '__main__':
    file = open("src/New Lead .html", 'r')
    print(html_parser(file))

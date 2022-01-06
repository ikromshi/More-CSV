import urllib.request


def get_pictures():
    data = urllib.request.urlopen("https://xkcd.com/")
    lines = data.readlines()
    for i in range(len(lines)):
        line = lines[i].decode("utf-8")
        if '<div id="comic">' in line:
            image = lines[i+1].decode("utf-8")
            image = image.replace("//imgs.xkcd.com/", "https://imgs.xkcd.com/")
            return image


def main():
    link = get_pictures()
    print(link)


main()

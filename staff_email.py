import urllib.request


def scrape(url, name_dict):
    '''
    This function identifies names and corresponding netpass IDs and adds them to
    lists
    Args: a url,an empty dictionary to add name-netpass values
    Returns: none
    '''
    data = urllib.request.urlopen(url)
    lines = data.readlines()
    key = "<li><a href=\"https://faculty.ithaca.edu/"
    for line in lines:
        line = line.decode("utf-8")
        if key in line:
            mail_start = line.index("https")
            mail_end = line.index('">')

            name_start = line.index('">') + 2
            name_end = line.index("</a") - 1

            staff_name = line[name_start:name_end]
            staff_mail = line[mail_start:mail_end]

            name_dict[staff_name] = staff_mail


def print_logins(name_dict):
    '''
    Print all of the name and netpass information
    Args: a list of names, a list of netpass IDs
    Return: none
    '''
    # Print each name followed by it's netpass

    for names, mails in name_dict.items():
        print(f"{names} {mails}\n")


def write_info(name_dict):
    my_file = open("staff_email.txt", "w")
    for names, emails in name_dict.items():
        my_file.write(f"{names}: {emails}\n")
    my_file.close()



def main():
    '''
    Run the webscraping function and print results
    Args: none
    Return: none
    '''
    name_dict = dict()
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
    for letter in letters:
        scrape(f"https://www.ithaca.edu/directories/faculty_list.php?startwith={letter}", name_dict)
        # print_logins(name_dict)
        write_info(name_dict)

main()

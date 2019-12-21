def main():
    import urllib.request
    from bs4 import BeautifulSoup

    user_data = input('Enter Name or Email Address: ').replace(' ', '+')
    url = 'https://viewdns.info/reversewhois/?q='+user_data

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read().decode()

    page_soup = BeautifulSoup(webpage, 'html.parser')
    page_table = page_soup.find(face='Courier').find_all('tr')
    domain_data = [i.find_all('td') for i in page_table]

    data_format = []

    for data in  domain_data:
        domainName = data[0].get_text()
        createData = data[1].get_text()
        registant = data[2].get_text()
    
    data_format.append([domainName, createData, registant])

    width = sorted([len(i[0]) for i in data_format])[-1]

    for a in data_format:
        print('{:<{dom_width}}||{:<{date_width}}||{}'.format(a[0], a[1], a[2], dom_width=width+1, date_width=10+3))
    print("\033[51m"+"#########################################")
    restart = input("do you want to search again?(y/n)")
    if restart == "y":
        main()
    else:
        exit()
main()
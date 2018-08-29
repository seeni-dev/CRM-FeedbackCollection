import  Downloader as d

def testEncode():
    product=input("Enter prodcut name:")
    f=d.FlipkartDownloader(product) # encode will be caleed in here.
    print(f.link)
    print("")

def testgetHtml():
    product = input("Enter prodcut name:")
    f = d.FlipkartDownloader(product)  # encode will be caleed in here.
    content=d.getHtml(f.link)
    print(content)
    with open("temp.html","wb") as f:
        f.write(content)


if __name__ == '__main__':
    testgetHtml()

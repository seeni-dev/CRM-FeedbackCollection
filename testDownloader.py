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


def testLinkExtract():
    product = input("Enter prodcut name:")
    f = d.FlipkartDownloader(product)  # encode will be caleed in here.
    print(f.link)
    return


def testgetScore():
    product = input("Enter prodcut name:")
    f = d.FlipkartDownloader(product)  # encode will be caleed in here.
    f.getPage()
    score=f.getScore()
    print(score)

def testGetReviews():
    product = input("Enter product name:")
    f = d.FlipkartDownloader(product)  # encode will be caleed in here.
    f.getPage()
    print(f.getReviews())


if __name__ == '__main__':
    testGetReviews()

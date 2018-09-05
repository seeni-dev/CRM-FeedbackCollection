import  Downloader as d

class testFlipkartDownloader():
    def testEncode(self):
        product=input("Enter prodcut name:")
        f=d.FlipkartDownloader(product) # encode will be caleed in here.
        print(f.link)
        print("")

    def testgetHtml(self):
        product = input("Enter prodcut name:")
        f = d.FlipkartDownloader(product)  # encode will be caleed in here.
        content=d.getHtml(f.link)
        print(content)
        with open("temp.html","wb") as f:
            f.write(content)


    def testLinkExtract(self):
        product = input("Enter prodcut name:")
        f = d.FlipkartDownloader(product)  # encode will be caleed in here.
        print(f.link)
        return


    def testgetScore(self):
        product = input("Enter prodcut name:")
        f = d.FlipkartDownloader(product)  # encode will be caleed in here.
        f.getPage()
        score=f.getScore()
        print(score)

    def testGetReviews(self):
        product = input("Enter product name:")
        f = d.FlipkartDownloader(product)  # encode will be caleed in here.
        f.getPage()
        print(f.getReviews())

    def testOverall(self):
        product = input("Enter product name:")
        f = d.FlipkartDownloader(product)  # encode will be caleed in here.
        print("Process Initiated")
        f.process()
        print("Dump Complete")

class testAmazonDownloader():
    def testMakeLink(self):
        a=d.AmazonDownloader("Oneplus 6")
        print(a.link)
        return a.link

if __name__ == '__main__':
    tfd=testAmazonDownloader()
    link=tfd.testMakeLink()

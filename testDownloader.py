import  Downloader as d

def testEncode():
    product=input("Enter prodcut name:")
    f=d.FlipkartDownloader(product) # encode will be caleed in here.
    print(f.link)
    print("")
if __name__ == '__main__':
    testEncode()

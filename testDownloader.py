import  Downloader as d

def testEncode():
    product=input("Enter prodcut name")
    f=d.FlipkartDownloader(product)
    print(f.link)

if __name__ == '__main__':
    testEncode()

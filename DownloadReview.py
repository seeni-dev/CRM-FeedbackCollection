import Downloader as downloader

def FlipkartDownloader(product):
    dl=downloader.FlipkartDownloader(product,name="Flipkart")
    dl.process()
    return

def AmazonDownloader(product):
    dl=downloader.AmazonDownloader(product,name="Amazon")
    dl.process()
    return

def downloadReview(product):
    FlipkartDownloader(product)
    AmazonDownloader(product)
    return

def driver():
    product=input("Enter the product:")
    downloadReview(product)


if __name__ == '__main__':
    driver()

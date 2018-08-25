import FlipkartDownloader as fd

def FlipkartDownloader(product):
    pass

def SnapdealDownloader(product):
    pass


def downloadReview(product):
    FlipkartDownloader(product)
    SnapdealDownloader(product)
    return

def driver():
    product=input("Enter the product:")
    downloadReview(product)

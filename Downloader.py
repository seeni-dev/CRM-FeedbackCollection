import os
import pickle
import bs4
import requests


def getHtml(link):
    #todo Get the page from the source
    pass


class Downloader():
    def __init__(self,product,name="Default"):
        self.product=product
        self.link=self.makeLink(product)
        self.name=name
        return

    def makeLink(self,product):
        #should be derived in derived class
        pass

    def getPage(self):
        self.content=getHtml(self.link)
        return

    def getScore(self):
        #should be implemented in Derived Class
        pass

    def getReviews(self):
        #should be implemented in derived class
        pass

    def saveSummary(self,summary):

        #make directory for for the product
        os.makedirs(self.product,exist_ok=True)
        productDir=os.path.join(self.product,self.name)
        os.makedirs(productDir,exist_ok=True)

        with open(os.path.join(productDir,"summary.json"),"wb") as file:
            pickle.dump(summary,file)

        return

    def process(self):
        self.getPage()
        summary={}
        summary["score"]=self.getScore()
        summary["reviews"]=self.getReviews()

        self.saveSummary(summary)



class FlipkartDownloader(Downloader):

    def __init__(self,product,name="Flipkart"):
        super().__init__(product,name)

    def makeLink(self,product):
        return "" #todo 3 create a link for flipkart

    def getScore(self):
        #todo get Score for Flipkart
        pass

    def getReviews(self):
        #todo get Reviews for Flipkart
        pass


class AmazonDownloader(Downloader):

    def __init__(self, product, name="Amazon"):
        super().__init__(product, name)

    def makeLink(self, product):
        return ""  # todo 3 create a link for Amazon

    def getScore(self):
        # todo get Score for Amazon
        pass

    def getReviews(self):
        # todo get Reviews for Amazon
        pass

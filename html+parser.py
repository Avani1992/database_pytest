
from HTMLParser import HTMLParser

n=int(input())
s=input()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        print("->",attrs.name,end="")
        print(" > ",attrs.value)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        print("->",attrs.name,end="")
        print(" > ",attrs.value)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(s)
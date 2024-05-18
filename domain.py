from urllib.parse import urlparse

# Get domain name (example.com)
def getDomainName(url):
    try:
        results = getSubdomainName(url).split(".")
        return results[-2] + "." + results[-1]
    except:
        return ""

# Get sub domain name (name.example.com)
def getSubdomainName(url):
    try:
        return urlparse(url=url).netloc
    except:
        return ""
    
# print(getDomainName("https://thenewboston.com/index.php"))
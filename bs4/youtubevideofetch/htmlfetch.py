import urllib3
import certifi
import urllib.request
from http.cookiejar import CookieJar

certifi_cert_path = '/usr/local/lib/python3.6/site-packages/certifi/cacert.pem'
openssl_cert_path = '/usr/local/etc/openssl/cert.pem'
encoding = 'utf-8'


class Fetcher():
    """Used to update the html text file from Youtube.
       Use in conjunction with a cron task to update daily, or whatever."""
    
    def __init__(self, url):
        self.url = url
        
    def updateFile(self, file):
        """
        http_pool = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=openssl_cert_path)
        r = str(session.get(self.url))
        """
        fp = urllib.request.urlopen(self.url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf-8")
        fp.close()
        
        with open(file, 'w', encoding=encoding) as f:
            f.write(mystr)

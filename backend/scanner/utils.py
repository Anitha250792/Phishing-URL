import socket
import ssl
import whois
from urllib.parse import urlparse


def dns_check(url):
    try:
        domain = urlparse(url).netloc
        socket.gethostbyname(domain)
        return True
    except:
        return False


def ssl_check(url):
    try:
        domain = urlparse(url).netloc
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
        return True
    except:
        return False


def whois_check(url):
    try:
        domain = urlparse(url).netloc
        data = whois.whois(domain)
        return bool(data.domain_name)
    except:
        return False

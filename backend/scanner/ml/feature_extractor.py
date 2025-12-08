# backend/scanner/ml/feature_extractor.py
from urllib.parse import urlparse
import re
from dns_ssl_whois import dns_lookup, ssl_info, whois_info

BAD_KEYWORDS = ["login", "secure", "account", "update", "verify", "bank", "confirm", "signin", "password"]

def _has_ip(host):
    return bool(re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host))

def extract_lexical(url: str) -> dict:
    parsed = urlparse(url)
    hostname = parsed.netloc or ""
    path = parsed.path or ""
    q = parsed.query or ""
    features = {
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(path),
        "num_dots": hostname.count("."),
        "num_hyphens": url.count("-"),
        "num_digits": sum(c.isdigit() for c in url),
        "has_https": 1 if parsed.scheme == "https" else 0,
        "has_at": 1 if "@" in url else 0,
        "has_ip_in_host": 1 if _has_ip(hostname.split(":")[0]) else 0,
        "suspicious_keyword": int(any(k in url.lower() for k in BAD_KEYWORDS)),
    }
    return features

def extract_features_dict(url: str, run_network_checks: bool = False) -> dict:
    """
    Returns a flat dict of numeric features.
    - run_network_checks: if True, will attempt DNS/SSL/WHOIS network calls (may be slow)
    """
    features = extract_lexical(url)
    if run_network_checks:
        try:
            dns_feats = dns_lookup(url)
            features.update(dns_feats)
        except Exception:
            # be resilient — network may fail
            features.update({
                "dns_a_count": 0,
                "mx": 0,
                "ns_count": 0,
            })
        try:
            ssl_feats = ssl_info(url)
            features.update(ssl_feats)
        except Exception:
            features.update({"ssl_valid": 0, "ssl_days_left": -1})
        try:
            who_feats = whois_info(url)
            features.update(who_feats)
        except Exception:
            features.update({"domain_age_days": -1, "registrar_count": 0})
    return features

from saml2.assertion import Policy

HOST = 'localhost'
PORT = 8087
HTTPS = False

# Which groups of entity categories that are under scrutiny
POLICY = Policy(
    {
        "default": {"entity_categories": ["swamid", "edugain", "refeds"]}
    }
)

# HTTPS cert information
SERVER_CERT = "pki/ssl.crt"
SERVER_KEY = "pki/ssl.pem"
CERT_CHAIN = ""

DB_PATH = "./results.db"
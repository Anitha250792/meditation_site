from OpenSSL import crypto

# Certificate details
CERT_FILE = "cert.crt"
KEY_FILE = "cert.key"

# Create a key pair
key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 4096)

# Create a self-signed certificate
cert = crypto.X509()
cert.get_subject().C = "IN"               # Country
cert.get_subject().ST = "Tamil Nadu"      # State
cert.get_subject().L = "Chennai"          # Locality
cert.get_subject().O = "MeditationSite"   # Organization
cert.get_subject().OU = "Dev"             # Organizational Unit
cert.get_subject().CN = "127.0.0.1"       # Common Name (localhost/127.0.0.1)

cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # 1 year
cert.set_issuer(cert.get_subject())
cert.set_pubkey(key)
cert.sign(key, 'sha256')

# Save cert and key
with open(CERT_FILE, "wt") as f:
    f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))

with open(KEY_FILE, "wt") as f:
    f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode("utf-8"))

print(f"✅ Certificate generated: {CERT_FILE}, {KEY_FILE}")

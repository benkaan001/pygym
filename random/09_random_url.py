import secrets

# secrets.token_urlsafe([nbytes=None]):
# Return a secure random URL-safe text string, containing n-bytes random bytes.
# Use this method to generate secure hard-to-guess URLs.

url = secrets.token_urlsafe(64)

print(url)
# qVH72ydYPIU2JIaJmnlsIdbGcUZZ0AdCpxdHb_8LlZECxtgGXpZjYAAhvT-9YgZZ6vNd58Bi-W4vTDk1DPraBQ

"""https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications"""

# Run a test server.
from app import app
app.run(host='0.0.0.0', port=5000, debug=True)
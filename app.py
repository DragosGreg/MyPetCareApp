"""
This Flask application follows the Application Factory pattern to enhance modularity, scalability, 
and ease of testing. Instead of creating a global Flask app instance, it uses a factory function 
to create and configure the app dynamically.

Model adapted from:
https://flask.palletsprojects.com/en/latest/patterns/appfactories/
"""

import os

from app_factory import init_app

app = init_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_DEBUG") == "1")

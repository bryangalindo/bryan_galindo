from flask import Flask

# setting up the app
app = Flask(__name__)

# importing the views for the rest of our site
from app import views


if __name__ == '__main__':
    app.run()

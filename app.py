from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Azure Python Web App</title>
        </head>
        <body>
            <h1>Welcome to My Changed Azure PaaS Python Web App</h1>
            <p>This app is running on Azure App Service using Python 3.14 and Gunicorn.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()

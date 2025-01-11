import flask


app = flask.Flask(__name__)


@app.route("/")
def get():
    return """Hello World!<br/><br/>This website is made with Flask, Gunicorn, Nginx, and Certbot. Hosted at a Linux server on Linode.<br/><br/>The full guide of deployment is available at <a href="https://github.com/wkentaro/zero-to-https-myapp" target="_blank">https://github.com/wkentaro/zero-to-https-myapp</a>."""

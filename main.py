from sanic import Sanic
from sanic.response import html, json, redirect
from sanic.exceptions import NotFound, ServerError
import asyncio

from template_loader.template_loader import template
from validator.validator import is_mobile, is_http
from mailer.mailer import Mailer
from config.config import config

app = Sanic()

# static files
app.static('/static', './static')

# middlewares
@app.middleware('request')
async def redirect_host_urls(request):
    if 'localhost' in request.url:
        return None
    if is_http(request):
        return redirect('https://' + request.url[len('http://'):])

# exceptions
@app.exception(NotFound)
async def notfound(request, exception):
    return redirect('/')

# endpoints
@app.route("/")
async def index(request):
    message = None
    if 'message' in request.args:
        message = request.args['message'][0]
        if message.startswith("Error"):
            return html(template('index.html').render(message=message, error=True))
        else:
            return html(template('index.html').render(message=message, error=False))
        return html(template('index.html').render(message=request.args['message'][0]))
    return html(template('index.html').render())

@app.route("/contact", methods=['POST', 'GET'])
async def contact(request):
    if request.method == 'GET':
        return html(template('contact.html').render())
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        mailer, url = Mailer(), None
        try:
            mailer.send_message(name, email, subject, message)
            url = app.url_for('index', message='Your message was sent!')
        except:
            url = app.url_for('index', message='Error: message failed to send')
        return redirect(url)

@app.route("/climb")
async def climb(request):
    return html(template('climb.html').render())

@app.route("/openai")
async def openai(request):
    return html(template('openai.html').render())

@app.route("/frogger")
async def frogger(request):
    return html(template('frogger.html').render())

@app.route("/healthcheck")
async def healthcheck(request):
    return json({ 'success': True}, status=200)

if __name__ == "__main__":
    print("Starting up collinprice website in...")
    app.run(host="0.0.0.0", port=8080)

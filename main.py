from config import app
from auth.auth import auth_blueprint
from yoga.yoga import yoga_blueprint
from melodies.melodies import melodies_blueprint
from learn.learn import learn_blueprint
from journal.journal import journal_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/user')
app.register_blueprint(yoga_blueprint, url_prefix = '/yoga')
app.register_blueprint(melodies_blueprint, url_prefix = '/melodies')
app.register_blueprint(learn_blueprint, url_prefix = '/learn')
app.register_blueprint(journal_blueprint, url_prefix = '/journal')

if __name__ == '__main__':
    app.run()
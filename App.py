from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from resources import AuthorResource, BookResource, MemberResource

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
api = Api(app)

api.add_resource(AuthorResource, '/authors')
api.add_resource(BookResource, '/books')
api.add_resource(MemberResource, '/members')

if __name__ == '__main__':
    app.run(debug=True)

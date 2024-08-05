from flask import request
from flask_restful import Resource
from models import db, Author, Book, Member

class AuthorResource(Resource):
    def get(self):
        authors = Author.query.all()
        return [{'id': a.id, 'name': a.name} for a in authors]

    def post(self):
        data = request.get_json()
        author = Author(name=data['name'])
        db.session.add(author)
        db.session.commit()
        return {'id': author.id, 'name': author.name}, 201

class BookResource(Resource):
    def get(self):
        books = Book.query.all()
        return [{'id': b.id, 'title': b.title, 'isbn': b.isbn, 'author_id': b.author_id} for b in books]

    def post(self):
        data = request.get_json()
        book = Book(title=data['title'], isbn=data['isbn'], author_id=data['author_id'])
        db.session.add(book)
        db.session.commit()
        return {'id': book.id, 'title': book.title, 'isbn': book.isbn, 'author_id': book.author_id}, 201

class MemberResource(Resource):
    def get(self):
        members = Member.query.all()
        return [{'id': m.id, 'name': m.name, 'email': m.email} for m in members]

    def post(self):
        data = request.get_json()
        member = Member(name=data['name'], email=data['email'])
        db.session.add(member)
        db.session.commit()
        return {'id': member.id, 'name': member.name, 'email': member.email}, 201

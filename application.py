from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

#Sets up our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#This is our main object for importing to our database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f"{self.author} - {self.book_name} - \nPublished by: {self.publisher}"

#Our root directory
@app.route('/')
def index():
    return 'Hello!'

#Our books directory, shows our book info
@app.route('/books')
def get_books():
    books = Book.query.all()

    out = []
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

        out.append(book_data)
    return {"books": out}

#Directory to show singular books in our database
@app.route('/books/<id>')

def get_drink(id):
    book = Book.query.get_or_404(id)
    return {"name": book.book_name, "author": book.author}

#Directory to update our database with POST book information to database
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'],
                author=request.json['author'],
                publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

#Directory to update our database with DELETE book information to database
@app.route('books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "unlucky"}
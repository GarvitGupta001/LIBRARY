from utils.utils import db
from Models.author_model import Authors
from Models.publisher_model import Publishers
from Models.vendor_model import Vendors
from Models.shelf_model import Shelfs
class Books(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id', onupdate="CASCADE"), nullable=False)
    book_title = db.Column(db.String(80), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.publisher_id', onupdate="CASCADE"), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id', onupdate="CASCADE"), nullable=False)
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.shelf_id', onupdate="CASCADE"), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    language_name = db.Column(db.String(50), nullable=False)
    subject_name = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    date_of_publishing = db.Column(db.Date, nullable=False)
    date_of_addition = db.Column(db.Date, nullable=False)
    availability = db.Column(db.Integer, nullable=False)
    shelf_date = db.Column(db.Date, nullable=False)
    bought_on = db.Column(db.Date, nullable=False)
    cover_page = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f"<Book {self.book_title}>"
    def to_dict(self):
        """Convert the BookModel instance into a dictionary format."""
        return {
            'book_id': self.book_id,
            'author_id': self.author_id,
            'book_title': self.book_title,
            'publisher_id': self.publisher_id,
            'vendor_id': self.vendor_id,
            'shelf_id': self.shelf_id,
            'category': self.category,
            'price': self.price,
            'language_name': self.language_name,
            'subject_name': self.subject_name,
            'genre': self.genre,
            'date_of_publishing': self.date_of_publishing.isoformat() if self.date_of_publishing else None,
            'date_of_addition': self.date_of_addition.isoformat() if self.date_of_addition else None,
            'availability': self.availability,
            'shelf_date': self.shelf_date.isoformat() if self.shelf_date else None,
            'bought_on': self.bought_on.isoformat() if self.bought_on else None,
        }
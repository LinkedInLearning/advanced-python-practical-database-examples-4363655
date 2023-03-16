from sqlalchemy.orm import registry, relationship
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey

engine = create_engine(
    'mysql+mysqlconnector://root:password@localhost:3306/books',
    echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Author(Base):
       __tablename__ = 'authors'
       author_id = Column(Integer, primary_key=True)
       first_name = Column(String(length=50))
       last_name = Column(String(length=50))

       def __repr__(self):
            return "<Author(author_id='{0}', first_name='{1}', last_name='{2}')>" \
                  .format(self.author_id, self.first_name, self.last_name)

class Book(Base):
       __tablename__ = 'books'
       
       book_id = Column(Integer, primary_key=True)
       title = Column(String(length=255))
       number_of_pages = Column(Integer)

       def __repr__(self):
            return "<Book(book_id='{0}', title='{1}', number_of_pages='{2}')>" \
                  .format(self.book_id, self.title, self.number_of_pages)

class BookAuthor(Base):
       __tablename__ = 'bookauthors'

       bookauthor_id = Column(Integer, primary_key=True)
       author_id = Column(Integer, ForeignKey('authors.author_id'))
       book_id = Column(Integer, ForeignKey('books.book_id'))

       author = relationship("Author")
       book = relationship("Book")

       def __repr__(self):
            return "<BookAuthor (bookauthor_id='{0}', author_id='{1}', book_id='{2}', first_name='{3}', last_name='{4}', title='{5}')>" \
                  .format(self.bookauthor_id, self.author_id, self.book_id, self.author.first_name, self.author.last_name, self.book.title)

Base.metadata.create_all(engine)

from . import myblueprint
from flask import render_template
from .models import Book,Publication


@myblueprint.route('/',methods = ['GET','POST'])
def homepage():
    return render_template('home.html')

@myblueprint.route('/booklist')
def book_list():
    Books_list  = Book.query.all() #All the books are queried and added in the list Books_list
    publisher = Publication.query.all()
    return render_template('booklist.html',Books_list=Books_list,publisher=publisher)

@myblueprint.route('/publication/<pub_id>')
def publication_detail(pub_id):
    mypublication = Publication.query.filter_by(id= pub_id).first() #however only one entry is going to reflect even if we use all()
    published_books = Book.query.filter_by(pub_id = mypublication.id).all() #Getting the books that has the same pubilication ID
    return render_template('publisher.html',published_books = published_books,mypublication= mypublication)

from . import myblueprint
from flask import render_template,redirect,request,url_for,flash
from .models import Book,Publication
from .wtf_forms import AddBook
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#from flask_login import login_required

loginstatus = True

@myblueprint.route('/home',methods = ['GET','POST'])
#@login_required
def homepage():
    return render_template('home.html',loginstatus=loginstatus)

@myblueprint.route('/booklist')
#@login_required
def book_list():
    Books_list  = Book.query.all() #All the books are queried and added in the list Books_list
    publisher = Publication.query.all()
    return render_template('booklist.html',Books_list=Books_list,publisher=publisher,loginstatus=loginstatus)

@myblueprint.route('/publication/<pub_id>')
def publication_detail(pub_id):
    mypublication = Publication.query.filter_by(id= pub_id).first() #however only one entry is going to reflect even if we use all()
    published_books = Book.query.filter_by(pub_id = mypublication.id).all() #Getting the books that has the same pubilication ID
    return render_template('publisher.html',published_books = published_books,mypublication= mypublication,loginstatus=loginstatus)

@myblueprint.route('/add_book',methods=["GET","POST"])
def addbook():
    form = AddBook()
    if request.method == "POST":
        Book.add_book(form.title.data,form.author.data,form.avg_ratting.data,form.format.data,form.image.data,form.num_pages.data,form.pub_id.data)
        return redirect(url_for('myblueprint.book_list'))
    return render_template('addbook.html',form=form,loginstatus = loginstatus)


######################################################################################
## CHANGES REQUIRED FOR DELETE FUNCTION NOT YET FUNCTION PROPERLY ###################
## Might be the creation of db here again isted of importing from catlog_app/__init__
@myblueprint.route('/delete_book/<id>',methods=["GET","POST"])
def deletebook(id):
    mybook = Book.query.get(id)
    if request.method == "POST":
        db.session.delete(mybook)
        db.session.commit()
        flash("Book is deleted successfully ")
        return redirect(url_for("myblueprint.book_list"))
    return render_template("confirm_delete.html",mybook= mybook,book_id=mybook.id)

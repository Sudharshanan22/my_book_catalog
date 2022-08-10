from . import myblueprint
from flask import render_template,redirect,request,url_for,flash
from .models import Book,Publication
from .wtf_forms import AddBook,UpdateBook
from flask_sqlalchemy import SQLAlchemy
#from flask_login import login_required

loginstatus = True

@myblueprint.route('/home',methods = ['GET','POST'])
def homepage():
    return render_template('home.html',loginstatus=loginstatus)

@myblueprint.route('/booklist')
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


@myblueprint.route('/delete_book/<id>',methods=["GET","POST"])
#@login_required
def deletebook(id):
    ## Importing db from My_Application gives an error as we have created another db in model.py
    ## Importing the db from My_Application to models was not happening due to circular import error
    ## Hence importing from models in this function to avoid circular import error
    from .models import db
    mybook = Book.query.get(id)
    if request.method == "POST":
        db.session.delete(mybook)
        db.session.commit()
        flash("Book is deleted successfully ")
        return redirect(url_for("myblueprint.book_list"))
    return render_template("confirm_delete.html",mybook= mybook,loginstatus = loginstatus)

@myblueprint.route('/update_book/<id>',methods=["GET","POST"])
#@login_required
def updatebook(id):
    from .models import db
    form = UpdateBook()
    mybook = Book.query.get(id)
    if request.method == "POST":
        mybook.avg_ratting = form.avg_ratting.data
        mybook.format = form.format.data
        mybook.num_pages = form.num_pages.data
        if form.image.data:
            mybook.image = form.image.data
        else:
            mybook.image = mybook.image
        db.session.commit()
        return redirect(url_for("myblueprint.book_list"))
    return render_template("update_book.html",form = form,mybook= mybook,loginstatus = loginstatus)

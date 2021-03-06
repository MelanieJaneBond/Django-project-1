import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
from ..connection import Connection


def get_libraries():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.title,
            l.address
        from libraryapp_library l
        """)

        return db_cursor.fetchall()

@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO libraryapp_book
        (
            title, author, isbn,
            year_published, librarian_id, location_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (form_data['title'], form_data['author'],
            form_data['isbn'], form_data['year_published'],
            request.user.librarian.id, form_data["location"]))

        return redirect(reverse('libraryapp:books'))
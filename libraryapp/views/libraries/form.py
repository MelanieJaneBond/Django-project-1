import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
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
def library_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'libraries/form.html'
        context = {
            'all_libraries': libraries
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO libraryapp_library
        (
            title, address
        )
        VALUES (?, ?)
        """,
        (form_data['title'], form_data['address'])
        )

        return redirect(reverse('libraryapp:libraries'))
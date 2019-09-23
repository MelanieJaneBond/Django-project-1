import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from ..connection import Connection

@login_required
def librarian_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.location_id,
                l.user_id,
                u.first_name,
                u.last_name,
                u.email
            from libraryapp_librarian l
            join auth_user u on l.user_id = u.id
            """)

            all_librarians = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                lib = Librarian()
                lib.id = row["id"]
                lib.location_id = row["location_id"]
                lib.user_id = row["user_id"]
                lib.first_name = row["first_name"]
                lib.last_name = row["last_name"]
                lib.email = row["email"]

                all_librarians.append(lib)

        template_name = 'librarians/list.html'

        context = {
            'all_librarians': all_librarians
        }

        return render(request, template_name, context)

    #ok, I can tell that the librarians needs to GET the details of WHAT the LOCATION is called.
    # if I can pull in, perhaps in a join table, the name of the library that each librarian is a memeber of, cool

    #I wonder if I also need to ask Steve whether we are going to build Librarians differently from how we build libraries and books
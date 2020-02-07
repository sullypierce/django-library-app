from django.contrib.auth.decorators import login_required
from libraryapp.models import model_factory
import sqlite3
from ..connection import Connection
from libraryapp.models import Library
from django.shortcuts import render, redirect, reverse

def list_libraries(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address
            from libraryapp_library l
            """)

            all_libraries = db_cursor.fetchall()

            template = 'libraries/list.html'
            context = {
                'all_libraries': all_libraries
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
            (form_data['title'], form_data['address']))

        return redirect(reverse('libraryapp:libraries'))
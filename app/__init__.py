from flask import Flask

app = Flask(__name__)

from app import routes

#route-nya ada di app/routes.py
# Ini mengimpor routes.py yang berisi definisi route untuk aplikasi Flask.
# Pastikan untuk mengimpor routes setelah mendefinisikan app
# agar Flask dapat menemukan route yang telah didefinisikan.    
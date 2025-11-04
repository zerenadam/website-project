from nicegui import ui
from db import Database


db = Database()


@ui.page('/')
def home():
    ui.label('🎒 Lost & Found').classes('text-3xl font-bold mb-6')
    ui.button('➕ Add Lost Item', on_click=lambda: ui.open('/add'))
    ui.button('📜 View All Items', on_click=lambda: ui.open('/items'))

ui.run(title="Lost & Foud", reload=True)
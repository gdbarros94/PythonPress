from flask import Blueprint, render_template
from app.models.page import Page

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    page = Page.query.filter_by(slug='home').first()
    return render_template('public/home.html', page=page)

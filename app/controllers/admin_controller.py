from flask import Blueprint, render_template, redirect, url_for
from app.models.page import Page
from app.models.plugin import Plugin

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/pages/new', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        page = Page(title=title, content=content)
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/create_page.html')

@admin_bp.route('/plugins')
def manage_plugins():
    plugins = Plugin.query.all()
    return render_template('admin/manage_plugins.html', plugins=plugins)

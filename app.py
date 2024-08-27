from flask import Flask, render_template, abort
import os
import markdown2
import yaml
from datetime import datetime
import re

app = Flask(__name__)

# Путь к папке с постами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_PATH = os.path.join(BASE_DIR, 'posts')

def highlight_code_blocks(content):
    # Добавляет класс hljs для работы с highlight.js
    return re.sub(r'<pre><code class="(\w+)">', r'<pre><code class="\1 hljs">', content)

def get_post_metadata_and_content(post_name):
    post_path = os.path.join(POSTS_PATH, f'{post_name}.md')
    if not os.path.exists(post_path):
        abort(404)

    with open(post_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Разделяем фронтматтер и контент
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) == 3:
                metadata = yaml.safe_load(parts[1])
                markdown_content = parts[2]
            else:
                metadata = {}
                markdown_content = content
        else:
            metadata = {}
            markdown_content = content

        html_content = markdown2.markdown(markdown_content, extras=["fenced-code-blocks"])
        html_content = highlight_code_blocks(html_content)  # Поддержка подсветки синтаксиса
    
    return metadata, html_content

def format_date(date_str):
    try:
        # Парсинг строки даты
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z")
        # Форматирование даты: 4 мая 2020 года
        return date.strftime("%d %B %Y").replace(' 0', ' ')
    except ValueError:
        return "Unknown Date"

@app.route('/')
def index():
    posts = []
    for filename in os.listdir(POSTS_PATH):
        if filename.endswith('.md'):
            post_name = os.path.splitext(filename)[0]
            metadata, _ = get_post_metadata_and_content(post_name)
            posts.append({
                'name': post_name,
                'title': metadata.get('title', post_name),
                'date': format_date(metadata.get('date', 'Unknown Date')),
            })
    posts = sorted(posts, key=lambda x: x['date'], reverse=True)  # Сортировка постов по дате, начиная с самых новых
    return render_template('index.html', posts=posts)

@app.route('/post/<post_name>')
def post(post_name):
    metadata, html_content = get_post_metadata_and_content(post_name)
    formatted_date = format_date(metadata.get('date', 'Unknown Date'))
    return render_template('post.html', content=html_content, title=metadata.get('title', post_name), date=formatted_date)

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')

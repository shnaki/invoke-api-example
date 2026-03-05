import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

BASE_URL = "https://jsonplaceholder.typicode.com"
console = Console()


def get_posts():
    """投稿一覧を取得（先頭5件表示）"""
    response = requests.get(f"{BASE_URL}/posts")
    response.raise_for_status()
    posts = response.json()[:5]

    table = Table(
        title="投稿一覧（先頭5件）",
        show_header=True,
        header_style="bold cyan",
        border_style="dim",
        title_style="bold green",
        expand=True,
    )
    table.add_column("ID", justify="right", style="cyan", width=4)
    table.add_column("タイトル", style="white", max_width=60, overflow="fold")

    for post in posts:
        table.add_row(str(post["id"]), post["title"])

    console.print()
    console.print(Panel(table, border_style="green", padding=(0, 1)))
    console.print()
    return posts


def get_post(post_id):
    """特定の投稿を取得"""
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    response.raise_for_status()
    post = response.json()
    print(f"\n=== GET /posts/{post_id} ===")
    print(f"  Title: {post['title']}")
    print(f"  Body:  {post['body'][:80]}...")
    return post


def create_post():
    """新しい投稿を作成"""
    data = {
        "title": "Sample Post",
        "body": "This is a sample post created via API.",
        "userId": 1,
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    response.raise_for_status()
    post = response.json()
    print(f"\n=== POST /posts ===")
    print(f"  Created post ID: {post['id']}")
    print(f"  Title: {post['title']}")
    return post


def update_post(post_id):
    """投稿を更新"""
    data = {
        "title": "Updated Post",
        "body": "This post has been updated.",
        "userId": 1,
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    response.raise_for_status()
    post = response.json()
    print(f"\n=== PUT /posts/{post_id} ===")
    print(f"  Updated title: {post['title']}")
    return post


def delete_post(post_id):
    """投稿を削除"""
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    response.raise_for_status()
    print(f"\n=== DELETE /posts/{post_id} ===")
    print(f"  Status: {response.status_code}")


def main():
    get_posts()
    get_post(1)
    create_post()
    update_post(1)
    delete_post(1)


if __name__ == "__main__":
    main()

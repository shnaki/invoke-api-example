import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts():
    """投稿一覧を取得（先頭5件表示）"""
    response = requests.get(f"{BASE_URL}/posts")
    response.raise_for_status()
    posts = response.json()[:5]
    print("=== GET /posts (先頭5件) ===")
    for post in posts:
        print(f"  [{post['id']}] {post['title']}")
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

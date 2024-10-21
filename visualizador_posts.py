import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição: {response.status_code}")
        return []

def display_posts(posts):
    print("\nLista de Posts:")
    for post in posts:
        print(f"ID: {post['id']}, Título: {post['title']}")

def view_post_details(posts, post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        print(f"\nDetalhes do Post {post_id}:")
        print(f"Título: {post['title']}")
        print(f"Corpo: {post['body']}")
    else:
        print("Post não encontrado.")

def main():
    posts = fetch_posts()
    if posts:
        display_posts(posts)

        while True:
            user_input = input("\nDigite o ID do post que você deseja ver (ou 'sair' para encerrar): ")
            if user_input.lower() == 'sair':
                break
            
            try:
                post_id = int(user_input)
                view_post_details(posts, post_id)
            except ValueError:
                print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()

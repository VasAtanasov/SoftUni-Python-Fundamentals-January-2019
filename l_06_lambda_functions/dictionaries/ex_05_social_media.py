posts = {}


def add_post(params):
    post = params[0]
    if post not in posts:
        posts[post] = {
            'Post': post,
            'Likes': 0,
            'Dislikes': 0,
            'Comments': []
        }


def like_post(params):
    post = params[0]
    if post in posts:
        posts[post]['Likes'] += 1


def dislike_post(params):
    post = params[0]
    if post in posts:
        posts[post]['Dislikes'] += 1


def comment_post(params):
    post = params[0]
    if post in posts:
        posts[post]['Comments'].append(f"{params[1]}: {' '.join(params[2:])}")


actions = {
    'post': add_post,
    'like': like_post,
    'dislike': dislike_post,
    'comment': comment_post,
}

while True:
    line = input()
    if 'drop the media' == line:
        break

    tokens = line.split(' ')
    action = tokens[0]
    actions[action](tokens[1:])

for key, value in posts.items():
    print(f"Post: {key} | Likes: {value['Likes']} | Dislikes: {value['Dislikes']}")
    print("Comments:")
    if not value['Comments']:
        print('None')
    else:
        print("\n".join(map(lambda a: f'*  {a}', value['Comments'])))

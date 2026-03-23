#20. Build a Mini Social Media Platform Problem: Design classes for User, Post, and Comment. Users can post messages, like posts, and comment. Use object relationships (e.g., posts have comments), class variables to count total posts, and override the string representation methods to print user-friendly content.
class User:
    total_posts = 0

    def __init__(self, name):
        self.name = name
        self.posts = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        User.total_posts += 1
        return post

    def __str__(self):
        return self.name


class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.likes = 0
        self.comments = []

    def like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"{self.user}: {self.content} (Likes: {self.likes})"


class Comment:
    def __init__(self, text, user):
        self.text = text
        self.user = user

    def __str__(self):
        return f"{self.user} commented: {self.text}"


u1 = User("Alice")
u2 = User("Bob")

p1 = u1.create_post("Hello World")
p1.like()
p1.add_comment(Comment("Nice post!", u2))

print(p1)
for c in p1.comments:
    print(c)

print("Total Posts:", User.total_posts)
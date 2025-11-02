import typing as t
import strawberry


@strawberry.type
class User:
    id: int
    name: str


@strawberry.type
class Post:
    id: int
    title: str
    author_id: int


USERS: t.Dict[int, User] = {}
POSTS: t.Dict[int, Post] = {}
_uid = 0
_pid = 0


def _next_user_id() -> int:
    global _uid
    _uid += 1
    return _uid


def _next_post_id() -> int:
    global _pid
    _pid += 1
    return _pid


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> t.List[User]:
        return list(USERS.values())

    @strawberry.field
    def user(self, id: int) -> t.Optional[User]:
        return USERS.get(id)

    @strawberry.field
    def posts(self) -> t.List[Post]:
        return list(POSTS.values())

    @strawberry.field
    def postsByAuthor(self, author_id: int) -> t.List[Post]:
        return [p for p in POSTS.values() if p.author_id == author_id]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def createUser(self, name: str) -> User:
        uid = _next_user_id()
        user = User(id=uid, name=name)
        USERS[uid] = user
        return user

    @strawberry.mutation
    def createPost(self, title: str, author_id: int) -> Post:
        if author_id not in USERS:
            raise ValueError("author not found")
        pid = _next_post_id()
        post = Post(id=pid, title=title, author_id=author_id)
        POSTS[pid] = post
        return post


schema = strawberry.Schema(query=Query, mutation=Mutation)
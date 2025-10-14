import typing as t
from ariadne import QueryType, MutationType, make_executable_schema, gql


type_defs = gql(
    """
    type User {
      id: Int!
      name: String!
    }

    type Post {
      id: Int!
      title: String!
      author_id: Int!
    }

    type Query {
      users: [User!]!
      user(id: Int!): User
      posts: [Post!]!
      postsByAuthor(author_id: Int!): [Post!]!
    }

    type Mutation {
      createUser(name: String!): User!
      createPost(title: String!, author_id: Int!): Post!
    }
    """
)


USERS: t.Dict[int, t.Dict[str, t.Any]] = {}
POSTS: t.Dict[int, t.Dict[str, t.Any]] = {}
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


query = QueryType()
mutation = MutationType()


@query.field("users")
def resolve_users(*_) -> t.List[t.Dict[str, t.Any]]:
    return list(USERS.values())


@query.field("user")
def resolve_user(*_, id: int) -> t.Optional[t.Dict[str, t.Any]]:
    return USERS.get(id)


@query.field("posts")
def resolve_posts(*_) -> t.List[t.Dict[str, t.Any]]:
    return list(POSTS.values())


@query.field("postsByAuthor")
def resolve_posts_by_author(*_, author_id: int) -> t.List[t.Dict[str, t.Any]]:
    return [p for p in POSTS.values() if p["author_id"] == author_id]


@mutation.field("createUser")
def resolve_create_user(*_, name: str) -> t.Dict[str, t.Any]:
    uid = _next_user_id()
    user = {"id": uid, "name": name}
    USERS[uid] = user
    return user


@mutation.field("createPost")
def resolve_create_post(*_, title: str, author_id: int) -> t.Dict[str, t.Any]:
    if author_id not in USERS:
        raise ValueError("author not found")
    pid = _next_post_id()
    post = {"id": pid, "title": title, "author_id": author_id}
    POSTS[pid] = post
    return post


schema = make_executable_schema(type_defs, [query, mutation])
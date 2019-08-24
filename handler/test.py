import os
import redis


def create():
    r = redis.StrictRedis()
    with open('handler/query.txt', 'r') as f:
        content = f.read().replace('\n', '').replace('"', '\'')
    print(content)
    reply = r.execute_command('GRAPH.QUERY', 'key', content)
    print(reply)


def retrieve():
    r = redis.StrictRedis()
    reply = r.execute_command('GRAPH.QUERY', 'key', "MATCH (n) RETURN n")
    print(reply[1])


if __name__ == "__main__":
    create()

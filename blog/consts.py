from enum import Enum


class Bloggers(Enum):
    cosven = 'cosven'
    yannnli = 'yannnli'


# 127.0.0.1 and localhost are used for debug
BloggerHostMap = {
    Bloggers.cosven: ['cosven.me', 'cosven.com', '127.0.0.1:8000'],
    Bloggers.yannnli: ['yannnli.me', 'yannnli.com', 'localhost:8000'],
}

from beidaqingniao.oop.supermarket.entity.user import User
from beidaqingniao.oop.supermarket.dao.user_dao import UserDao


class UserService:
    ___udao = UserDao()

    def login(self, user):
        return UserService.___udao.login(user)

    def reg(self, user):
        return UserService.___udao.add(user)
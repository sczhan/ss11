from beidaqingniao.oop.supermarket.entity.admin import Admin
from beidaqingniao.oop.supermarket.dao.admin_dao import AdminDao


class AdminService:

    def login(self, admin):
        admindao = AdminDao()
        return admindao.login(admin)
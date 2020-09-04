from beidaqingniao.oop.new_supermarket.entity.user import User

from beidaqingniao.oop.new_supermarket.dao.user_dao import UserDao
from beidaqingniao.oop.new_supermarket.dao.item_Dao import ItemDao
from beidaqingniao.oop.new_supermarket.dao.order_dao import OrderDao
from functools import reduce


class OrderService:
    __odao = OrderDao()
    __udao = UserDao()
    __idao = ItemDao()

    def add(self, order):
        try:
            OrderService.__odao.add(order)
            sum = reduce(lambda a, b: a + b, map(lambda x: x.price * x.stock, order.items))
            # sum=0
            for i in order.items:
                # sum+=i.stock*i.price
                OrderService.__idao.updata_stock(i)
            print(int(sum))
            user = User(user_name=order.user_id, point=int(sum))
            OrderService.__udao.update_point(user)
            return True
        except:
            return False

    def price(self, order):
        sum = reduce(lambda a, b: a + b, map(lambda x: x.price * x.stock, order.items))
        return sum

    def item_order(self, order):
        a = order.items
        a = str(a[0])
        b = a.split(":")
        c = b[1].split(",")
        return b[0] + ": " + c[0] + "个数:" + b[3] + ": " + b[4]




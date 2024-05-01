# class Payment:
#     def pay(self, money):
#         raise NotImplementedError

from abc import ABCMeta, abstractclassmethod

# 接口
class Payment(metaclass=ABCMeta):
    @classmethod
    @abstractclassmethod
    def Pay(self, money):
        pass

class AliPay(Payment):
    pass
    # def Pay(self, money):
    #     print("支付宝支付 %d 元." % money)

class WechatPay:
    def pay(self, money):
        pass

p = AliPay()

p.Pay(100)
# _*_ coding=utf-8 _*_


"""
适配器模式：将一个类的接口装化成客户希望的另一个接口。
            使得原本由于接口不兼容而不能起一工作的那些类可以一起工作。
两种实现方式：
    类适配器：使用多继承
    对象适配器：使用组合
"""

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):

    def pay(self, money):
        print("支付宝支付%s" % money)


class BankPay:
    def cost(self, money):
        print("银联支付%s" % money)


# 类适配器:适用于单个或少数需要适配的接口
class AdapterClass(Payment, BankPay):

    def pay(self, money):
        self.cost(money)


# 组合适配器：适用于多个需要适配的接口
class AdapterCombination(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = AdapterCombination(BankPay())
p.pay(100)

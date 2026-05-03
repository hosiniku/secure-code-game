'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal, InvalidOperation

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ORDER_AMOUNT = 1_000_000    # 한도 설정(100만 달러)

def validorder(order: Order):
    net = Decimal(0)    # float 대신 Decimal로 정밀한 계산

    for item in order.items:
        # 숫자 타입 검증
        if not isinstance(item.amount, (int, float)):
            return "Invalid amount: %s" % item.amount
        if item.type == 'product' and not isinstance(item.quantity, (int, float)):
            return "Invalid quantity: %s" % item.quantity
        
        # float -> Decimal 변환
        try:
            amount = Decimal(str(item.amount))
            quantity = Decimal(str(item.quantity))
        except InvalidOperation:
            return "Invalid amount: %s" % item.amount

        # 한도 초과 체크
        if item.type == 'product' and abs(amount * quantity) > MAX_ORDER_AMOUNT:
            return "Total amount payable for an order exceeded"

        if item.type == 'payment':
            net += amount
        elif item.type == 'product':
            net -= amount * quantity
        else:
            return "Invalid item type: %s" % item.type

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
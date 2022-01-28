"""
주문 상품 가격이 20,000원 미만이면 배송비 2,500원 추가
"""

def get_price(unit_price, quantity):    # 단위당 가격, 수량
    delivery_fee = 2500                 # 배송비
    price = unit_price * quantity    # 상품 주문 가격
    if price < 20000:
        price = price + delivery_fee
    else:
        price
    return price
    

price1 = get_price(15000, 2)
price2 = get_price(5000, 3)     # 배송비 추가

print("상품1 가격 : " + str(price1) + "원")
print("상품2 가격 : " + str(price2) + "원")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

product_name = input("Product Name: ")
def col_one(points):
    arr_one = []
    for i in range(len(points)):
        col_one_values = points.iloc[i,0]
        arr_one.append(col_one_values)
        # print(arr_one)
    return arr_one

def col_two(points):
    arr_one = []
    for i in range(len(points)):
        col_one_values = points.iloc[i,1]
        arr_one.append(col_one_values)
        # print(arr_one)
    return arr_one

def profit_cal(tax, mp_price, ps, cp):
    pp = (cp - (mp_price + tax))*ps
    return pp

def loss_cal(pp, cp):
    loss = (pp - cp)/pp
    return loss

# def data_cal(tax, mp_price, ps, cp)

# Product A:

product_a_points = pd.read_csv('price_product_a.csv')
product_a_price = np.array(col_one(product_a_points)).reshape(-1, 1)
product_a_sales = np.array(col_two(product_a_points)).reshape(-1, 1)

# Product B:

product_b_points = pd.read_csv('price_product_b.csv')
product_b_price = np.array(col_one(product_b_points)).reshape(-1, 1)
product_b_sales = np.array(col_two(product_b_points)).reshape(-1, 1)

# Product C:

product_c_points = pd.read_csv('price_product_c.csv')
product_c_price = np.array(col_one(product_c_points)).reshape(-1, 1)
product_c_sales = np.array(col_two(product_c_points)).reshape(-1, 1)

# Product D:

product_d_points = pd.read_csv('price_product_d.csv')
product_d_price = np.array(col_one(product_d_points)).reshape(-1, 1)
product_d_sales = np.array(col_two(product_d_points)).reshape(-1, 1)

if product_name == "A":
    tax = 9
    mp_price = 60
    current_price_product_a = int(input("Current price of product: "))
    range_price = current_price_product_a - 80
    model = LinearRegression()
    model.fit(product_a_price, product_a_sales)
    prev_sales = model.predict(np.array(current_price_product_a).reshape(-1, 1))
    print("Previous Sales: ", prev_sales)
    prev_price_profit = profit_cal(tax, mp_price, prev_sales, current_price_product_a)
    print("Prev price profit: ", prev_price_profit)

    plt.scatter(product_a_price, product_a_sales)
    plt.plot(np.linspace(0, 160, 100).reshape(-1, 1), model.predict(np.linspace(0, 160, 100).reshape(-1, 1)), 'r')
    plt.ylim(0, 100)
    # plt.show()

    print("Choose option------")
    print("1. Increasing sales with 0 loss models      2. Profit centric models")
    choice = int(input())

    if choice == 1:
        print("Algo for sales boosting")
        n = int((range_price / 2)+1)
        print(n)
        profit_arr = []
        for i in range(1, n):
            L = 2*i
            # print(i)
            mock_price = current_price_product_a - L
            new_sales = model.predict(np.array(mock_price).reshape(-1,1))
            new_price_profit = profit_cal(tax, mp_price, new_sales, mock_price)
            loss = loss_cal(prev_price_profit, new_price_profit)
            # print(mock_price, new_sales, new_price_profit, loss)
            # print(loss)
            if loss <= 0:
                new_object = {"profit": str(new_price_profit), "sales": str(new_sales), "price": mock_price}
                profit_arr.append(new_object)
        profits = [obj["profit"] for obj in profit_arr]
        max_profit = max(profits)
        max_profit_element = next((item for item in profit_arr if item["profit"] == max_profit), None)
        print("maximum profit: ", max_profit_element)
    elif choice ==2:
        print("Algo for profit boosting")


elif product_name == "B":
    tax = 21
    mp_price = 80
    current_price_product_b = int(input("Current price of product: "))
    range_price = current_price_product_b - 120

    model = LinearRegression()
    model.fit(product_b_price, product_b_sales)

    prev_sales = model.predict(np.array(current_price_product_b).reshape(-1, 1))
    print("Previous Sales: ", prev_sales)
    prev_price_profit = profit_cal(tax, mp_price, prev_sales, current_price_product_b)
    print("Prev price profit: ", prev_price_profit)

    plt.scatter(product_b_price, product_b_sales)
    plt.plot(np.linspace(0, 260, 100).reshape(-1, 1), model.predict(np.linspace(0, 160, 100).reshape(-1, 1)), 'r')
    plt.ylim(0, 100)
    # plt.show()

    print("Choose option------")
    print("1. Increasing sales with 0 loss models      2. Profit centric models")
    choice = int(input())

    if choice == 1:
        print("Algo for sales boosting")
        n = int((range_price / 2) + 1)
        print(n)
        profit_arr=[]
        for i in range(1, n):
            L = 2 * i
            # print(i)
            mock_price = current_price_product_b - L
            new_sales = model.predict(np.array(mock_price).reshape(-1, 1))
            new_price_profit = profit_cal(tax, mp_price, new_sales, mock_price)
            loss = loss_cal(prev_price_profit, new_price_profit)
            print(mock_price, new_sales, new_price_profit, loss)
            # print(loss)
            if loss <= 0:
                new_object = {"profit": str(new_price_profit), "sales": str(new_sales), "price": mock_price}
                profit_arr.append(new_object)
        profits = [obj["profit"] for obj in profit_arr]
        max_profit = max(profits)
        max_profit_element = next((item for item in profit_arr if item["profit"] == max_profit), None)
        print("maximum profit: ", max_profit_element)
    elif choice == 2:
        print("Algo for profit boosting")


elif product_name == "C":
    tax = 57
    mp_price = 160
    current_price_product_c = int(input("Current price of product: "))
    range_price = current_price_product_c - 240

    model = LinearRegression()
    model.fit(product_c_price, product_c_sales)

    prev_sales = model.predict(np.array(current_price_product_c).reshape(-1, 1))
    print("Previous Sales: ", prev_sales)
    prev_price_profit = profit_cal(tax, mp_price, prev_sales, current_price_product_c)
    print("Prev price profit: ", prev_price_profit)

    plt.scatter(product_c_price, product_c_sales)
    plt.plot(np.linspace(0, 370, 100).reshape(-1, 1), model.predict(np.linspace(0, 160, 100).reshape(-1, 1)), 'r')
    plt.ylim(0, 100)
    # plt.show()

    print("Choose option------")
    print("1. Increasing sales with 0 loss models      2. Profit centric models")
    choice = int(input())

    if choice == 1:
        print("Algo for sales boosting")
        n = int((range_price / 2) + 1)
        print(n)
        profit_arr = []
        for i in range(1, n):
            L = 2 * i
            # print(i)
            mock_price = current_price_product_c - L
            new_sales = model.predict(np.array(mock_price).reshape(-1, 1))
            new_price_profit = profit_cal(tax, mp_price, new_sales, mock_price)
            loss = loss_cal(prev_price_profit, new_price_profit)

            if loss <= 0:
                new_object = {"profit": str(new_price_profit), "sales": str(new_sales), "price": mock_price}
                profit_arr.append(new_object)
        profits = [obj["profit"] for obj in profit_arr]
        max_profit = max(profits)
        max_profit_element = next((item for item in profit_arr if item["profit"] == max_profit), None)
        print("maximum profit: ", max_profit_element)
    elif choice == 2:
        print("Algo for profit boosting")

elif product_name == "D":
    tax = 117
    mp_price = 347
    current_price_product_d = int(input("Current price of product: "))
    range_price = current_price_product_d - 510

    model = LinearRegression()
    model.fit(product_d_price, product_d_sales)

    prev_sales = model.predict(np.array(current_price_product_d).reshape(-1, 1))
    print("Previous Sales: ", prev_sales)
    prev_price_profit = profit_cal(tax, mp_price, prev_sales, current_price_product_d)
    print("Prev price profit: ", prev_price_profit)

    plt.scatter(product_d_price, product_d_sales)
    plt.plot(np.linspace(300, 720, 100).reshape(-1, 1), model.predict(np.linspace(0, 160, 100).reshape(-1, 1)), 'r')
    plt.ylim(0, 100)
    # plt.show()

    print("Choose option------")
    print("1. Increasing sales with 0 loss models      2. Profit centric models")
    choice = int(input())

    if choice == 1:
        print("Algo for sales boosting")
        n = int((range_price / 2) + 1)
        print(n)
        profit_arr = []
        for i in range(1, n):
            L = 2 * i
            # print(i)
            mock_price = current_price_product_d - L
            new_sales = model.predict(np.array(mock_price).reshape(-1, 1))
            new_price_profit = profit_cal(tax, mp_price, new_sales, mock_price)
            loss = loss_cal(prev_price_profit, new_price_profit)

            if loss <= 0:
                new_object = {"profit": str(new_price_profit), "sales": str(new_sales), "price": mock_price}
                profit_arr.append(new_object)
        profits = [obj["profit"] for obj in profit_arr]
        max_profit = max(profits)
        max_profit_element = next((item for item in profit_arr if item["profit"] == max_profit), None)
        print("maximum profit: ", max_profit_element)
    elif choice == 2:
        print("Algo for profit boosting")

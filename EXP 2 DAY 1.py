import pandas as pd
data ={'customer_id':[100,101,102,103,101],
        'order_date':["2023-08-12","2023-09-15","2023-08-04","2023-08-31","2023-09-13"],
        'product_name':["HP","Asus","HP","Dell","MSI"],
        'order_quantity':[3,2,1,4,1] }
order_data = pd.DataFrame(data)
customer_count = order_data.groupby("customer_id").size()
average_quantity = order_data.groupby("product_name")["order_quantity"].mean()
early_date = order_data["order_date"].min()
late_date = order_data["order_date"].max()
print("Data Frame:")
print(order_data)
print("1. Number of order by each customer :")
print(customer_count)
print("2. Average order quantity :")
print(average_quantity)
print("3a. Earliest date :")
print(early_date)
print("3b. Latest date :")
print(late_date)

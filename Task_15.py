
sales_data = [
    {"name": "Ноутбук", "price": 50000, "quantity": 3},
    {"name": "Мышь", "price": 1500, "quantity": 10},
    {"name": "Клавиатура", "price": 3000, "quantity": 5},
    {"name": "Мышь", "price": 1500, "quantity": 4},
    {"name": "Монитор", "price": 20000, "quantity": 4},
]

revenue_by_product = {}


for record in sales_data:
    item_name = record["name"]
    total = record["price"] * record["quantity"]
    revenue_by_product[item_name] = revenue_by_product.get(item_name, 0) + total

print("Выручка по товарам:")
for product, revenue in revenue_by_product.items():
    print(f"{product}: {revenue:,.2f} руб.")


most_profitable_product = max(revenue_by_product, key=revenue_by_product.get)
max_revenue = revenue_by_product[most_profitable_product]


unique_names_count = len(revenue_by_product)

print("\n--- Итоги ---")
print(f"Самый прибыльный товар: '{most_profitable_product}' (выручка {max_revenue:,.2f} руб.)")
print(f"Количество уникальных наименований: {unique_names_count}")
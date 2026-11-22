import random
import pandas as pd
import plotly.express as px

TEMPLATE = "plotly_white"

random.seed(42)

categories = ["Ноутбуки", "Смартфоны", "Наушники", "Мониторы"]
cities = ["Минск", "Гродно", "Брест"]
dates = pd.date_range(start="2026-01-01", periods=30, freq="D")

rows = []
for i, date in enumerate(dates):
    cat = random.choice(categories)
    city = random.choice(cities)
    price = random.randint(150, 2500)
    quantity = random.randint(1, 10)
    rating = round(random.uniform(3.2, 5.0), 1)
    rows.append({
        "OrderID": f"ORD-{100 + i}",
        "Date": date,
        "Category": cat,
        "City": city,
        "Price": float(price),
        "Quantity": quantity,
        "Rating": rating,
    })

df = pd.DataFrame(rows)


df.loc[[2, 10], "Price"] = None
df.loc[[5, 18], "Rating"] = None
df.loc[[4, 15], "City"] = None
df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)




print("    ПЕРВЫЕ 5 СТРОК    ")
print(df.head())

print("\n    ИНФОРМАЦИЯ О ТИПАХ ДАННЫХ     ")
print(df.info())

print("\n    ОПИСАТЕЛЬНАЯ СТАТИСТИКА      ")
print(df.describe())


print("\     ПРОПУСКИ ДО ЗАПОЛНЕНИЯ        ")
print(df.isnull().sum())


for col in ["Price", "Rating"]:
    df[col] = df[col].fillna(df[col].median())


for col in ["Category", "City"]:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\n    ПРОПУСКИ ПОСЛЕ ЗАПОЛНЕНИЯ      ")
print(df.isnull().sum())


dup_count = df.duplicated().sum()
print(f"\nНайдено полных дубликатов: {dup_count}")
if dup_count > 0:
    df = df.drop_duplicates().reset_index(drop=True)


print("\n    МАТРИЦА КОРРЕЛЯЦИИ       ")
print(df.corr(numeric_only=True).round(2))


df["Revenue"] = df["Price"] * df["Quantity"]


print("\n     СТАТИСТИКА ПО КАТЕГОРИЯМ")
group_stats = df.groupby("Category")["Revenue"].agg(["count", "mean", "median"]).round(2)
print(group_stats)


print("\n     СВОДНАЯ ТАБЛИЦА (Средняя выручка: Category x City)      ")
pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Category",
    columns="City",
    aggfunc="mean",
    fill_value=0
).round(2)
print(pivot)


print("\n     ТОП-5 ЗАКАЗОВ ПО ВЫРУЧКЕ (с рейтингом >= 4.0)    ")
filtered_df = df[df["Rating"] >= 4.0]
top_5 = filtered_df.sort_values(by="Revenue", ascending=False).head(5)
print(top_5[["OrderID", "Date", "Category", "City", "Revenue", "Rating"]])


pivot_long = pivot.reset_index().melt(id_vars="Category", var_name="City", value_name="AvgRevenue")

fig1 = px.bar(
    pivot_long,
    x="Category",
    y="AvgRevenue",
    color="City",
    barmode="group",
    text_auto=".0f",
    title="Средняя выручка по категориям и городам",
    labels={"Category": "Категория", "AvgRevenue": "Средняя выручка (BYN)", "City": "Город"},
    template=TEMPLATE,
)
fig1.show()


fig2 = px.box(
    df,
    x="Category",
    y="Revenue",
    color="Category",
    title="Распределение выручки по категориям товаров",
    labels={"Category": "Категория", "Revenue": "Выручка (BYN)"},
    template=TEMPLATE,
)
fig2.show()


daily_revenue = df.groupby("Date", as_index=False)["Revenue"].sum()

fig3 = px.line(
    daily_revenue,
    x="Date",
    y="Revenue",
    markers=True,
    title="Динамика общей выручки по дням",
    labels={"Date": "Дата", "Revenue": "Выручка за день (BYN)"},
    template=TEMPLATE,
)
fig3.show()


fig4 = px.imshow(
    pivot,
    text_auto=".0f",
    aspect="auto",
    color_continuous_scale="Blues",
    title="Тепловая карта: средняя выручка (Категория x Город)",
    labels={"x": "Город", "y": "Категория", "color": "Выручка (BYN)"},
    template=TEMPLATE,
)
fig4.show()
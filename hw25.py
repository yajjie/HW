import pandas as pd

# 1. 讀取正確路徑下的雜貨店資料
df = pd.read_csv('archive/Grocery_Inventory_and_Sales_Dataset.csv')

# 2. 清理價格欄位：把 '$' 拿掉，並轉換成純數字型態 (float)
df['Unit_Price'] = df['Unit_Price'].str.replace('$', '', regex=False).astype(float)


# (1) 計算每個商品的總庫存價值
df['Total_Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']

print("--- 每個商品的總庫存價值 ---")
print(df[['Product_Name', 'Total_Inventory_Value']])


# (2) 找出最暢銷
best_seller = df.loc[df['Sales_Volume'].idxmax()]

print("\n--- 最暢銷商品 ---")
print(best_seller['Product_Name'])


# (3) 計算 9 折後的收入
total_revenue = (df['Sales_Volume'] * df['Unit_Price'] * 0.9).sum()

print("\n--- 9折後的收入 ---")
print(round(total_revenue, 2))
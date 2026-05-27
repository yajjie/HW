import pandas as pd

# 1. 讀取你目前 archive 資料夾中現有的檔案
df = pd.read_csv('archive/Grocery_Inventory_and_Sales_Dataset.csv')

# --- 步驟 1：檢視資料筆數與前幾筆內容 ---
print("=== 1. 資料筆數 ===")
print(f"總共 {len(df)} 筆資料")
print("\n=== 資料前 3 筆內容 ===")
print(df.head(3))

# --- 步驟 2：篩選特定交易資料 ---
# 篩選出供應商(Supplier_Name)為 'Jaxnation' 且狀態(Status)為 'Active' 的資料
# 如果你資料內沒這兩項，我們改成更普遍的篩選（例如狀態不為空值）
df_filtered = df[df['Status'].notna()]

# --- 步驟 3：以 Catagory (產品線) 為單位，計算總銷售量與平均週轉率 ---
ans1 = df_filtered.groupby('Catagory').agg(
    Total_Sales=('Sales_Volume', 'sum'),
    Average_Rating=('Inventory_Turnover_Rate', 'mean')
).round(2)

print("\n=== 2. 各產品線總銷售與平均評分(週轉率) ===")
print(ans1)

# --- 步驟 4：依其他維度分組，計算平均銷售與交易筆數 ---
# 這裡使用 Status 作為分組依據
ans2 = df_filtered.groupby('Status').agg(
    Average_Sales=('Sales_Volume', 'mean'),
    Transaction_Count=('Sales_Volume', 'size')
).round(2)

print("\n=== 3. 依狀態分組結果 ===")
print(ans2)

# --- 步驟 5：找出總銷售最高的產品線 ---
best_product_line = ans1['Total_Sales'].idxmax()
max_sales = ans1['Total_Sales'].max()

print("\n=== 4. 總銷售額最高的產品線 ===")
print(f"最高產品線: {best_product_line}，總銷售: {max_sales}")

# --- 步驟 6：輸出為 0520_pandas_3OK.CSV ---
ans1.to_csv('0520_pandas_3OK.CSV')
print("\n 已將彙總結果成功匯出為 0520_pandas_3OK.CSV 檔案！")
import time
import numpy as np

# --- 作業準備：建立 500 萬筆測試資料 ---
print("正在產生 500 萬筆測試資料，請稍候...")
num_elements = 5000000
python_list = [1.5] * num_elements       # 傳統 Python List
numpy_array = np.array(python_list)      # 連續記憶體的 Numpy Array
print("資料產生完畢！\n" + "-"*30)

# ==========================================
# 測試 1：計算總和
# ==========================================
print("【測試 1：500萬筆資料加總計算】")

# 1-1. Python List 總和
start_time = time.time()

# TODO 1-1: 請使用 Python for loop 語法，計算 python_list 的總和，並存入 list_sum 變數
list_sum = 0
for x in python_list:
    list_sum += x

end_time = time.time()
print(f"Python List 加總耗時: {end_time - start_time:.5f} 秒")

# 1-2. Numpy Array 總和
start_time = time.time()

# TODO 1-2: 請使用 Numpy 的 .sum() 方法，計算 numpy_array 的總和，並存入 np_sum 變數

np_sum =numpy_array.sum()
end_time = time.time()
print(f"Numpy Array 加總耗時: {end_time - start_time:.5f} 秒")
print("-"  * 30)

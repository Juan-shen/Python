# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取商
print(1 % 1)  # 取餘數
print(2**3)  # 次方

# 優先順序
# 1. () 括號
# 2. **次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

# input() 讓使用者在終端機入入資料
# input() 的括弧內可以放入"提示字串"
a = input("請輸入數字：")
# 透過 input() 輸入的資料都是字串
print(a + "1")  # 字串相加
print(int(a) + 1)  # 將字串轉換成整數在相加

# 正方形面積計算
r = input("請輸入正方形邊長：")
r = int(r)  # 將字串轉換成整數
area = r * r  # 計算面積
print(f"正方形面積為： {area}")  # 印出面積

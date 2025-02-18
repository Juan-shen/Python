# 變數
# 變數可以使用=將右邊的資料儲存在變數中
# 變數開頭不能使用數字，不能用保留字，不能有空白，不能有特殊符號但可以用底線
# 變數名稱大小寫有區分
# 舉例myName與myname是不同變數
a = True
print(a)

myName = 123
print(myName)

myName = "Donna"
age = 20
print("Hello, {myName},you are {age} years old")
# f-strings(formatted string
print(f"Hello, {myName}, you are {age} years old")
age = "25"
print("Hello, " + myName + ", you are " + age + " years old")

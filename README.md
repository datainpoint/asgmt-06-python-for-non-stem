# asgmt-06-python-for-non-stem
Assignment 06: Python for Non-STEM.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為三種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 程式題：以函數/類別宣告答案，函數/類別名稱下的長字串（docstring）會描述測試資料與預期輸出，能夠讓我們充分暸解預期輸入以及預期輸出之間的對應關係，寫作完畢後要記得輸出答案的變數 `return your_answer_variable`
- 如果練習題需要載入檔案，檔案會與練習題存放在同個資料夾中，這時可以運用工作目錄的相對路徑直接指定檔案名稱載入。
- 寫作完成後將 `answers.py` 存檔，再執行專案資料夾中的 `test_runner.py` 進行測試，再依照測試結果修正答案或截圖測試結果繳交作業。

## 01.（程式題）定義函數 `answer_01()` 能夠將輸入整數的因數個數輸出。

來源：<https://en.wikipedia.org/wiki/Divisor>

```python
def answer_01(x: int) -> int:
    """
    >>> answer_01(1)
    1
    >>> answer_01(2)
    2
    >>> answer_01(3)
    2
    >>> answer_01(4)
    3
    >>> answer_01(5)
    2
    """
```

## 02.（程式題）定義函數 `answer_02()` 能夠判斷輸入整數是否為質數。

來源：<https://en.wikipedia.org/wiki/Prime_number>

```python
def answer_02(x: int) -> bool:
    """
    >>> answer_02(1)
    False
    >>> answer_02(2)
    True
    >>> answer_02(3)
    True
    >>> answer_02(4)
    False
    >>> answer_02(5)
    True
    """
```

## 03.（程式題）定義函數 `answer_03()` 能夠判斷輸入的數個整數是否為質數。

來源：<https://en.wikipedia.org/wiki/Prime_number>

```python
def answer_03(x: list) -> list:
    """
    >>> answer_03([1, 2, 3, 4, 5])
    [False, True, True, False, True]
    >>> answer_03([6, 7, 8, 9, 10])
    [False, True, False, False, False]
    """
```

## 04.（程式題）定義函數 `answer_04()` 能夠回傳一個符合 Fizz buzz 規則元素的片段。

來源：<https://en.wikipedia.org/wiki/Fizz_buzz>

```python
def answer_04(start: int, stop: int) -> list:
    """
    >>> answer_04(1, 5)
    [1, 2, 'Fizz', 4, 'Buzz']
    >>> answer_04(11, 15)
    [11, 'Fizz', 13, 14, 'Fizz Buzz']
    >>> answer_04(25, 30)
    ['Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz']
    """
```

## 05.（程式題）定義函數 `answer_05()` 能夠以新台幣的硬幣與鈔票來進行最佳的找零。

```python
notes = {100, 200, 500, 1000}
coins = {1, 5, 10, 50}
```

```python
def answer_05(price: int, paid: int) -> dict:
    """
    >>> answer_05(99, 100)
    {'1': 1}
    >>> answer_05(99, 200)
    {'100': 1, '1': 1}
    >>> answer_05(99, 500)
    {'200': 2, '1': 1}
    >>> answer_05(99, 1000)
    {'500': 1, '200': 2, '1': 1}
    >>> answer_05(49, 50)
    {'1': 1}
    >>> answer_05(49, 100)
    {'50': 1, '1': 1}
    >>> answer_05(49, 200)
    {'100': 1, '50': 1, '1': 1}
    >>> answer_05(49, 500)
    {'200': 2, '50': 1, '1': 1}
    >>> answer_05(49, 1000)
    {'500': 1, '200': 2, '50': 1, '1': 1}
    >>> answer_05(119, 150)
    {'10': 3, '1': 1}
    >>> answer_05(119, 200)
    {'50': 1, '10': 3, '1': 1}
    >>> answer_05(119, 500)
    {'200': 1, '100': 1, '50': 1, '10': 3, '1': 1}
    >>> answer_05(119, 1000)
    {'500': 1, '200': 1, '100': 1, '50': 1, '10': 3, '1': 1}
    """
```
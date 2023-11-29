# list

test
a
## 型について

list, dict, set, tupleの型アノテーションは:

- Pythonのバージョン3.5〜3.8では、typingからインポートする必要がる。
- Pythonのバージョン3.9以降では、typingのインポートは不要で、組み込み型をジェネリック型として使用できる。
- 3.9以降でも組み込み型として存在していないものは、typingからインポートする必要がある。

``` python
# 3.5 ~ 3.8
from typing import List


numbers: List[int] = [1, 3, 5, 7]

def sum_numbers(numbers: List[int]) -> int:
    return sum([number for number in numbers])
```

``` python
# 3.9以降
numbers: list[int] = [1, 3, 5, 7]

def sum_numbers(numbers: list[int]) -> int:
    return sum([number for number in numbers])
```

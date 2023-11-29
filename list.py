"""
list型の扱い方を試す

Authors: behike56
Version: 1.0.0
License: MIT
"""

from typing import List


def list_main() -> None:

    # how_to_initialize(dir(list))
    # how_slice_work(range(20))
    # delete_specify_number(list(range(5)), 3)
    # deleted_list = delete_number_with_index(list(range(3)), 3)
    # print(deleted_list)

    # [0, 1, 2, 3, 4]
    # 
    inserted_list = insert_with_other(list(range(5)), 5, 99)
    print(inserted_list)


def how_to_initialize(definition: list[str]) -> None:
    """_summary_

    Args:
        definition (list[str]): _description_

    Return:
        None
    """

    print(definition)

    list_0 = ['abc', 123, ['def', 456], {'name': 'Gordon'}]

    list_1: List[str] = ["ABC", "あいうえお"]

    list_2: List[int] = [1, 5, 7, 11]

    list_3: List[List[str]] = [["A", "B", "C"], ["Q", "O", "L"]]

    list_4: List[int] = [range(1, 20)]
    list_5: List[int] = list(range(1, 20))

    list_6: List[int] = [1] + [2]
    list_7: List[int] = list_2 + list_5
    list_8: List[int] = list_5[3:5]

    print(list_0)
    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)
    print(list_5)
    print(list_6)
    print(list_7)
    print(list_8)


def how_slice_work(numbers: list[int]) -> None:
    """_summary_

    Args:
        numbers (list[int]): _description_

    Return:
        None
    """

    print(numbers[:4])
    print(numbers[3:])
    print(numbers[:])
    print(numbers[::2])
    print(numbers[::-1])


def delete_specify_number(numbers: list[int], number: int) -> list[int]:
    """
    指定された数値をリストから削除する

    Args:
        numbers (list[int]): 削除対象のリスト
        number (int): 削除対象の数値

    Returns:
        list[int]:
            削除対象の数値がリストに有る場合は、削除後のリストを返す。
            削除対象の数値がリストに無い場合は、削除対象のリストを返す。
    """

    if number in numbers:
        return numbers.remove(number)

    if number not in numbers:
        return numbers


def delete_number_with_index(numbers: list[int], index: int) -> list[int]:
    """
    指定されたインデックスの数値を削除する。

    Args:
        numbers (list[int]): 削除対象のリスト
        index (int): 削除対象のインデックス

    Returns:
        list[int]:
            削除対象のリストが空の場合は、削除対象のリストを返す。
            削除対象のリストが空ではなく、
    """
    list_length: int = len(numbers)

    print("リストのサイズは: %d, インデックスは: %d. " % (list_length, index))

    if list_length == 0:
        return numbers

    if list_length <= index:
        return numbers

    if list_length > 0 and list_length > index:
        numbers.pop(index)
        return numbers


def extend_with_other(target: list[int], other: list[int]) -> list[int]:
    """_summary_

    Args:
        target (list[int]): _description_
        other (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    return target.extend(other)


def insert_with_other(numbers: list[int], index: int, value: int) -> list[int]:
    """_summary_

    Args:
        numbers (list[int]): _description_
        index (int): _description_
        value (int): _description_

    Returns:
        list[int]: _description_
    """
    list_length: int = len(numbers)
    max_index: int = list_length - 1

    print("insert_with_other() => リストのサイズ: %d, インデックス: %d, MAX_INDEX: %d. "
          % (list_length, index, max_index))

    if list_length == 0:
        return numbers

    if index > max_index:
        return numbers

    # 挿入可能なインデックスは最大のインデックス-1となる
    if list_length > 0 and index <= max_index:
        numbers.insert(index, value)
        return numbers


if __name__ == "__main__":
    list_main()

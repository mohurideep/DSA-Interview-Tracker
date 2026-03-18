> You are given:
>
> * An integer `target`
> * An array of **distinct positive integers** `nums`
>
> Your task is to determine **how many unique combinations of elements** from the array sum up exactly to the target.

---

## 📌 Rules

* Each element can be used **at most once**
* The **order of elements does NOT matter**

  * `[2, 3, 5]` and `[5, 3, 2]` are considered the **same combination**
* Return the **count of unique combinations**

---

## 📌 Function Signature

```python
def countCombinations(nums: List[int], target: int) -> int:
```

---

## 🔍 Example

```text
Input:
nums = [1, 2, 3, 4, 5]
target = 10

Output:
3
```

### Explanation:

The valid unique combinations are:

* `[1, 2, 3, 4]`
* `[1, 4, 5]`
* `[2, 3, 5]`

---

## ⚠️ Constraints

* `1 <= len(nums) <= N`
* All elements are **positive integers**
* No duplicates in input array

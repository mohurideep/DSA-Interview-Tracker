> You are given a list of temperature readings collected at regular time intervals.
>
> A **valley point** is defined as an index `i` such that:
>
> * `temperature[i]` is strictly less than its immediate neighbors
>   i.e.,
>
>   ```
>   temperature[i] < temperature[i - 1] AND temperature[i] < temperature[i + 1]
>   ```
>
> Your task is to return a list of all indices where valley points occur.

---

## 📌 Function Signature

```python
def detectValleys(temperature: List[int]) -> List[int]:
```

---

## ⚠️ Constraints

* If the list has **fewer than 3 elements**, return an empty list
* Only consider indices from `1` to `n-2` (ignore first and last elements)
* All values are integers

---

## 🔍 Example

```text
Input:
temperature = [30, 20, 25, 19, 22, 18, 23]

Output:
[1, 3, 5]
```

### Explanation:

* Index 1 → 20 < 30 and 25 ✅
* Index 3 → 19 < 25 and 22 ✅
* Index 5 → 18 < 22 and 23 ✅


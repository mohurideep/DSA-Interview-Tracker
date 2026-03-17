> **Given a string `s`, return the length of the longest substring that lies between two identical characters, excluding those characters themselves.**
>
> If no such substring exists, return **-1**.

---

## 📌 Clarifications (what interviewer expects you to ask)

* Substring is **strictly between two equal characters**
* Do **not include** the matching characters
* If no repeating characters → return **-1**

---

## 🔍 Example

```text
Input:  s = "bderdb"
Output: 4
```

Explanation:

* First `'b'` at index 0
* Last `'b'` at index 5
* Substring = `"derd"` → length = **4**

---

```text
Input:  s = "abcdef"
Output: -1
```

Explanation:

* No repeating characters


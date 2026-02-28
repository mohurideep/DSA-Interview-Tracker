Question 1 — Basic String Sanitization
Problem
Given a string s, return a new string after removing all characters that are not English letters (a–z, A–Z) or digits (0–9).
Function signature

def clean_string(s: str) -> str:
    ...

Example
Input:  "a!b@c#123$%^"
Output: "abc123"


Realistic (What companies actually ask)
Question 2 — Username Validation
Problem
A website only allows usernames containing letters and numbers.
Given a raw username string entered by a user, sanitize it by removing invalid characters.

Input:  "john.doe_1999!!"
Output: "johndoe1999"

What they are testing:
character checks
iteration
string building efficiency

Question 3 — Log Processing (Very common)
Problem
You are given a log message containing timestamps and punctuation.
Normalize the log by keeping only alphanumeric characters.

Input:
"[ERROR] 2025-01-01 10:45:33 -- Connection failed!!!"

Output:
"ERROR20250101104533Connectionfailed"

This tests real-world string cleaning (very common in backend/NLP).
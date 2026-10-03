"""
RECORD CHECK  -  my version
===========================

Name  : Maliha
Lane  :  AI
Date  : 30th september 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label= input("Enter dataset name: ")
rows_loaded = float(input("enter number of rows loaded: "))
rows_expected = float(input("number of rows expected: "))

free = rows_expected- rows_loaded
percent = rows_loaded/rows_expected *100

print("=" * 34)
print(f"         RECORD CHECK - {label}")
print("=" * 34)
print(f"ROWS LOADED   :{rows_loaded:10.2f}")
print(f"ROWS EXPECTED :{rows_expected:10.2f}")
print(f"FREE          :{free:10.2f}")
print(f"PERCENT       :{percent:+10.2f}%")

print("=" * 34)




#3. Filter numeric values from a mixed-type tuple, attempt modification (handle error), and concatenate two tuples.
t = (1, "hello", 3.5, 8, "world", 12)

numeric_values = [i for i in t if isinstance(i, (int, float))]
print("Numeric values:", numeric_values)

try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)

t2 = ("a", "b", "c")
new_tuple = t + t2

print("Concatenated tuple:", new_tuple)
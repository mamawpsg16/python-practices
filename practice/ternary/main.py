# EXAMPLE 1
is_nice = True
# value_if_true if condition else value_if_false
state = "nice" if is_nice else "not nice"
# print(state)

# EXAMPLE 2 - NOT REALLY GOOD TO USE
nice = True
# (if_test_is_false, if_test_is_true)[test]
personality = ("mean", "nice")[nice]
print("The cat is ", personality)

# ShortHand Ternary
print(True or "Some")
print(False or "Some")

output = None
msg = output or "No data returned"
print(msg)
L = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
print("Original List :- ",L)
u_value = set(val for dictionary in L for val in dictionary.values()
)
print("Unique Values :- ",u_value)

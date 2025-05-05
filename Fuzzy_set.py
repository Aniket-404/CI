import numpy as np

# Define fuzzy sets A and B (membership functions for elements)
A = {'x1': 0.8, 'x2': 0.5, 'x3': 0.3}
B = {'x1': 0.6, 'x2': 0.7, 'x3': 0.2}

# Union of A and B
def union(A, B):
    result = {}
    for key in set(A) | set(B):
        result[key] = max(A.get(key, 0), B.get(key, 0))
    return result

# Intersection of A and B
def intersection(A, B):
    result = {}
    for key in set(A) | set(B):
        result[key] = min(A.get(key, 0), B.get(key, 0))
    return result

# Complement of A
def complement(A):
    result = {key: 1 - value for key, value in A.items()}
    return result

# Difference of A and B
def difference(A, B):
    result = {}
    for key in set(A) | set(B):
        result[key] = max(0, A.get(key, 0) - B.get(key, 0))
    return result

# Fuzzy relation creation (Cartesian product of fuzzy sets)
def fuzzy_relation(A, B):
    relation = {}
    for x in A:
        for y in B:
            relation[(x, y)] = min(A[x], B[y])  # Using min for fuzzy relation
    return relation

# Max-min composition of two fuzzy relations
def max_min_composition(R1, R2):
    result = {}
    for (x, z) in R1:
        max_val = 0
        for y in R2:
            max_val = max(max_val, min(R1.get((x, y), 0), R2.get((y, z), 0)))
        result[(x, z)] = max_val
    return result

# Function to print fuzzy sets and relations
def print_fuzzy_set(name, fuzzy_set):
    print(f"{name}:")
    for key, value in fuzzy_set.items():
        print(f"  {key}: {value:.2f}")
    print()

def print_fuzzy_relation(name, relation):
    print(f"{name}:")
    for (x, y), value in relation.items():
        print(f"  ({x}, {y}): {value:.2f}")
    print()

# Example of fuzzy sets A and B
print_fuzzy_set("Fuzzy Set A", A)
print_fuzzy_set("Fuzzy Set B", B)

# 1. Union of A and B
union_result = union(A, B)
print_fuzzy_set("Union of A and B", union_result)

# 2. Intersection of A and B
intersection_result = intersection(A, B)
print_fuzzy_set("Intersection of A and B", intersection_result)

# 3. Complement of A
complement_result = complement(A)
print_fuzzy_set("Complement of A", complement_result)

# 4. Difference of A and B
difference_result = difference(A, B)
print_fuzzy_set("Difference of A and B", difference_result)

# Fuzzy relation between sets A and B
R1 = fuzzy_relation(A, B)
print_fuzzy_relation("Fuzzy Relation R1 (A x B)", R1)

# Example Fuzzy Relation R2 for Max-Min composition
C = {'y1': 0.8, 'y2': 0.5}
R2 = fuzzy_relation(B, C)
print_fuzzy_relation("Fuzzy Relation R2 (B x C)", R2)

# 5. Max-Min Composition of R1 and R2
composition_result = max_min_composition(R1, R2)
print_fuzzy_relation("Max-Min Composition of R1 and R2", composition_result)


P = "It's Saturday afternoon"

# Finding the index of a substring
index_saturday = P.index("Saturday")    # Should return 4
index_afternoon = P.index("afternoon")   # Should return 13
index_not_found = P.index("Monday")     # Raises ValueError 

# To Print the results
print(f"Index of 'Saturday': {index_saturday}")    # Output: 4
print(f"Index of 'afternoon': {index_afternoon}")   # Output: 13

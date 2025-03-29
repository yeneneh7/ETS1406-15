SS = "I have a Lenovo PC"

# Finding the index 
index_have = SS.find("have")    # Should return 2
index_lenovo = SS.find("Lenovo")  # Should return 10
index_not_found = SS.find("Apple") # Should return -1

# If we want to print 
print(f"Index of 'have': {index_have}")      # Output: 2
print(f"Index of 'PC': {index_pc}")          # Output: 16
print(f"Index of 'Apple': {index_not_found}") # Output: -1

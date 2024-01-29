def count_vowels(s):
    if not s:
        return "Error: No input provided."
    
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def string_manipulation(s):
    # Normalize the string to lowercase for consistent comparisons
    s_lower = s.lower()
    
    # Count vowels
    vowels = "aeiou"
    vowel_count = sum(1 for char in s_lower if char in vowels)

    # Reverse the string
    reversed_str = s[::-1]

    # Check for palindrome (ignoring case and spaces)
    cleaned_str = ''.join(c.lower() for c in s if c.isalnum())  # remove spaces and punctuation
    is_palindrome = cleaned_str == cleaned_str[::-1]

    # Print results
    print(f"Original String: {s}")
    print(f"Vowel Count: {vowel_count}")
    print(f"Reversed String: {reversed_str}")
    print(f"Is Palindrome: {'Yes' if is_palindrome else 'No'}")

# Example usage
string_manipulation("A man a plan a canal Panama")

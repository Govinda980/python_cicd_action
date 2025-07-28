
def is_palindrome(s):
    """
    Check if the given string is a palindrome.
    Ignores case and non-alphanumeric characters.
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sample = "A man, a plan, a canal: Panama"
    print(f"'{sample}' is a palindrome? {is_palindrome(sample)}")

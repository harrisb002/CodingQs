# Program Spec: Given two strings str1 and str2 of size m and n
# Write a program to check whether two given strings are anagrams
# Str1 is an anagram of str2 if chars of str1 can be rearranged to form str2
# Both strings may contain duplicate letters
# Chars in both strings are lowercase English chars
# Input: str1 = "dusty"  Input2: = "study"
# Output: True

def check_anagram(str1, str2):
    if len(str1) != len(str2):  # Must be same size for anagram
        return False

    # Create direct address tables for both strings to store counts for characters
    freq_count1 = [0] * 26
    freq_count2 = [0] * 26

    # Using Python ord() function to return the Unicode code from a given character.
    # Note for word "abide":  ord(str1[0]) = 97 (ASCII code for 'a')
    # By subtracting ord('a') (ASCII value for 'a')
    # We begin the address table at index zero containing any occurrences of 'a'
    for i in range(len(str1)):
        freq_count1[ord(str1[i]) - ord('a')] += 1
        freq_count2[ord(str2[i]) - ord('a')] += 1

    for i in range(26):
        if freq_count1[i] != freq_count2[i]:
            return False

    return True

def main():
    str1 = "study"
    str2 = "dusty"
    ans = check_anagram(str1, str2)
    print(ans)


main()
def check_unique(text):
    checked = []
    for char in text:
        if char in checked:
            return False
        else:
            checked.append(char)
    return True

def longest_without_repeat(text):
    longest_val = 0
    longest_str = ''
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            substr = text[i:j]
            if check_unique(substr):
                if (j - i) > longest_val:
                    longest_val = j - i
                    longest_str = substr

    return longest_str

def longest_common_substring(text1, text2):
    longest_common_str = ''
    for i in range(len(text1)):
        for j in range((i+1), len(text1)+1):
            substr = text1[i:j]
            if substr in text2 and len(substr) > len(longest_common_str):
                longest_common_str = substr
    return longest_common_str

if __name__ == "__main__":
    print(longest_without_repeat("geeksforgeeks"))
    print(longest_common_substring("abcdxyz", "xyzabcd"))

def file_read(fname):
    txt = open(fname)
    print(txt.read())
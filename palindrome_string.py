def isPalindrome(str, index):
  middle = int(len(str)/2)
  if index<=middle:
    if str[index]==str[-(index+1)]:
      return isPalindrome(str, index+1)
    else: print("not a palindrome")
  else: print("palindrome")

str=input()
isPalindrome(str,0)

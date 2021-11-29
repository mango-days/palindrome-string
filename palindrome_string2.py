pal_str = "abcba"
for index in range ( 0 , int( len( pal_str )/2 ) ) :
    if pal_str[index] != pal_str[ len(pal_str)-index-1 ] :
        print ("not a palindrome")
        break
    elif index == int( len( pal_str )/2 )-1 :
        print ( "palindrome" )

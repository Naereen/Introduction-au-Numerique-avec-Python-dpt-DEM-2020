def plusGrand( l:list ):
    if l == []:
       return( -1 )
    p = l[0]
    m = plusGrand( l[1:] )
    if m > p:
       return( m )
    return( p )

def main():
    print( plusGrand( [] ) )
    print( plusGrand( [2,3] ) )
    print( plusGrand( [1,6,7,3,9] ))
    return

if __name__ == '__main__': main()
    

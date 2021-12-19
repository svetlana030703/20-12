x, y, z = map( int, input().split())

def f( x, y ):
    if x > y:
        return x
    return y
def m( x, y, z ):
    return f( x, f( y, z ) )

print(m( x, y, z ))

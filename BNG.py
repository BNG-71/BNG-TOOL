import platform
b = platform.architecture()[0]
if b == '64bit':
    import __BNG_71__
elif b == '32bit':
    print("32bit Not Supported! Sorry")

import platform
b = platform.architecture()[0]
if b == '64bit':
    import bngr
elif b == '32bit':
    print("32bit Not Supported! Sorry")

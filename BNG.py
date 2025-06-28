import ctypes
import os

# .so ফাইলের নাম
so_file = "khan.cpython-312.so"

# চেক করি ফাইলটা আছে কিনা
if not os.path.isfile(so_file):
    print(f"[×] {so_file} ফাইল খুঁজে পাওয়া যায়নি!")
    exit()

try:
    # .so ফাইল লোড করা
    lib = ctypes.CDLL(f"./{so_file}")

    # ধরে নিচ্ছি main() নামে একটা ফাংশন আছে
    lib.main()
except Exception as e:
    print(f"[×] .so ফাইল রান করতে সমস্যা: {e}")

import RSA
if __name__ == '__main__':
    while True:
        print("Please input command:")
        print("0) Generate public and private key")
        print("1) Encryption")
        print("2) Decryption")
        print("3) Exit")
        command = input("> ")
        if command == "0":
            print("Generate 1024 bits key...")
            n, p, q, pub_key, pri_key = RSA.KeyGenerator()
            print("N: %X" % n)
            print("p: %X" % p)
            print("q: %X" % q)
            print("Public  key: %X" % pub_key)
            print("Private key: %X" % pri_key)
            print("")
        elif command == "1":
            n   = int(input("Input n(base 16): "), 16)
            key = int(input("Input key(base 16): "), 16)
            message = int(input("Input message(base 16): "), 16)
            print("\nResult: %X\n" % RSA.Encryption(n, key, message))
        elif command == "2":
            n   = int(input("Input n(base 16): "), 16)
            p   = int(input("Input p(base 16): "), 16)
            q   = int(input("Input q(base 16): "), 16)
            key = int(input("Input key(base 16): "), 16)
            message = int(input("Input message(base 16): "), 16)
            print("\nResult: %X\n" % RSA.DecryptionCRT(n, p, q, key, message))
        else:
            break
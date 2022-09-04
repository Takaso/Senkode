import base64, sys;

def key(seed:int=0x80) -> str:
    def gcd(seed:int, b:int) -> int:
        if b == 0:
            return seed;
        return gcd(b, seed%b);
    return gcd(seed, 0xff); 

def encrypt(string:str, seed:int) -> str:
    sex = "".join([chr(ord(x)^seed) for x in list(string)]);
    return base64.b16encode(bytes(sex, encoding="utf-8"));

def decrypt(string:str, seed:int) -> str:
    s = base64.b16decode(string);
    a = "".join([chr(int(ord(i)^seed)) for i in list(str(s))]);
    return a#.split("$")[1];

try:
    if sys.argv[1].startswith("-e") and sys.argv[3].startswith("-k"): print(encrypt(sys.argv[2], key(int(sys.argv[4]))));
    elif sys.argv[1].startswith("-d") and sys.argv[3].startswith("-k"): print(decrypt(sys.argv[2], key(int(sys.argv[4]))));
    else: print("nigger");
except Exception as e:
    print(e);

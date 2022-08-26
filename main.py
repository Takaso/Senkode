import base64;

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
    return a.split("$")[1];
        
print(encrypt("Loja", key(69))); #=>4F6C6962
print(decrypt("4F6C6962", key(69)));

from Crypto.Cipher import DES,AES
from Crypto.Util.Padding import pad, unpad
import time, os

#--------------------------DES Encryption & Decryption------------------------------

def get_des_plaintext():
    with open('des_aes/des_plaintext.txt','rb') as file:
        text=file.read()
        return text

def des_encrypt_decrypt(des_plaintext):
    print("The DES plaintext is:", des_plaintext)

    key_des=os.urandom(8)
    cipher=DES.new(key_des,DES.MODE_ECB)

    des_ciphertext=cipher.encrypt(pad(des_plaintext,DES.block_size))
    print("The Encrypted DES ciphertext is:", des_ciphertext)

    decipher=DES.new(key_des,DES.MODE_ECB)
    des_decrypt_result=unpad(decipher.decrypt(des_ciphertext),DES.block_size)
    print("The Decrypted DES plaintext is:", des_decrypt_result)

    if des_decrypt_result==des_plaintext:
        print("\nThe DES Encryption and Decrytion is successful!")
    

#--------------------------AES Encryption & Decryption------------------------------
        
def get_aes_plaintext():
    with open('des_aes/aes_plaintext.txt','rb') as file:
        text=file.read()
        return text

def aes_encrypt_decrypt(aes_plaintext):
    print("The AES plaintext is:", aes_plaintext)

    key_size=int(input("Select the key size for AES(16, 24, 32):"))
    key_aes=os.urandom(key_size)
    cipher=AES.new(key_aes,AES.MODE_ECB)
    
    aes_ciphertext=cipher.encrypt(pad(aes_plaintext,AES.block_size))
    print("The Encrypted AES ciphertext is:", aes_ciphertext)

    decipher=AES.new(key_aes,AES.MODE_ECB)
    aes_decrypt_result=unpad(decipher.decrypt(aes_ciphertext),AES.block_size)
    print("The Decrypted AES plaintext is:", aes_decrypt_result)

    if aes_decrypt_result==aes_plaintext:
        print("\nThe AES Encryption and Decrytion is successful!")


#--------------------------DES & AES Encryption speed comparison------------------------------

def speed_comparison():
    print(f"\nEncryption Speed Comparison for 1000000 repeats of 128-bit block")

    with open('des_aes/plaintext_128.txt','rb') as file:
        plaintext=file.read()
    
    count=1000000

    des_key=os.urandom(8)
    des_cipher=DES.new(des_key, DES.MODE_ECB)
    start_des=time.time()
    for i in range(count):
        des_cipher.encrypt(plaintext[:8])  
        des_cipher.encrypt(plaintext[8:]) 
    des_time=time.time()-start_des

    aes_key=os.urandom(16)
    aes_cipher=AES.new(aes_key, AES.MODE_ECB)
    start_aes=time.time()
    for i in range(count):
        aes_cipher.encrypt(plaintext)  
    aes_time=time.time()-start_aes

    print("Total time of DES Encryption:",des_time)
    print(f"Total time of AES Encryption:",aes_time)

    aes_time_units=(aes_time/des_time)*100
    print("DES encryption of 128 bits (ie two DES blocks)require 100 time units, AES encryption for same takes:",aes_time_units,"time units")

#--------------------------Main function------------------------------

if __name__ == "__main__":

    des_plaintext=get_des_plaintext()
    des_encrypt_decrypt(des_plaintext);
    print('__'*25,'\n')

    aes_plaintext=get_aes_plaintext()
    aes_encrypt_decrypt(aes_plaintext);
    print('__'*25,'\n')


    speed_comparison()











    




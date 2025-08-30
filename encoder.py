import base64

def encode_base64(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

def decode_base64(encoded_text):
    base64_bytes = encoded_text.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('utf-8')

while True:
    print("\n\t\t\t--- Encoder/Decoder ---\n\t\t\t -- N 3 X 4 R Q U 3 --")
    print("1. Encode ")
    print("2. Decode ")
    print("3. Exit ")

    choice = input("Choose option : ")
    if choice == '1':
        text = input("Enter the your secret to hide the truth by encoding it : ")
        print("Encoded secret is here : ",encode_base64(text))

    elif choice == '2':
        encoded_text = input("Enter your encoded secret to reveal the truth by decoding it : ")
        try : 
            print("Decoded Secret is here : ",decode_base64(encoded_text))
        except Exception as e :
            print("Invalid input!")
        break
    
    elif choice == '3':
        break

    else :
        print("Invalid choice, Try again later")
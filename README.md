# 🔐 Message Encryption and Decryption Tool

This is a simple yet creative **Message Encryption and Decryption** tool built using Python. It allows users to **encrypt** and **decrypt** messages using a custom algorithm that adds randomness and character transformations to obscure the original message.

## 📌 Features

- Encrypt any text message using custom random-letter encoding
- Decrypt messages back to the original form
- Handles short, medium, and long words differently for added complexity
- Text-based user interface using terminal input

## 🧠 Logic Overview

### 🔒 Encryption
- For words with:
  - **5 or more characters**: adds random letters before and after, reorders internal characters
  - **3-4 characters**: similar logic with slightly less transformation
  - **Less than 3 characters**: simply reversed
- Uses `random` and `string` modules to generate disguising characters

### 🔓 Decryption
- Reverses the logic based on word length
- Restores original message using position-based decoding
- Simple reverse for words shorter than 9 characters

## 🧪 Example

**Input (to encrypt):**
Hello world

**Encrypted:**
MemlolHeKRh TpAldrWoBQK

**Decrypted:**
Hello World

> The actual encrypted output will vary each time because of the random characters added during encryption.

## 💻 How to Run

1. Make sure Python is installed on your machine (Python 3.x recommended).
2. Clone the repository or download the script.

```bash
git clone https://github.com/sadain-ahmad/Message-Encryption.git
cd Message-Encryption
```
3. **Run the script:**

python Message-Encryption.py

4. **Follow the prompts to either encrypt or decrypt a message.**

## 📚 Concepts Used:
- Python basics: variables, loops, conditionals

- String manipulation

- Random character generation (random, string)

- Input/output handling

## 👨‍💻 Author
### Sadain Ahmad
GitHub: https://github.com/sadain-ahmad
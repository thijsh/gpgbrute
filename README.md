# GPGbrute
GPG passphrase brute forcing script intended to help recover the passphrase of your private key.

## Description
This script is most useful when you have chosen a passphrase loosely based on [XKCD Password Strength](https://xkcd.com/936/).
A full search of all possible combinations of words is not feasible, if you however remember the set of words that could possibly have been used you can recover the passphrase in a short enough time. Never lose control over a private key anymore when your mind holds the pieces of the puzzle you have created for yourself! ;)

## Usage
- Edit the *'gpgbrute.py'* file.
- Enter an encrypted input file that you failed to decode.
- When there are known prefixes that could have been used enter them all, otherwise only leave *''*.
- Braindump all the words that you can think of in the context of this private key.
- Add a list of separators, if you know for sure all words are seperated by space alone only leave *' '*.
- Run the script and make some coffee, when the list is not too long your password will be found before you finish your coffee!


# LMCracker
A simple Python script that checks LM hashes on cracker.offensive-security.com. It's a lot faster than john. :-D

## Usage:

1.) Create a list of LM hashes e.g.: lm_hashes.txt

``` 1b16d18d7bnb96db1aa818381e4e281a ```

``` 2b16d18d7bnb96db1aa818381e4e281a ```

``` 3b16d18d7bnb96db1aa818381e4e281a ```

2.) Edit crack.py and insert your priority code (you'll find it in your lab panel).

3.) Start cracking!

python crack.py lm_hashes.txt

Hashes that are not known will be inserted in the cracking queue, just come back later then.

Problems:

Implement a character-scanning tokenizer. Group each consecutive run of ASCII letters, digits, or underscores into one token. Discard whitespace and emit every other character as its own token. Preserve the original case and token order; an empty or whitespace-only string produces an empty list.

Return a Python list of token strings.





**Breakdown:**
### Step 1: Initialize two variables

- tokens: An empty list to store completed tokens.
- current: An empty string to build the current token.
### Step 2: Scan each character

- Use a loop to go through the input string one character at a time, from left to right.
### Step 3: Check if the character is valid

- Check whether the character is an ASCII letter (A–Z, a–z), digit (0–9), or underscore (_).
- If yes, add it to `current`.
- Keep building `current` as long as the characters are valid.
### Step 4: Handle invalid characters

When a character is not a letter, digit, or underscore:

- Check whether `current` is not empty.
- If it contains something, append it to `tokens`.
- Reset `current` to an empty string.

This process is called flushing the current token.
### Step 5: Handle whitespace and punctuation

- Whitespace: Skip it and move to the next character.
- Punctuation or other symbols: Add each character as its own token.
- Never include whitespace in the output.
### Step 6: Handle the last token

- After the loop finishes, check whether `current` still contains characters.
- If it does, append it to `tokens`.
- This prevents losing the last word when the string ends with a valid character.
### Step 7: Return the result

- Return the list containing all completed tokens in their original order and case.
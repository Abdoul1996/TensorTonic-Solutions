Problem:

Implement a deterministic word-level tokenizer used as preparation for the Transformer exercises. This is a simplified tokenizer, not the subword system used in the original paper.

build_vocab must assign IDs 0 through 3 to PAD, UNK, BOS, and EOS, then assign IDs to lowercased training words in sorted order. encode lowercases and whitespace-splits text, using UNK for unseen words. decode maps IDs back to tokens, using UNK for unknown IDs. Return a list of integer IDs from encode and a space-separated string from decode.



Break down:

1. build_vocab function

1. lowercase text
2. split on whitespace
3. collect unique words
4. sort the words
5.
2. encode word to id 

1. text sorted
2. call spacial tokens and copy
3. create empty dict word_to_id 

1. word_to_id[w] = i + 4
2. return word_to_id
3. decode id to word

1. create empty dict id_to_word
2. reverse the ids to words
3. return id_to_word
class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        """
        # Initialize special tokens 
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token] = 1 
        self.word_to_id[self.bos_token] = 2
        self.word_to_id[self.eos_token] = 3
      
        # step 2:  Lowercase, split, and remove duplicates, sort 
        lower_texts = []
        for text in texts:
          lower_texts.append(text.lower())

        split_words = []
        for word in lower_texts:
          split_words.extend(word.split())
          
        unique_words = list(set(split_words))
        sort_words = sorted(unique_words)

        # step 3: asssigned ID to words 
        for index, word in enumerate(sort_words):
          self.word_to_id[word] = index + 4
          
        # step 4: reversing ID TO WORDs 
        for word, token_id in self.word_to_id.items():
          self.id_to_word[token_id] = word

        # step 5: Update the size vocabulary 
        self.vocab_size = len(self.word_to_id)
        
      

    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        lower_text = text.lower()
        split_text = lower_text.split()
        word_id = []

        for word in split_text:
          if word in self.word_to_id:
            word_id.append(self.word_to_id[word])
          else:
            word_id.append(self.word_to_id[self.unk_token])
        return word_id
        

    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        id_to_words = []
      
        for id in ids:
          if id in self.id_to_word:
            id_to_words.append(self.id_to_word[id])
          else:
            id_to_words.append(self.id_to_word[1])
        text = " ".join(id_to_words)
        return text 
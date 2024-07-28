class WordsFinder:
    def __init__(self,  * file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = file.read().lower()
                for i in ['', ',', '.', '=', '!', '?', ';', ':', ' - ']:
                    data = data.replace(i, '')
                    all_words[file_name] = data.split()
        return all_words

    def find(self, word):
        word_find = {}
        for name, words in self.all_words.items():
            word = word.lower()
            words = list(map(str.lower, words))
            if word in words:
                word_find[name] = words.index(word) + 1
        return word_find

    def count(self, word):
        word_count = {}
        count = 0
        for name, words in self.all_words.items():
            word = word.lower()
            words = list(map(str.lower, words))
            for i in words:
                if i == word:
                    count += 1
                word_count[name] = count
        return word_count
















finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
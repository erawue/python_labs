import sys
import os
# путь к папке lib
current_dir = os.path.dirname(__file__)
lib_path = os.path.join(current_dir, '..', '..', 'lib')
sys.path.append(lib_path)
from text import normalize, top_n, tokenize, count_freq
text = sys.stdin.read()
words = tokenize(normalize(text))
freq = count_freq(words)
top = top_n(freq, 5)
print(f'Всего слов: {len(words)}')
print(f'Уникальных слов: {len(freq)}')
print('Топ-5:')
for word, count in top:
    print(f'{word}:{count}')
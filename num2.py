user_input = input("Введите строку: ")
words = user_input.split()
even_length_count = 0
longest_word = ''
for word in words:
    if len(word) % 2 == 0:
        even_length_count += 1
    if len(word) > len(longest_word):
        longest_word = word
print("Количество слов с четной длиной:", even_length_count)
print("Самое длинное слово:", longest_word)

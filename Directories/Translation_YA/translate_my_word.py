from directories.translation_YA.translation import get_translate

print(*get_translate(input(">"), 'en-ru')['text'])

"""
Напечатайте на экран:
- Количество любимых песен Димы (только число).
- Все любимые песни Сони, построчно.
"""

favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'], 
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'], 
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
}

print(len(favorite_songs['Дима']))
for song in favorite_songs['Соня']:
    print(song)

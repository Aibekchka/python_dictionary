cities = [
    'Алматы',
    'Астана',
    'Шымкент',
    'Актобе',
    'Караганда',
    'Тараз',
    'Павлодар',
    'Семей',
    'Астана',
    'Кызылорда',
    'Шымкент',
    'Актау',
    'Астана',
    'Петропавловск',
    'Алматы',
]



friends = {
    'Сергей': 'Павлодар',
    'Айбек': 'Атырау',
    'Дамир': 'Астана'
}
friends['Сергей'] = 'Астана'
print(friends['Сергей'])

friends = {
    'Сергей': 'Павлодар',
    'Айбек': 'Атырау',
    'Дамир': 'Астана',
    'Рустем': 'Алматы',
    'Максим': 'Кокшетау',
    'Амир': 'Алматы',
    'Азат': 'Уральск',
    'Руслан': 'Астана'
}
for i in set(friends.values()):
    print(i)


dictionary = {
    'a': 50,
    'b': 20,
    'c': 13.2,
    'd': 70
}
print(dictionary)
sozder = dictionary.values()
print(sum(sozder))

friends = {
    'Сергей': 'Павлодар',
    'Айбек': 'Атырау',
    'Дамир': 'Астана',
    'Асылбек': 'Шымкент',
    'Самат': 'Ташкент'
}
print(friends)


friends = {
    'Сергей': 'Павлодар',
    'Айбек': 'Атырау',
    'Дамир': 'Астана',
    'Асылбек': 'Шымкент',
    'Самат': 'Ташкент'
}
new_friends = {
    'Амир': 'Алматы',
    'Азат': 'Уральск',
    'Руслан': 'Астана'
}

friends.update(new_friends)
print(friends)

friends_names = ['Сергей', 'Айбек', 'Дамир', 'Рустем', 'Максим']
friends_cities = ['Павлодар', 'Атырау', 'Астана', 'Алматы', 'Кокшетау']

friends = {}

for i in range(len(friends_names)):
    name = friends_names[i]
    city = friends_cities[i]
    friends[name] = city
print(friends)

#Үй тапсырмасы

friends = {
    'Сергей': 'Павлодар',
    'Айбек': 'Атырау',
    'Дамир': 'Астана',
    'Рустем': 'Алматы',
    'Максим': 'Кокшетау',
    'Амир': 'Алматы',
    'Азат': 'Уральск',
    'Руслан': 'Астана'
}
for name,gorod in zip(friends, friends.values()):
    print(name,'живёт в городе',gorod)


favorite_songs = {
    'Сергей': ['Karma Police', 'Reptilia', 'No Surprises'],
    'Дамир': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
    'Рустем': ['Владимирский централ', 'Той жыры', 'Аяулым']
}

print('Дамирдың сүйікті әндерінің саны',len(favorite_songs))
favorite_songs.pop('Сергей')
favorite_songs.pop('Дамир')
for music in favorite_songs.values():
    print('Рүстемнің сүйікті әндері',music)


playlist = {
    'Venus As a Boy',
    'Yesterday',
    'Comfortably Numb',
    'Time After Time',
}
new_music = [
    'Stairway to Heaven',
    'Wish You Were Here',
    'Bohemian Rhapsody',
    'Let It Be',
]

playlist.update(new_music)
print(playlist)


def is_anyone_in(collection, city):
    for friend in city:
        if collection > friend:
            print('в городе',city,'меня есть друг, но мне туда не надо')
        else:
            print('в городе живет',collection,'Обизательно зайду в гость!')

is_anyone_in(friends, 'Алматы')
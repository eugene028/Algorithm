my_day = "My day First, I wake up. Then, I get dressed. I walk to school. " \
         "I do not ride a bike. I do not ride the bus. I like to go to school. " \
         "It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple. " \
         "I play outside. I like to play. I read a book. I like to read books. " \
         " walk home. I do not like walking home. My mother cooks soup for dinner. " \
         "The soup is hot. Then, I go to bed. I do not like to go to bed."

my_day = my_day.replace(",","")
my_day = my_day.replace(".","")

my_day = my_day.lower()
word_list = my_day.split()

my_day = set(word_list)
my_day1 = list(my_day)
my_day2 = list(my_day)
my_day3 = list(my_day)

down1 = sorted(my_day1, reverse=True)
my_day3.sort(reverse =True)

print(down1)
print("다음 문제")
print(my_day2[::])
print("반대로 출력")
print(my_day2[::-1])
print("다음 문제")
print(my_day3)
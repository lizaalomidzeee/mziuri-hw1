#  task1 ში დაწერეთ ფუნქცია, რომელიც მიიღებს სიტყვას და დააბრუნებს იგივე სიტყვას, ოღონდ ხმოვანი ასოები (a, e, i, o, u) იქნება დიდი.. მაგალითად hello -> hEllO , aabbgg -> AAbbgg   
def capitalize_vowels(word):
    vowels = 'aeiou'
    result = ' '
    for i in word:
        if i in vowels:
            result += i.capitalize()
        else:
            result += i
    return result

print(capitalize_vowels("mziuri"))
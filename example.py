from source.script import path_shortener

my_path = "~/here/is/my/file/text.txt"
my_shortened_path = path_shortener(my_path)

print(f"{my_path} --> {my_shortened_path}")
print("Look at that. So much simpler and prettier.")

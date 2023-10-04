# print("what is your name")
name = input("what is your name? ")
print("hello" , name);

#  single = sign is assignment operator


# end and separator in the python
print("hello," , end="")
print(name);

# use of sep
# this separate the line into two
# we can add the string inside it
print("hello," , name , sep="???")

#4 -- Names sep parameter
# this is the another way to write the string
print(f"hello , {name}");


#5 -- str (strings)

# 1) Remove white space from the string method
# strip is the function
name = name.strip();
print(f"Hello {name}")

# 2) Capitalize user's name
# it only capitalize only first letter of the name
# there both are the same
name = name.capitalize();
name = name.title();
print(f"Hello {name}")

# remove whitespace and capitalize it
# there both are the function 
name = name.strip().title();


# 3) 
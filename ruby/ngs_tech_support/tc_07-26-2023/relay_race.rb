# Create a method that determines the missing number from the following:
# [2, 1, 5, 4, 6, 9, 7, 8, 10], return the missing num

list = [2, 1, 5, 4, 6, 9, 7, 8, 10]



def missing_num(collection=[])
  collection.sort.each_with_index do |num, i|
    if num != i + 1
      return i + 1
    end
  end
end

#Create a method that uses the missing number as an argument,
#then returns the number as a string
#like 1 => one

numbers = {
  1 => 'One',
  2 => 'Two',
  3 => 'Three',
  4 => 'Four',
  5 => 'Five',
  6 => 'Six',
  7 => 'Seven',
  8 => 'Eight',
  9 => 'Nine',
  10 => 'Ten'
}

def missing_num_as_string(missing_num, numbers)
  numbers[missing_num]
end

# Create a method with the string as an arg that returns only
# the vowels in the string

# Split word into letters array, downcase
# Create empty array of vowels
# iterate through split word array, if vowel shovel into new array
# combine array
# return new array

def vowels(number_as_word)
  split_word = number_as_word.downcase.split("")
  all_vowels = ["a", "e", "i", "o", "u"]
  split_word.find_all { |l| all_vowels.include?(l) }
end

number_as_word = missing_num_as_string(missing_num(list), numbers)
p vowels(number_as_word)



require 'prime'

def prime(arr)
  prime_numbers = []
  arr.each do |a|
    if a.prime?
      prime_numbers << a
    end
  end
  prime_numbers
end

# with each i we add the previous element to it

def fibbonacci_sequence(prime)
  sorted = prime.sort
  output = 0

  sorted.each do |e|
    output += e
  end

  output
end

arr = [10, 34, 8, 44, 31, 3, 27, 48, 56, 57, 50, 26, 36, 64, 55, 14, 40, 63, 54, 11]

p fibbonacci_sequence(prime(arr))

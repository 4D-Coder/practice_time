
def staircase(n)
  collection = ""
  counter = n
  # Take in the integer and print to the termanal n times
  n.times do
      collection.concat("#")
      justified = collection.rjust(n)

      puts justified
  end
end

staircase(6)
# =>
# "     #"
# "    ##"
# "   ###"
# "  ####"
# " #####"
# "######"

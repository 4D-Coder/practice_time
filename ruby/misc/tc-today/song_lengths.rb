# Given a set of song lengths, count the number of pairs of songs that sum to 60:
# Example:
# output = 2

songs = [20, 40, 60, 20]

def count_pairs(songs)
  count = 0
  songs.each_with_index do |s, i|
    e = songs.length - i
    # => 4 3 2 1
    c = 1
    e.times do
      if songs[i + c] == nil
        break
      end
      
      if s + songs[i + c] == 60
        count += 1
      end
      c += 1
    end
  end
  count
end

p count_pairs(songs)

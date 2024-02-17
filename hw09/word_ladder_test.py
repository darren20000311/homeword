from word_ladder import WordLadder


# # TODO: Write appropriate unit tests

# def test_make_ladder():
#     assert False

def test_make_ladder():

  wordlist = {"cat", "hat", "bat"}

  wl = WordLadder("cat", "hat", wordlist)

  ladder = wl.make_ladder()

  assert ladder.peek() == "hat" 
  assert ladder.size() == 2
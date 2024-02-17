from NgramFrequencies import NgramFrequency

def test_add_item():
    nf = NgramFrequency("the", 1)
    nf.add_item("the")
    assert nf.word_counts["the"] == 1

def test_top_n_counts():  
    nf = NgramFrequency("the", 1)
    nf.add_item("the")
    assert nf.top_n_counts() == [("the", 1)]
  
def test_top_n_freqs():
    nf = NgramFrequency("text", 1)  
    nf.add_item("the")
    assert nf.top_n_freqs() == [("the", 0.25)]
  
def test_frequency():
    nf = NgramFrequency("the", 1)
    nf.add_item("the")  
    assert nf.frequency("the") == 1
  
test_add_item()
test_top_n_counts()
test_top_n_freqs() 
test_frequency()
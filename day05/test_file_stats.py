from file_stats import count_nucleotides

def test_counter():
    res = count_nucleotides("test_seq.txt")
    assert res == '''A: 4 (33.33%)
T: 3 (25.00%)
C: 3 (25.00%)
G: 2 (16.67%)
Low GC content
'''
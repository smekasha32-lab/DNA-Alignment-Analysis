from re import match


def compare_sequences(seq1, seq2):
    matches = 0
    mismatches = 0
    mismatch_positions = []

    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] == seq2[i]:
            matches += 1
        else:
            mismatches += 1
            mismatch_positions.append((i, seq1[i], seq2[i]))
    return matches, mismatches, mismatch_positions

def calculate_alignment_score(matches, mismatches, match_score=1, mismatch_penalty=-1):
    return (matches * match_score) + (mismatches * mismatch_penalty)

def similarity_percentage(matches, mismatches):
    total_positions = matches + mismatches
    if total_positions == 0:
        return 0.0
    return (matches / total_positions) * 100

def main():
    seq1 = "ATGAATCG"
    seq2 = "ATGCGTCGTCG"
    matches, mismatches, mismatch_positions = compare_sequences(seq1, seq2)
    
    print("\n=== Sequences ===")
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    
    print("\n=== Sequence Alignment Report ===")
    print(f"Matches: {matches}")
    print(f"Mismatches: {mismatches}")
    alignment_score = calculate_alignment_score(matches, mismatches)
    print(f"Alignment Score: {alignment_score}")
    similarity = similarity_percentage(matches, mismatches)
    print(f"Similarity: {similarity:.2f}%")    
    
    print("\n=== Mismatch Details ===")
    for pos, base1, base2 in mismatch_positions:
        print(f"Position {pos}: {base1} -> {base2}")



if __name__ == "__main__":
    main()
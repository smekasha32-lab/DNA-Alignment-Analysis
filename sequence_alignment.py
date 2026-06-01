def compare_sequences(seq1, seq2):
    match = 0
    mismatch = 0
    mismatch_positions = []

    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] == seq2[i]:
            match += 1
        else:
            mismatch += 1
            mismatch_positions.append((i, seq1[i], seq2[i]))
    return match, mismatch, mismatch_positions

def main():
    seq1 = "ATGAATCG"
    seq2 = "ATGCGTCGTCG"

    match, mismatch, mismatch_positions = compare_sequences(seq1, seq2)
    print(f"Match: {match}")
    print(f"Mismatch: {mismatch}")
    print("\n--- Mismatch Details ---")

    for pos, base1, base2 in mismatch_positions:
        print(f"Position: {pos}, {base1} -> {base2}")

    total_positions = match + mismatch
    similarity_percentage = (match / total_positions) * 100 if total_positions > 0 else 0
    print(f"Similarity: {similarity_percentage:.2f}%")

if __name__ == "__main__":
    main()
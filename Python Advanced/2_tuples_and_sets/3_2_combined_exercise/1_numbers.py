def add(seq, new_seq):
    seq = seq.union(new_seq)
    return seq

def remove(seq, new_seq):
    seq = seq.difference(new_seq)
    return seq

def check(seq1, seq2):
    print(set(seq1).issubset(seq2) or set(seq2).issubset(seq1))


first_seq = set([int(x) for x in input().split()])
second_seq = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    command, set_type, *nums = input().split()
    nums = [int(x) for x in nums]
    if command == "Add":
        if set_type == "First":
            first_seq = add(first_seq, nums)
        elif set_type == "Second":
            second_seq = add(second_seq, nums)

    elif command == "Remove":
        if set_type == "First":
            first_seq = remove(first_seq, nums)
        elif set_type == "Second":
            second_seq = remove(second_seq, nums)

    elif command == "Check":
        check(first_seq, second_seq)

print(", ".join(([str(x) for x in sorted(first_seq)])))
print(", ".join(([str(x) for x in sorted(second_seq)])))
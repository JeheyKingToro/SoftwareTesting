# test_metamorphic.py
import quick_sort

def check_equal(list1, list2):
    """Helper function to check if two lists are identical."""
    return list1 == list2

def test_mr1():
    """
    MR1: Reversing the input list should not change the sorted output.
    """
    print("=== MR1: Reversing input ===\n")
    test_groups = [
        [4, 2, 5, 1],
        [9, 8, 7, 6],
        [10, 1, 3, 2, 5],
        [100, 50, 200, 25],
        [3, 3, 2, 1]
    ]

    for i, source in enumerate(test_groups, start=1):
        followup = list(reversed(source))
        src_out = quick_sort.quick_sort(source)
        follow_out = quick_sort.quick_sort(followup)
        result = check_equal(src_out, follow_out)

        print(f"Test Group {i}")
        print(f"Original:      {source}")
        print(f"Reversed:      {followup}")
        print(f"Sorted Output: {src_out}")
        print(f"Sorted Reversed: {follow_out}")
        print(f"Result: {'PASS' if result else 'FAIL'}\n")

def test_mr2():
    """
    MR2: Adding a constant to each element should preserve relative order.
    (i.e., the order of elements in sorted output should remain consistent)
    """
    print("=== MR2: Adding a constant ===\n")
    test_groups = [
        ([3, 1, 2], 5),
        ([10, 5, 15, 0], 10),
        ([7, 3, 9], 2),
        ([100, 50, 200, 150], -50),
        ([1, 1, 2, 3], 100)
    ]

    for i, (source, c) in enumerate(test_groups, start=1):
        followup = [x + c for x in source]
        src_sorted = quick_sort.quick_sort(source)
        follow_sorted = quick_sort.quick_sort(followup)

        # Compare the relative ordering (using ranks)
        src_ranks = [source.index(x) for x in src_sorted]
        follow_ranks = [followup.index(x) for x in follow_sorted]
        result = src_ranks == follow_ranks

        print(f"Test Group {i}")
        print(f"Original:         {source}")
        print(f"Shifted (+{c}):    {followup}")
        print(f"Sorted Original:  {src_sorted}")
        print(f"Sorted Shifted:   {follow_sorted}")
        print(f"Relative Ranks Match: {result}")
        print(f"Result: {'PASS' if result else 'FAIL'}\n")


if __name__ == "__main__":
    print("Running Metamorphic Tests for quick_sort.py\n")
    test_mr1()
    test_mr2()

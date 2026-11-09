def solution(A):
    N = len(A)

    # Get the total once, so the right side can be worked out
    # without re-adding it every time (that would be too slow)
    total = 0
    for x in A:
        total = total + x

    left = 0
    # -1 means "no answer yet". It's safe because a real difference is never negative.
    best = -1

    # P is where the tape is cut. P starts at 1 and stops before N,
    # so both sides always have at least one number.
    for P in range(1, N):
        # Moving the cut right adds one more number to the left side
        left = left + A[P - 1]

        # Whatever isn't on the left is on the right
        right = total - left

        # Absolute value by hand: if the difference is negative, flip its sign
        diff = left - right
        if diff < 0:
            diff = -diff

        # Keep the smallest difference seen so far
        # (or take the first one if there's nothing yet)
        if best == -1 or diff < best:
            best = diff

    return best
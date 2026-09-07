from collections import Counter


class Solution:

  def lexGreaterPermutation(self, s: str, target: str) -> str:
    n = len(s)
    counts = Counter(s)

    # Try matching target up to length prefix_len, starting from longest to shortest
    for prefix_len in range(n - 1, -1, -1):
      prefix_counts = Counter(target[:prefix_len])
      if any(prefix_counts[c] > counts[c] for c in prefix_counts):
        continue

      rem_counts = counts - prefix_counts
      target_char = target[prefix_len]
      candidates = sorted([c for c in rem_counts if c > target_char])

      if candidates:
        chosen_char = candidates[0]
        rem_counts[chosen_char] -= 1

        suffix = "".join(
            c * rem_counts[c] for c in sorted(rem_counts.keys())
        )
        return target[:prefix_len] + chosen_char + suffix

    return ""
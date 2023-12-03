
def count_batteries_by_health(present_capacities):
  counts={
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  # Constants
  rated_capacity = 120  # Rated capacity of a new battery in Ah

  # Function to calculate SoH%
  def calculate_soh(present_capacity):
      return (present_capacity / rated_capacity) * 100

  # Classify batteries based on SoH and update counts
  for present_capacity in present_capacities:
      soh = calculate_soh(present_capacity)

      if soh > 80:
          counts["healthy"] += 1
      elif 62 <= soh <= 80:
          counts["exchange"] += 1
      else:
          counts["failed"] += 1

  return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  # Test Case 1
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)

  # Test Case 2: All healthy batteries
  present_capacities = [110, 115, 120, 118, 105]
  counts = count_batteries_by_health(present_capacities)
  assert counts["healthy"] == 5
  assert counts["exchange"] == 0
  assert counts["failed"] == 0

  # Test Case 3: All failed batteries
  present_capacities = [50, 45, 55, 40, 30]
  counts = count_batteries_by_health(present_capacities)
  assert counts["healthy"] == 0
  assert counts["exchange"] == 0
  assert counts["failed"] == 5

  # Test Case 4: Mix of healthy, exchange, and failed
  present_capacities = [90, 75, 82, 105, 62, 78, 55]
  counts = count_batteries_by_health(present_capacities)
  assert counts["healthy"] == 1
  assert counts["exchange"] == 4
  assert counts["failed"] == 2

  # Test Case 5: Minimum present capacity (edge case)
  present_capacities = [0, 10, 20]
  counts = count_batteries_by_health(present_capacities)
  assert counts["healthy"] == 0
  assert counts["exchange"] == 0
  assert counts["failed"] == 3

  # Test Case 6: Maximum present capacity (edge case)
  present_capacities = [120, 119, 120, 118, 119]
  counts = count_batteries_by_health(present_capacities)
  assert counts["healthy"] == 5
  assert counts["exchange"] == 0
  assert counts["failed"] == 0

  # Test Case 7: All batteries at the SoH boundary (80%)
  present_capacities = [96, 100, 84, 80, 82]
  counts = count_batteries_by_health(present_capacities)
  assert counts["healthy"] == 1
  assert counts["exchange"] == 4
  assert counts["failed"] == 0

  print("All assertions passed. Done counting :")

if __name__ == '__main__':
  test_bucketing_by_health()

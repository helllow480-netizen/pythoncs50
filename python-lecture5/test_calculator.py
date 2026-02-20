from calculator import square

def main():
  test_square()


def test_square():
  try:
    assert square(2) == 4
  except AssertionError:
      print("2 squared was not 4")
  try:
      assert square(3) == 9
      print("3 squared was 9")
  except AssertionError:
      print("3 squared was not 9")
  try:
      assert square(-2) == 4
      print("-2 squared was 4")
  except AssertionError:
      print("-2 squared was not 4")
  try:
     assert square(-3) == 9
     print("-3 squared was 9")
  except AssertionError:
      print("-3 squared was not 9")
  try:
      assert square(0) == 0
      print("0 squared was 0")
  except AssertionError:
      print("0 squared was not 0")



if __name__ == "__main__":
  main()
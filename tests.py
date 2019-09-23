import unittest
import utils
import asyncio

def _run_async(coroutine):
  """Helper method for running async methods
  
  Arguments:
      coroutine {coroutine} -- The async method
  
  Returns:
      any -- The coroutine's returned data
  """
  return asyncio.get_event_loop().run_until_complete(coroutine)

class TestControllers(unittest.TestCase):
  """Tests the bot utils methods in utils.py
  """
  def setUp(self):
    self.intro = utils.rand_intro()
    self.comment = utils.rand_leonflix_comment()
  
  def test_fetch_meme(self):
    """Tests that the fetched meme has a getvalue method and returns a value len > 10
    """
    self.assertGreater(len(_run_async(utils.fetch_meme()).getvalue()), 10)
  
  def test_rand_intro(self):
    """Tests that the intro string is not empty
    """
    self.assertGreater(len(self.intro), 0)

  def test_rand_comment(self):
    """Tests that the comment string is not empty
    """
    self.assertGreater(len(self.comment), 0)


if __name__ == "__main__":
  unittest.main()
  
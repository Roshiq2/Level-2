import threading
import queue

def ros(timeout=10):
  result_queue = queue.Queue()

  def input_target():
    result_queue.put(input('Enter your input: '))

  thread = threading.Thread(target=input_target)
  thread.start()

  try:
    return result_queue.get(timeout=timeout)
  except queue.Empty:
    return ""

# Example usage
ros()
if user_input:
  print("You entered:", user_input)
else:
  print("No input received. Proceeding...")
  

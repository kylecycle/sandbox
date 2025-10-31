import json
from sql_factory import SqlFactory
import debugpy

# Start the debugger listener on 0.0.0.0:5678
debugpy.listen(("0.0.0.0", 5678))
print(" Debugger is listening on port 5678...")

# Uncomment this to pause until debugger is attached
# debugpy.wait_for_client()

raw = '''
[
  { "name": "foo", \
    "type": "bar", \
    "params": {"p1": "this", "p2": "that"}},
  { "name": "food", \
    "type": "barb", \
    "params": {"pp1": "Mike", "pp2": "Dave", "pp3": [1,5,30]}}
]
'''

items = json.loads(raw)

for item in items:
    processor = SqlFactory.get_processor(item["type"])
    processor.process(item["name"], item["params"])

# if __name__ == "__main__":
#     main()

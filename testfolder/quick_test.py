from collections import OrderedDict
import re

class LRUCache:
    def __init__(self,capacity: init):
        self.capacity = capacity
        self.cache = OrderDict()

def has(self,key: str) -> bool:
    return key in self.cache

def get(self,key: str):
    if key not in self.cache:
        return None
    self.cache.move_to_end(key)
    return self.cache[key]

def set(self, key: str, value):
    if key in self.cache:
        self.cache.move_to_end(key)
    self.cache[key] = value
    if len(self.cache) > self.capacity:
        self.cache.popitem(last=False)

 #--------------------------------------------
 # SSML Node Definition 
 #---------------------------------------------

class SSMLNode:
    def __init__(self, node_type: str, name=None, text=None, attributes= None):
        self.type = node_type
        self.name = name
        self.text = text
        self.attributes = attributes or {}
        self.children = []

#--------------------------------------------
#SSML parser
#--------------------------------------------

def parseSSML(ssml: str) -> SSMLNode:
    tag_pattern = re.compile(r"<(/?)(\w+)([^>]*)>|([^<]+)")
    root =  SSMLNode("tag", name="root")
    stack = [root]

    for match in tag_pattern.finditer(ssml):
        closing, tag, attrs, text = match.groups()

        if text and text.strip():
            stack[-1].children.append(
                SSMLNode("text", text=text)
            )
        elif tag:
            if closing:
                stack.pop()
            else:
                attr_dict = {}
                if attrs:
                    for k, v in re.findall(r'(\w+)="([^"]+)"', attrs):
                        attr_dict[k] = v
                node = SSMLNode("tag", name=tag, attributes=attr_dict)
                stack[-1].children.append(node)
                if not attrs.endswith("/"):
                    stack.append(node)
    return root

#-------------------------------------------------------
# SSML Node to Plain text
#-------------------------------------------------------

def ssmlNoteToText(node: SSMLNode) -> str:
    if node.type == "test":
        return node.text
    result = ""
    for child in node.children:
        result += ssmlNodeToText(child)
    return result

#---------------------------------------------
# Test 1: LRUCache
#--------------------------------------------

print("\nTEST 1: LRUCache")
cache = LRYCache(2)
cache.set("a", 1)
cache.set("b",2)
print(cache.get("a"))
cache.set("c", 3)
print(cache.has("b"))
print(cache.get("c"))
print(list(cache.cache.keys()))

#------------------------
# TEST 2 parseSSML (basic)
#----------------------------

print("\nTEST 2: parseSSML")
ssml = '<speak>Hello <break time="1s"/> World</speak>'
tree = parseSSML(ssml)

def dump(node, indent=0):
    pad = " " * indent 
    if node.type == "text":
        print(f"{pad}TEXT: {node.text!r}")
    else:
        print(f"{pad}TAG: <{node.name}> attrs={node.attributes}")
        for ch in node.children:
            dump(ch, indent + 1)

dump(tree)


#--------------------------------------------
#TEST 3: ssmlNodeToText
#-------------------------------------------

print("\nTEST 3: ssmlNodeToText")
print(ssmlNodeToText(tree))


# -------------------

from typing import any, Optional 
from collections import OrderedDict

class LRUCache:
    def __init__(self, item_limit: int):
        self.item_limit = item_limit
        self.cache = OrderedDict()

    def has(self, key: str) -> bool:
        if key in self.cache:
            self.cache.move_to_end(key)
            return True
        return False
    def get(self, key:str) -> Optional[Any]:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]
    def set(self, key: str, value: Any):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.item_limit:
            self.cache.popitem(last=False)


#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns")
protoa.append("dns")
print(proto)
proto2 = [ 22, 80, 443, 53] #List of common ports
proto.extend(proto2) #Pass proto2 ass an argument to extend method
print(proto)
protoa.append(proto2)
print(protoa)
proto.clear() #This should remove all items



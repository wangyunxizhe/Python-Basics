from redis import Redis

rc = Redis(host="192.168.68.131", port=6379, db=0)
rc.set("name", "wyuan")
name = rc.get("name")
print(name)
rc.delete("name")

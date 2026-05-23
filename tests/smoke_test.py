from leher import hello

message = hello()
if message == "Hello from leher!":
    print("Smoke test succeeded")
else:
    raise RuntimeError(message)

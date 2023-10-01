import requests

def get_stream(query: str):
    s = requests.Session()
    with s.post(
        "http://localhost:8000/chat",
        stream=True,
        json={"text": query}
    ) as r:
        for line in r.iter_content():
            print(line.decode("utf-8"), end="")



get_stream("Tell me a long story about how are you feeling")
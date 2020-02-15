
class Endpoint:

    def __init__(self, id, latency):
        self.id = id
        self.latency = latency
        self.caches = []
        self.requests = []

    def add_cache(self, cache):
        self.caches.append(cache)

    def add_request(self, request):
        self.requests.append(request)
    
    def sort_request(self):
        sorted(self.requests, key=lambda r: r.n_req, reverse=True)

    def time_saved(self, cache, request):
        return (self.latency - cache.latency) * request.n_req

class Cache:
    def __init__(self, id, latency, size):
        self.id = id
        self.latency = latency
        self.size = size
        self.content = 0
        self.vids = []
        

    def can_add(self, v):
        return v + self.content < self.size

    def add(self, v):
        self.vids.append(v)
        self.content += v

class Request:
    def __init__(self, vid, n_req, v_size):
        self.vid = vid
        self.n_req = n_req
        self.v_size = v_size
        
        
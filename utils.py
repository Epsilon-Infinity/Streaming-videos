
import os
from models import Endpoint, Cache, Request

def readline(file):
    return list(map(int, file.readline().strip().split()))

def read_file(file_path):
    with open(file_path) as file:
        n_videos,  n_endpoints,  n_requests_des, n_caches, cache_size = readline(file)
        video_sizes = readline(file)
        endpoints = {}
        for i in range(n_endpoints):
            latency, catche_len =  readline(file)
            endpoint = Endpoint(i, latency)
            endpoints[i] = endpoint
            for i in range(catche_len):
                id, latency =  readline(file)
                endpoint.add_cache(Cache(id, latency, cache_size))
        for i in range(n_requests_des):
            vid, endpoint, n_req = readline(file)
            endpoints[endpoint].add_request(Request(vid, n_req, video_sizes[vid]))

        for v in endpoints.values():
            v.sort_request()

        return endpoints

        # return {'n_videos':n_videos, 'n_endpoints':n_endpoints, 'n_requests_des':n_requests_des,\
        #      'n_caches':n_caches, 'cache_size':cache_size, 'endpoints':endpoints, 'rides_list':rides_list}

def solve_files(dir, solver, out_dir='results'):
    result_dir = os.path.join(dir,"..",out_dir)
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    for file in os.listdir(dir):
        if not file.endswith('.in'):
            continue
        print("Solving file :",file)
        inputs = read_file(os.path.join(dir, file))
        print(inputs)
        output = solver(inputs)
        with open(os.path.join(result_dir,file+'.sol'), "w") as solution:
            for vehicle, rides in output.items():
                solution.write(str(vehicle) + ' ')
                solution.write(" ".join([str(i) for i in rides]) + "\n")

# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import rpc_hello_pb2
import rpc_hello_pb2_grpc
import time
import csv

# from rpc_echo_python_client import Connection, HelloRequest
# import time
# import csv
# from random import randbytes, randrange

# c = Connection("172.31.27.226:5000")

# for pow in range(7):
#     length = 10 ** pow
#     print(length)
#     time_l = []
#     for i in range(1000):
#         req_str = "a" * length
#         start = time.time()
#         req = HelloRequest(req_str)
#         o = c.say_hello(req)
#         end = time.time()
#         diff = end - start
#         time_l.append([str(i), diff])

#     with open(f"./data/mrpc_data_{length}.csv", "w") as f:
#         csvwriter = csv.writer(f)
#         csvwriter.writerows(time_l)

# print(sum(time_l)/len(time_l))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('172.31.27.226:50051') as channel:
        stub = rpc_hello_pb2_grpc.GreeterStub(channel)
        for pow in range(7):
            length = 10 ** pow
            time_l = []
            for i in range(1000):
                req_str = "a" * length
                start = time.time()
                response = stub.SayHello(rpc_hello_pb2.HelloRequest(name=req_str))
                end  = time.time()
                diff = end - start
                time_l.append([diff])
            with open(f"./data/mrpc_data_{length}.csv", "w") as f:
                csvwriter = csv.writer(f)
                csvwriter.writerows(time_l)
            
    print("Greeter client received: " + response.message)
    with open("grpc_data.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(time_l)


if __name__ == '__main__':
    logging.basicConfig()
    run()

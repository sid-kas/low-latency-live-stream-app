import os, sys, cv2, grpc

import butter_pb2
import butter_pb2_grpc

class GrpcButterStreamImpl(butter_pb2_grpc.VideoStreamServicer):

    def __init__(self):
        self.butter_stream_apis = {}

    def connect(self, request: butter_pb2.ConnectArg, context):
        
        

    def startStream(self, request, context):
       
        

    def stopStream(self, request, context):
    

    def disconnect(self, request, context):
       
        

def GrpcSrvice():
    def __init__(self):
        pass

    def serve(self):
        pass
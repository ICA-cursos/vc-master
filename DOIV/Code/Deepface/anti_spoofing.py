from deepface import DeepFace


help(DeepFace.stream)
DeepFace.stream(db_path = "./deepface",detector_backend='opencv',enable_face_analysis=False,time_threshold=5,frame_threshold=8)
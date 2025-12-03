import cv2
import os


def get_video_info(file_path):

    cap = cv2.VideoCapture(file_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file at {file_path}")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    duration = (frame_count / fps) / 60

    cap.release()

    return duration

def main():
    
    pfad = input("Pfad: ")
    os.chdir(pfad)
    file_list = os.listdir(".")

    total_duration = []

    for file in file_list:
        if file.endswith('mp4'):
            total_duration.append(get_video_info(file))

    duration = sum(total_duration)
    if duration > 60:
        duration /= 60

    print(f"{duration:5.2f}")

if __name__ == "__main__":
    main()

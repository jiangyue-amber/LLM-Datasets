# Software Name: Video_Scene_Recognition_Viewer
# Category: Video
# Description: The Video Scene Recognition Viewer is a software application that allows users to view and navigate videos based on automatically recognized scene changes. It utilizes computer vision algorithms to analyze the content of a video and identify different scenes based on visual cues and changes in frames.

import cv2
import numpy as np
import argparse
import os

def detect_scene_changes(video_path, threshold=30):
    """
    Detects scene changes in a video using frame differencing.

    Args:
        video_path (str): The path to the video file.
        threshold (int): The threshold for frame difference to be considered a scene change.

    Returns:
        list: A list of frame numbers where scene changes occur.
    """

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return []

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    scene_changes = [0]  # Scene changes always starts at the beginning
    prev_frame = None

    for frame_num in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray_frame)
            mean_diff = np.mean(diff)

            if mean_diff > threshold:
                scene_changes.append(frame_num)

        prev_frame = gray_frame

    cap.release()
    return scene_changes

def display_video_with_scenes(video_path, scene_changes):
    """
    Displays a video and allows navigation between scenes.

    Args:
        video_path (str): The path to the video file.
        scene_changes (list): A list of frame numbers where scene changes occur.
    """

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return

    current_scene_index = 0
    cap.set(cv2.CAP_PROP_POS_FRAMES, scene_changes[current_scene_index])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video Scene Recognition Viewer", frame)

        key = cv2.waitKey(30) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('n'):  # Next scene
            if current_scene_index < len(scene_changes) - 1:
                current_scene_index += 1
                cap.set(cv2.CAP_PROP_POS_FRAMES, scene_changes[current_scene_index])
        elif key == ord('p'):  # Previous scene
            if current_scene_index > 0:
                current_scene_index -= 1
                cap.set(cv2.CAP_PROP_POS_FRAMES, scene_changes[current_scene_index])
        elif key == ord('f'): # Go to the first frame
            current_scene_index = 0
            cap.set(cv2.CAP_PROP_POS_FRAMES, scene_changes[current_scene_index])
        elif key == ord('l'):  # Go to the last scene
            current_scene_index = len(scene_changes) -1
            cap.set(cv2.CAP_PROP_POS_FRAMES, scene_changes[current_scene_index])

    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="Video Scene Recognition Viewer")
    parser.add_argument("video_path", help="Path to the video file")
    parser.add_argument("--threshold", type=int, default=30, help="Threshold for scene change detection (default: 30)")

    args = parser.parse_args()

    if not os.path.exists(args.video_path):
        print(f"Error: Video file not found at {args.video_path}")
        return

    scene_changes = detect_scene_changes(args.video_path, args.threshold)
    print("Scene changes detected at frames:", scene_changes)
    display_video_with_scenes(args.video_path, scene_changes)


if __name__ == "__main__":
    main()
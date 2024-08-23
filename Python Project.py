# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:45:17 2024

@author: hillr
"""

import json
from datetime import datetime

# Function to load videos from file
def load_videos(filename="videos.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Function that saves videos to file
def save_videos(videos, filename="videos.json"):
    with open(filename, "w") as file:
        json.dump(videos, file)

# Function to validate video release year
def validate_year(year):
    try:
        year = int(year)
        if 1800 <= year <= datetime.now().year:
            return year
        else:
            print("Please enter a valid year between 1800 and the current year.")
            return None
    except ValueError:
        print("Please enter a valid numeric year.")
        return None

# Function to validate movie duration
def validate_duration(duration):
    try:
        duration = int(duration)
        if duration > 0:
            return duration
        else:
            print("Please enter a positive number for duration.")
            return None
    except ValueError:
        print("Please enter a valid numeric value for duration.")
        return None

# Function to add a new video
def add_video(videos):
    print("Enter video title: ", end="")
    title = input()
    print("Enter director: ", end="")
    director = input()

    release_year = None
    while not release_year:
        print("Enter release year: ", end="")
        release_year = validate_year(input())

    print("Enter genre: ", end="")
    genre = input()

    duration = None
    while not duration:
        print("Enter duration (in minutes): ", end="")
        duration = validate_duration(input())

    video = {
        "title": title,
        "director": director,
        "release_year": release_year,
        "genre": genre,
        "duration": duration
    }
    videos.append(video)
    save_videos(videos)
    print("Video added successfully!")

# Function to edit an existing video
def edit_video(videos):
    display_videos(videos)
    try:
        print("Enter the movie index: ", end="")
        index = int(input()) - 1
        if 0 <= index < len(videos):
            video = videos[index]
            print("Leave blank if you don't want to change a field.")
            video['title'] = input(f"Enter new title [{video['title']}]: ") or video['title']
            video['director'] = input(f"Enter new director [{video['director']}]: ") or video['director']

            new_year = input(f"Enter new release year [{video['release_year']}]: ")
            video['release_year'] = validate_year(new_year) if new_year else video['release_year']

            video['genre'] = input(f"Enter new genre [{video['genre']}]: ") or video['genre']

            new_duration = input(f"Enter new duration [{video['duration']}]: ")
            video['duration'] = validate_duration(new_duration) if new_duration else video['duration']

            save_videos(videos)
            print("Video updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

# Function that deletes a video
def delete_video(videos):
    display_videos(videos)
    try:
        print("Enter the movie index: ", end="")
        index = int(input()) - 1
        if 0 <= index < len(videos):
            videos.pop(index)
            save_videos(videos)
            print("Video deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

# Function that displays all videos by name
def display_videos(videos):
    if videos:
        for i, video in enumerate(videos, 1):
            print(f"{i}. {video['title']}")
    else:
        print("No videos available.")

# Function that display the detailed video information
def display_detailed_info(videos):
    try:
        print("Enter the movie index: ", end="")
        index = int(input()) - 1
        if 0 <= index < len(videos):
            video = videos[index]
            print(f"Title: {video['title']}")
            print(f"Director: {video['director']}")
            print(f"Release Year: {video['release_year']}")
            print(f"Genre: {video['genre']}")
            duration_hours = video['duration'] // 60
            duration_minutes = video['duration'] % 60
            print(f"Duration: {duration_hours} hours {duration_minutes} minutes")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

# Function that list all videos by criteria
def list_videos_by_criteria(videos):
    print("The following criteria is available:")
    print("1. Director.")
    print("2. Release Year.")
    print("3. Genre.")
    print("4. Duration.")
    print("Enter criteria: ", end="")
    criteria = input().strip()

    if criteria == "1":
        search_videos(videos, "director")
    elif criteria == "2":
        search_videos(videos, "release_year")
    elif criteria == "3":
        search_videos(videos, "genre")
    elif criteria == "4":
        search_videos(videos, "duration")
    else:
        print("Invalid criteria.")

# Function that searches videos by a specific field
def search_videos(videos, field):
    print(f"You selected {field.capitalize()}. The list of available {field}s is below:")
    unique_values = list(set(video[field] for video in videos))
    for i, value in enumerate(unique_values, 1):
        print(f"{i}. {value}")
    try:
        print("Enter selection: ", end="")
        selection = int(input()) - 1
        if 0 <= selection < len(unique_values):
            for video in videos:
                if video[field] == unique_values[selection]:
                    print(f"{videos.index(video) + 1}. {video['title']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
def main():
    videos = load_videos()
    print("Welcome to the Video Library Management System!")
    while True:
        print("Choose from the options below:")
        print("1. Add new video.")
        print("2. Edit video.")
        print("3. Delete video.")
        print("4. Display all videos by name.")
        print("5. Display detailed video information.")
        print("6. List videos by criteria.")
        print("7. Exit.")
        print("Enter your choice: ", end="")
        choice = input()

        if choice == '1':
            add_video(videos)
        elif choice == '2':
            edit_video(videos)
        elif choice == '3':
            delete_video(videos)
        elif choice == '4':
            display_videos(videos)
        elif choice == '5':
            display_detailed_info(videos)
        elif choice == '6':
            list_videos_by_criteria(videos)
        elif choice == '7':
            print("Thank you for using the Video Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

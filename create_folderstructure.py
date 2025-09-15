import os
import argparse

# Define full folder structure
FOLDER_STRUCTURE = {
    "torrents": [
        "books",
        "movies",
        "music",
        "tv",
        "anime/movies",
        "anime/tv",
    ],
    "usenet": [
        "incomplete",
        "complete/books",
        "complete/movies",
        "complete/music",
        "complete/tv",
        "complete/anime/movies",
        "complete/anime/tv",
    ],
    "ddl": [
        "incomplete",
        "complete/books",
        "complete/movies",
        "complete/music",
        "complete/tv",
        "complete/anime/movies",
        "complete/anime/tv",
    ],
    "media": [
        "books",
        "movies",
        "music",
        "tv",
        "anime/movies",
        "anime/tv",
        "personal/rip/movies",
        "personal/rip/tv",
        "personal/rip/anime/movies",
        "personal/rip/anime/tv",
        "personal/remux/movies",
        "personal/remux/tv",
        "personal/remux/anime/movies",
        "personal/remux/anime/tv",
    ]
}


def create_structure(base_path: str):
    """
    Create the 'data' folder structure under the given base path.

    :param base_path: Where to create the 'data' root folder.
    """
    data_root = os.path.join(base_path, "data")

    for category, subfolders in FOLDER_STRUCTURE.items():
        for sub in subfolders:
            folder_path = os.path.join(data_root, category, sub)
            os.makedirs(folder_path, exist_ok=True)
            print(f"[OK] Created: {folder_path}")

    print("\n✅ Folder structure created successfully at:", data_root)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create media server folder structure."
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Base directory where 'data' will be created (default: current directory)."
    )

    args = parser.parse_args()
    create_structure(args.path)

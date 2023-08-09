import zipfile


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive('compressed.zip',
                    'C:/Users/13mei/OneDrive/Desktop/Python_projects/lessons/60_days_code-python/app1 - ToDo/bonus')

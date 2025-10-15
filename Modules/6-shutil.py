import shutil

# shutil.copy('diff.png','new2.png')     # copy file

# shutil.copy2('diff.png','new2.png')     # copy file also preserves metadata of file

# shutil.copytree('Git','newGit')     # copy folder

# shutil.move('diff.png','Experiments/')      # Move folder or file

# shutil.rmtree('newGit')     # remove folder

# shutil.make_archive('newgit','zip','Git')       # create compressed archives

# shutil.unpack_archive('newgit.zip','newgit')        # extracts archive into directories

usage = shutil.disk_usage('/')

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024

print("Total:", format_size(usage.total))
print("Used :", format_size(usage.used))
print("Free :", format_size(usage.free))


import os

def get_files(path, suffix):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if (file.endswith(suffix)):
                files.append(os.path.join(r, file))
    return files

path = 'monthly_results'
files = get_files(path, '_monthly.csv')
print(files)

repos = [x.split('/')[1][:-12] for x in files]
print(repos)

with open('completed_repos.txt', 'w') as f:
    for repo in repos:
        f.write(repo + '\n')
